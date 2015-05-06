# COSC 5P71 Assignment 2 #

## Software required ##

Besides the usual Python install the following modules are needed:
	- DEAP
	- NUMPY
	- MATPLOTLIB
	- SCIPI
	
## 4 Forks of the Code ##
	- The code is broken down into 4 main distinctions
		- provided textures
			- language A
			- language B
		- bonus textures
			- language A
			- language B
	- Each of the 4 main distinctions are a different variation of the main code listed below:

## Main Code Components ##
	- `assign_2.py` - does the GP evolution and on training data
	- `blast_out` - script that resets all logs and clears out precalculated points
	- `filter_functions.py` - definition of the image filter functions (ie AVG3)
	- `generate_data` - script that peforms 10 runs of each of the 4 textures
	- `paramset.txt` - One stop shop to set relavent GP parameters
	- `pregenerate_data.py` - for pre-calculating numeric value of filter functions on random training points
	- `setup` - Helper script that makes the required directories
	- `testing.py` - Peforms the calculations necessary on the testing data to generate peformance images, confustion matrix data, etc
	- `training_points.py` - Generates the random points to be used for training on the 4 textures, saves as text files
	- `visualize_training_points.py` - generates an image of all of the training points generated. Usefull for debugging

## Sub-Directories ##
	- `brodatz` - texture files to be use
	- `confusion` - csv files of the testing data for confusion matrix generation
	- `filter_values` - pre calculated filter values saved as python _pickels_
	- `fitness_plots` - code to generate the image files of the fitness plots, text files of multirun scores, image files of results, a couple helper scripts to do the work
	- `gp_found` - text representations of the best GPs found in the runs
	- `images` - where all performance images are saved
	- `logs` - raw text file logs of the GP runs
	- `testing` - Python _pickels_ of testing data from the tail end of `assign_2.py`
	- `testing_points` csv and _pickels_ of the testing points required

## Running the software ##
	- adjust parameter values for run in `paramset.txt`
	- `generate_data` does the main evolutions
	- create fitness plots with code in `fitness_plots`
	- run explict tests using `testing.py`



