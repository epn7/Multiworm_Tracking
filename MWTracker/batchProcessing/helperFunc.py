# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:59:08 2016

@author: ajaver
"""
import os
import sys
import fnmatch

def walkAndFindValidFiles(root_dir, pattern_include='*', pattern_exclude=''):
    invalid_ext = [
                '*_intensities.hdf5',
                '*_skeletons.hdf5',
                '*_trajectories.hdf5',
                '*_features.hdf5',
                '*_feat_ind.hdf5']
    
    if not pattern_exclude:
        pattern_exclude = []
    elif not isinstance(pattern_exclude, (list, tuple)):
        pattern_exclude = [pattern_exclude]
    pattern_exclude += invalid_ext
    print(root_dir)
    return _walkAndFind(root_dir, 
                        pattern_include = pattern_include, 
                        pattern_exclude = pattern_exclude)

def _walkAndFind(root_dir, pattern_include='*', pattern_exclude=''):
    root_dir = os.path.abspath(root_dir)
    assert os.path.exists(root_dir)

    # if there is only a string (only one pattern) let's make it a list to be
    # able to reuse the code
    if not isinstance(pattern_include, (list, tuple)):
        pattern_include = [pattern_include]
    if not isinstance(pattern_exclude, (list, tuple)):
        pattern_exclude = [pattern_exclude]

    valid_files = []
    for dpath, dnames, fnames in os.walk(root_dir):
        for fname in fnames:
            good_patterns = any(fnmatch.fnmatch(fname, dd)
                                for dd in pattern_include)
            bad_patterns = any(fnmatch.fnmatch(fname, dd)
                               for dd in pattern_exclude)
            if good_patterns and not bad_patterns:
                fullfilename = os.path.abspath(os.path.join(dpath, fname))
                assert os.path.exists(fullfilename)
                valid_files.append(fullfilename)

    return valid_files

def getRealPathName(fullfile):
    '''get the path name that works with pyinstaller binaries'''
    try:
        base_name = os.path.splitext(os.path.basename(fullfile))
        # use this directory if it is a one-file produced by pyinstaller
        script_cmd = [os.path.join(sys._MEIPASS, base_name)]
        if os.name == 'nt':
            script_cmd[0] += '.exe'
        return script_cmd
    except Exception:
        return [sys.executable, os.path.realpath(fullfile)]

def create_script(base_cmd, args, argkws):
    cmd = base_cmd + args
    for key, dat in argkws.items():
        if isinstance(dat, bool):
            if dat:
                cmd.append('--' + key)
        elif isinstance(dat, (list, tuple)):
            cmd += ['--'+key] + list(dat)
        else:
            cmd += ['--' + key, str(dat)]
    return cmd


def getDefaultSequence(action, is_single_worm=False, use_skel_filter=True):
    assert any(action == x for x in ['Compress', 'Track', 'All'])
    if is_single_worm:
        CHECKPOINTS_DFT = { 'Compress': ['COMPRESS',
                                        'COMPRESS_ADD_DATA'],
                            'Track' : ['TRAJ_CREATE',
                                        'TRAJ_JOIN',
                                        'SKE_CREATE',
                                        'STAGE_ALIGMENT',
                                        'SKE_FILT',
                                        'SKE_ORIENT',
                                        'INT_PROFILE',
                                        'INT_SKE_ORIENT',
                                        'CONTOUR_ORIENT',
                                        'FEAT_CREATE']}
    else:
        CHECKPOINTS_DFT = { 'Compress': ['COMPRESS'],
                            'Track' : ['TRAJ_CREATE',
                                    'TRAJ_JOIN',
                                    'SKE_CREATE',
                                    'SKE_FILT',
                                    'SKE_ORIENT',
                                    'INT_PROFILE',
                                    'INT_SKE_ORIENT',
                                    'FEAT_CREATE']}
    
    if not use_skel_filter:
        CHECKPOINTS_DFT['Track'].remove('SKE_FILT')
    
    if action == 'All':
        return CHECKPOINTS_DFT['Compress'] + CHECKPOINTS_DFT['Track']
    else:
        return CHECKPOINTS_DFT[action]

