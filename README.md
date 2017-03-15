# liveDataDisplay
This code can be used to visualize kinetic energy and courant number while the simulation is running.

Requirements:
- Textfile that states DEM-timestep and total kinetik energy (seperated by tab and one timestep each line)
- A CFD(EM) logfile in which courant number (mean and max) is printed. Program searches for keywords and collects data from the logfile

Required Adjustment:
- Size of DEM-timestep needs to be adjusted to your given value
- Pathes to files need to be changed in accordance to your needs
