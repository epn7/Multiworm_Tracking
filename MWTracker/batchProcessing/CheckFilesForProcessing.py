# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:12:48 2015

@author: ajaver
"""

import os
from MWTracker.helperFunctions.timeCounterStr import timeCounterStr
from MWTracker.batchProcessing.helperFunc import create_script
from MWTracker.batchProcessing.ProcessWormsLocal import SCRIPT_LOCAL
from MWTracker.batchProcessing.AnalysisPoints import AnalysisPoints


class CheckFilesForProcessing(object):
    def __init__(self, video_dir_root, mask_dir_root, 
                 results_dir_root, tmp_dir_root='', 
                 json_file='', analysis_checkpoints = [], 
                 is_single_worm = False, no_skel_filter=False,
                  is_copy_video = True):
        
        def _testFileExists(fname, type_str):
            if fname:
                fname =  os.path.abspath(fname)
                if not os.path.exists(fname):
                    raise FileNotFoundError(
                    '%s, %s does not exist.' % fname)
            return fname
        
        def _makeDirIfNotExists(fname):
            if fname:
                fname =  os.path.abspath(fname)
                if not os.path.exists(fname):
                    os.makedirs(fname)
            return fname
        
        # checkings before accepting the data
        self.video_dir_root = _testFileExists(video_dir_root, 'Videos root directory')
        self.mask_dir_root = _makeDirIfNotExists(mask_dir_root)
        self.results_dir_root = _makeDirIfNotExists(results_dir_root)
        self.json_file = _testFileExists(json_file, 'Parameters json file')
        
        self.tmp_dir_root = _makeDirIfNotExists(tmp_dir_root)
        
        self.is_single_worm = is_single_worm
        self.is_copy_video = is_copy_video
        self.use_skel_filter = not no_skel_filter
        
        self.analysis_checkpoints = analysis_checkpoints
        self.filtered_files = {}
    

    def _checkIndFile(self, video_file):
        '''Check the progress in the file.'''
        video_dir, video_file_name = os.path.split(video_file)
        subdir_path = self._getSubDirPath(video_dir, self.video_dir_root)
        
        mask_dir = os.path.join(self.mask_dir_root, subdir_path)
        results_dir = os.path.join(self.results_dir_root, subdir_path)
        
        ap_obj = AnalysisPoints(video_file, mask_dir, results_dir, self.json_file,
                 self.is_single_worm, self.use_skel_filter)
        
        unfinished = ap_obj.getUnfinishedPoints(self.analysis_checkpoints)
        
        if len(unfinished) == 0:
            msg = 'FINISHED_GOOD'
        elif unfinished != self.analysis_checkpoints:
            msg =  'FINISHED_BAD'
        elif self.analysis_checkpoints:
            unmet_requirements = ap_obj.hasRequirements(self.analysis_checkpoints[0])
            if len(unmet_requirements) == 0:
                msg = 'SOURCE_GOOD'
            else:
                msg ='SOURCE_BAD'
                #print(self.analysis_checkpoints[0], unmet_requirements)
                #print(ap_obj.file_names['masked_image'])
        else:
            msg = 'EMPTY_ANALYSIS_LIST'
        
        return msg, ap_obj
    
    
    def _getSubDirPath(self, source_dir, source_root_dir):
        '''Generate the destination dir path keeping the same structure 
        as the source directory'''
        subdir_path = source_dir.replace(source_root_dir, '')
        # consider the case the subdirectory is only a directory separation
        # character
        if subdir_path and subdir_path[0] == os.sep:
            subdir_path = subdir_path[1:] if len(subdir_path) > 1 else ''
        
        return subdir_path
    

    def filterFiles(self, valid_files):
        # intialize filtered files lists
        filtered_files_fields = (
            'SOURCE_GOOD',
            'SOURCE_BAD',
            'FINISHED_GOOD',
            'FINISHED_BAD',
            'EMPTY_ANALYSIS_LIST')
        self.filtered_files = {key: [] for key in filtered_files_fields}
        
        progress_timer = timeCounterStr('')
        for ii, video_file in enumerate(valid_files):
            label, ap_obj = self._checkIndFile(video_file)
            self.filtered_files[label].append(ap_obj)
            
            if (ii % 10) == 0:
                print('Checking file {} of {}. Total time: {}'.format(ii + 1, 
                      len(valid_files), progress_timer.getTimeStr()))

        print('''Finished to check files.\nTotal time elapsed {}\n'''.format(progress_timer.getTimeStr()))
        msg = '''Files to be proccesed :  {}
Invalid source files  :  {}
Files that were succesfully finished: {}
Files whose analysis is incompleted : {}'''.format(
                len(self.filtered_files['SOURCE_GOOD']),
                len(self.filtered_files['SOURCE_BAD']),
                len(self.filtered_files['FINISHED_GOOD']),
                len(self.filtered_files['FINISHED_BAD']))
        print(msg)
        
        return self.getCMDlist()
    
    def _printUnmetReq(self):
        def _get_unmet_requirements(ap_obj):
            for requirement in ap_obj.unmet_requirements:
                if requirement in ap_obj.checkpoints:
                    provenance_file = ap_obj.checkpoints[requirement]['provenance_file']
                    requirement = '{} : {}'.format(requirement, provenance_file)
                return requirement

        dd = map(_get_unmet_requirements, self.filtered_files['SOURCE_BAD'])
        dd ='\n'.join(dd)
        print(dd)
        return dd


    def getCMDlist(self):
        A = map(self.generateIndCMD, self.filtered_files['SOURCE_GOOD'])
        B = map(self.generateIndCMD, self.filtered_files['FINISHED_BAD'])
        return list(A) + list(B)

    def generateIndCMD(self, good_ap_obj):

        subdir_path = self._getSubDirPath(
            os.path.dirname(good_ap_obj.video_file),
            self.video_dir_root)
        
        tmp_mask_dir = os.path.join(self.tmp_dir_root, 'MaskedVideos', subdir_path)
        tmp_results_dir = os.path.join(self.tmp_dir_root, 'Results', subdir_path)
        
        args = [good_ap_obj.video_file]
        argkws = {'masks_dir':good_ap_obj.masks_dir, 
                  'results_dir':good_ap_obj.results_dir,
            'tmp_mask_dir':tmp_mask_dir, 'tmp_results_dir':tmp_results_dir,
            'json_file':self.json_file, 'analysis_checkpoints':self.analysis_checkpoints,
            'is_single_worm':self.is_single_worm, 'use_skel_filter':self.use_skel_filter,
            'is_copy_video':self.is_copy_video}
        
        cmd = create_script(SCRIPT_LOCAL, args, argkws)
        return cmd
