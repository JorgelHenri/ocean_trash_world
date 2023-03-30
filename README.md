Installation instructions:
  - Follow the installation processes at https://github.com/ctu-mrs/mrs_uav_system;
  - Setup and install dependencies 
```
sudo apt-get update
sudo apt-get install libfftw3-dev
sudo apt-get install libclfft-dev
sudo apt-get install libcgal-dev
```
  - In the home/workspace/src directory clone this package;
  - Run a catkin build;
  - Using terminal access home/workspace/src/ocean_trash_world/offshore_uav_pack/start;
  - Run this command on the terminal:
  
    $ ./start.sh
  - Before "starting" the simulation, just run the second script in the tmux spawn window, to spawn the USV
  - Now press play on the gazebo.

  PS: If you want to change the way the garbage is being generated, go to the random_trash folder and run the pyhton application "ilhalixoLaunch.py", on lines 14 to 23 you can see some parameters that you can change to make different patterns with the garbage. Once you run the code, you need to get the trash.launch file that is overwritten in the folder, and replace it in the start folder in offshore_uav_pack. (PACKAGE/offshore_uav_pack/start).
