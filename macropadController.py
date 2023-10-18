import serial
import serial.tools.list_ports
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import win32api
from win32con import VK_MEDIA_NEXT_TRACK, VK_MEDIA_PLAY_PAUSE, VK_MEDIA_PREV_TRACK, KEYEVENTF_EXTENDEDKEY, KEYEVENTF_KEYUP, VK_VOLUME_UP, VK_VOLUME_DOWN, VK_VOLUME_MUTE, VK_F5

serialPort = None

previousVolume = [1.0, 1.0, 1.0]
previousEncoder = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
previousMute = [0, 0, 0]
apps = [["firefox.exe", "chrome.exe"], ["Teams.exe", "Discord.exe"], ["GenshinImpact.exe"]]
globalVolume = 1.0
digitalVolumeIncrement = 0.05

def processSerial(data):
    try:
        dataSplit = data.split(" ")
        if (dataSplit[0] == "s"):
            buttonHandler(int(dataSplit[1]), int(dataSplit[2]))
        elif (dataSplit[0] == "t"):
            switchHandler(int(dataSplit[1]), int(dataSplit[2]))
        elif (dataSplit[0] == "re"):
            rotaryEncoderHandler(int(dataSplit[1]), dataSplit[2].strip())
        elif (dataSplit[0] == "p"):
            potentiometerHandler(int(dataSplit[1]), int(dataSplit[2]))
    except Exception as e:
        print("processSerial error:")
        print(e)

def buttonHandler(buttonIndex, buttonState):
    try:
        # TODO: Identify hotkeys or macros to use
        if (buttonState == 1):
            if (buttonIndex == 1):
                print("Previous track")
                win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif (buttonIndex == 2):
                print("Play/Pause")
                win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif (buttonIndex == 3):
                print("Next track")
                win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif (buttonIndex == 4):
                print("Play/Pause")
                win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif (buttonIndex == 5):
                win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif (buttonIndex == 6):
                win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif (buttonIndex == 7):
                win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif (buttonIndex == 8):
                win32api.keybd_event(VK_F5, 0, KEYEVENTF_EXTENDEDKEY, 0)
    except Exception as e:
        print("buttonHandler error:")
        print(e)

def switchHandler(switchIndex, switchState):
    global previousMute
    try:
        if (switchState != previousMute[switchIndex]):
            previousMute[switchIndex] = switchState
            setMute(switchState, apps[switchIndex])
    except Exception as e:
        print("switchHandler error:")
        print(e)

def rotaryEncoderHandler(encoderIndex, encoderState):
    try:
        if (encoderIndex == 0):
            if (encoderState.lower() == "clockwise"):
                print("Volume up")
                win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif (encoderState.lower() == "counterclockwise"):
                print("Volume down")
                win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
    except Exception as e:
        print("rotaryEncoderHandler error:")
        print(e)

def potentiometerHandler(potentiometerIndex, potentiometerState):
    try:
        if (previousVolume[potentiometerIndex]/1024 != float(potentiometerState)):
            previousVolume[potentiometerIndex] = float(potentiometerState)/1024
            setVolume(previousVolume[potentiometerIndex], apps[potentiometerIndex])
    except Exception as e:
        print("rotaryEncoderHandler error:")
        print(e)

def setMute(muteIn, applicationNames):
    try:
        print(muteIn)
        print(applicationNames)
        for i in applicationNames:
            print("Setting mute to " + str(muteIn) + " for " + i)
            sessionVolume = getSessionVolume(i)
            if (sessionVolume != None):
                if (muteIn == 1):
                    sessionVolume.SetMute(0, None)
                else:
                    sessionVolume.SetMute(1, None)
    except Exception as e:
        print("setMute error:")
        print(e)

def setVolume(volumeIn, applicationNames):
    try:
        for i in applicationNames:
            print("Setting volume to " + str(round(volumeIn, 2)) + " for " + i)
            sessionVolume = getSessionVolume(i)
            if (sessionVolume != None):
                sessionVolume.SetMasterVolume(volumeIn, None)
    except Exception as e:
        print("setVolume error:")
        print(e)

def getSessionVolume(applicationName):
    try:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == applicationName:
                return session.SimpleAudioVolume
    except Exception as e:
        print("getSession error:")
        print(e)

def listPorts():
    for port in serial.tools.list_ports.comports():
        info = dict({"Name": port.name, "Description": port.description, "Manufacturer": port.manufacturer, "Hwid": port.hwid})
        print(info)
        if (port.description.__contains__("CH340")):
            global serialPort
            serialPort = serial.Serial(port=port.name, baudrate=9600, timeout=2)
            break

def main():
    global serialPort
    while True:
        try:
            if serialPort == None:
                listPorts()
                time.sleep(1)
            else:
                if serialPort.in_waiting > 0:
                    data = serialPort.readline().decode('ascii')
                    processSerial(data)
        except Exception as e:
            print("main error:")
            print(e)
            serialPort = None

main()