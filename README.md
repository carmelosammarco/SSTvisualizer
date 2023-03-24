# SSTvisualizer
Visualizing sea surface temperature data in a way that it is easy to understand and interpret.

## Anaconda environment installation:

Please to run the following code using the "environment.yml" file in the root folder:

```
conda env create -f environment.yml
```

To activate the evironment run:

```
conda activate PyLab4NetCDF
```

At this point your environment should be functional and ready to go!


## How the folder is structured:

## Go inside the "SRC" folder and the impotant thing to know are:

- **TEST-DATA** folder that contains the starting NetCDF file to be processed

- **PNG** folder that contains all the imaged created for each time step (the image will be numbered in a integer range starting from 0)

- **lib** folder that contains the python modules needed to process the data and called by "main.py" script

- **main.py** script that allows to start the proccesing.

## From the main.py file we can modify:

- **input data**: "infile" variable with the path to data to process

- **dpi**: resolution of our image

- **fps**: frame for second -  the velocity of the animation in simpler terms

---

## How to start with my data inside TEST-DATA (relative to the SST on August 2022)

### just run the **"main.py"** script once you finisched to settting up your python environment

#### You are going to observe:

- The PNG folder is going to be fill up by map images one for each time steps.

- When the first process, described in the previous step, ends then a second process will stack cronologically all the images produced, generating a GIFF file.

##### **Many thanks to visit this page**