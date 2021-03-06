# Multiworm_Tracking

This repository contains my work on the multiworm tracker for the [MRC-CSC](http://csc.mrc.ac.uk/) [Behavioral Genomics Group](http://behave.csc.mrc.ac.uk/).

# Installation

## Requirements.
- Python 3 + numpy matplotlib pytables pandas h5py scipy scikit-learn scikit-image seaborn xlrd pyqt cython
- ffmpeg
- openCV3
- hdf5
- Cython including a compatible C/C++ compiler.
- Additionally it requires to clone the [open-worm-analysis-toolbox](https://github.com/openworm/open-worm-analysis-toolbox) from OpenWorm for the feature extraction.

## Installation using python homebrew (OS X)
Run `bash installation_script.sh brew`. If it is not a clean installation, I cannot warranty this script will work since I have encountered conflict with previous versions of the libraries installed by homebrew. In the future I might develop a script that allow to remove previous installations.
 
## Installation using anaconda (OS X/Linux).
Run `bash installation_script.sh`.
On linux there might be some problems with dependencies. It might be requiered to install from scratch ffmpeg and pyqt5.

## Manual installation (Windows)
- Download and install [git tools for windows](https://git-scm.com/download/win). Make sure to select "Select Windows' default window". Otherwise you will have to use MinTTY as command line.
- Clone this repository and  [OpenWorm analysis toolbox](https://github.com/openworm/open-worm-analysis-toolbox):
```
git clone https://github.com/ver228/Multiworm_Tracking
git clone https://github.com/openworm/open-worm-analysis-toolbox
```
- Install [ffmpeg](https://ffmpeg.org/download.html). [Here](http://adaptivesamples.com/how-to-install-ffmpeg-on-windows/) are friendly installation instructions.
- Download [anaconda](https://www.continuum.io/downloads) or [miniconda](http://conda.pydata.org/miniconda.html) with python 3.5.
- If you install miniconda install the following packages:
```
conda install -y anaconda-client conda-build numpy matplotlib pytables pandas h5py scipy scikit-learn scikit-image seaborn xlrd statsmodels
```
- Install additionally dependencies:
```
pip install gitpython pyqt5
conda install -c https://conda.binstar.org/ver228 opencv3
```
- Go to open-worm-analysis-toolbox directory and run `python3 setup.py develop`
- Go to open-worm-analysis-toolbox/open_worm_analysis_toolbox  and change the file `user_config_example.txt` to `user_config.py`
- Go the the Multiworm_Tracking directory and run `python3 setup.py develop`
- Try to run `python -c "import cv2; import h5py; import MWTracker; import open_worm_analysis_toolbox"`. You should recieve no error messages.
##Issues
- If you recieve an error related with a module in segWormPython you will need to compile the cython files. It will require the same C compiler used to compile python. On OS X you need to install xcode using the app store. On Windows using python 3.5 you have to install [visual studio community 2015](https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx) (use custom installation and select Visual C++). Then run `python3 setup.py build_ext --inplace` in the directory `Multiworm_Tracking/MWTracker/trackWorms/segWormPython/cythonFile`, and try to check again if it was a succesful installation.


