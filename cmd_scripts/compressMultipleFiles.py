# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:12:48 2015

@author: ajaver
"""

from MWTracker.batchProcessing.processMultipleFilesFun import compressMultipleFilesFun
from MWTracker.batchProcessing.ProcessMultipleFilesParser import CompressMultipleFilesParser

if __name__ == '__main__':
    args = CompressMultipleFilesParser().parse_args()
    compressMultipleFilesFun(**vars(args))
