# Self_Driving_Car_Simulation
Using CNNs and Behavioral Cloning , train a car to self-drive on a track in Unity3D simulation

The project makes use of the technique called Behavioral
Cloning along with Deep Learning to train the model to drive a car on its own in a simulation
environment. It includes the generation of data, pre-processing of data and training the Convolutional
Neural Networks and tuning the model to work well in test track.

 Dataset for the training of the model was collected using [Udacity-Self-Driving-simulator](https://github.com/udacity/self-driving-car-sim).The files also include a trained model i.e **_model-0.0426.h5_**. Below is the detailed description about how the model was trained, preprocessing that was done on data and the video of the project in action where the model drives the car on its own.
 
 ### Prerequisites
 Keras, TensorFlow, OpenCV, flask, eventlet, python-socketio
 
1.Install the project dependecies:
- Flask : ```$ pip install Flask```
- Numpy : ``` $ pip install numpy```
- SocketIO : ```$ pip install socketio``` 
- Eventlet : ```$ pip install eventlet```
- PIL : ```$ pip install Pillow```
- Keras : ```$ pip install keras```
- argparse : ```$ pip install argparse```

2.Download the simulator from [Udacity-Self-Driving-simulator](https://github.com/udacity/self-driving-car-sim#avaliable-game-builds-precompiled-builds-of-the-simulator)

### Run Simulation
1. Clone the repository or [Download as zip](https://github.com/venkma/Self_Driving_Car_Simulation.git).<br>
2. Run the simulator.Choose the 'lake track' and click on Autonomous mode.<br>
3. Run the python script **_"Run_Simulation.py"_** Using your Favourite IDE and make sure **_"model.h5"_** file in same directory as that of the script.


## Demo

**_Click Below Image To See The Project in Action_**
[![Self_Driving_Simulation_In_Action](https://drive.google.com/file/d/1R4I5yvVPaYlRJl0GRiDM6ur6_xH9y_lS/view?usp=sharing)](https://youtu.be/yifmgYiCRBc)
