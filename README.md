# Python Arduino Serial Volume Controller
## This project uses Python to process Serial data from an Arduino to control the volume of applications on a Windows PC.
The Arduino is assumed to have three toggle switches and 3 potentiometers connected to it. The toggle switches are used to mute a group of applications, and the potentiometers are used to control the volume of a group of applications. The Arduino is connected to the PC via USB, and the Python script is used to process the serial data from the Arduino and control the volume of the applications.

## Setup
### Arduino
> Connect three toggle switches and 3 potentiometers to the Arduino.
> Copy the `Potentiometer.ino` file to the Arduino and upload it.

### Python
> Python 3.7.4 was used for this project and is necessary to run the script. The following packages are also required:
> - `pyserial`
> - `pycaw`

> To install the packages, run the following commands in the terminal:
> - `pip install pyserial`
> - `pip install pycaw`

### Windows
> The script was tested on Windows 10, but should work on Windows 7, 8, and 11 as well. The script uses the Windows Core Audio API to control the volume of the applications. The script will not work on Linux or Mac.
> I am currently working on making a Visual Basic script that will be triggered on startup to run the Python script in the background. This will allow the script to run on startup and will not require the user to open the script manually.

### Adding and Removing Applications
> The apps list in `audioController.py` contains the names of the applications that the script will control. To add an application, simply add the name of the application to the list. To remove an application, remove the name of the application from the list. The names of the applications can be found in the Volume Mixer. The list has 3 sublists containing strings with the names of each application. The subslists are used to group applications together to be controlled by the same potentiometer and toggle switch on the Arduino.

## Notes
I intend to improve the Arduino logic to be cleaner and more efficient in the number of pins it uses. I 3D printed my housing for the Arduino, toggle switches, and potentiometers. I intend to make the files for the housing available in the future.