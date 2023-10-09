import serial
import serial.tools.list_ports
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import win32api
from win32con import VK_MEDIA_NEXT_TRACK, VK_MEDIA_PLAY_PAUSE, VK_MEDIA_PREV_TRACK, KEYEVENTF_EXTENDEDKEY, KEYEVENTF_KEYUP

serialPort = None

previousData = ""
previousVolume = [1.0, 1.0, 1.0]
previousEncoder = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
previousMute = [0, 0, 0]
apps = [["firefox.exe", "chrome.exe"], ["Teams.exe", "Discord.exe"], ["GenshinImpact.exe"]]
digitalVolumeIncrement = 0.05

def processSerial(data):
    try:
        global previousData
        if (data != previousData):
            previousData = data
            dataSplit = data.split("|")
            for i in range(len(dataSplit)):
                split = dataSplit[i].split(":")
                if (split[0].__contains__("S ")):
                    switchHandler(split[0], split[1])
                elif (split[0].__contains__("RE ")):
                    rotaryEncoderHandler(int(split[0].split(" ")[2]), split[1], i)
                elif (split[0].__contains__("P ")):
                    potentiometerHandler(split[0], split[1])
    except Exception as e:
        print("processSerial error:")
        print(e)

def switchHandler(switchIndex, switchState):
    global previousMute
    try:
        switches = switchState.split(" ")
        for i in range(len(switches) - 1):
            if (int(switches[i]) != previousMute[i]):
                previousMute[i] = int(switches[i])
                setMute(switches[i], apps[i])
    except Exception as e:
        print("switchHandler error:")
        print(e)

def rotaryEncoderHandler(encoderIndex, encoderState, inputIndex):
    global previousEncoder
    try:
        clk = int(encoderState.split(" ")[0])
        dt = int(encoderState.split(" ")[1])
        sw = int(encoderState.split(" ")[2])
        if (clk != previousEncoder[encoderIndex][0]):
            if (dt != clk):
                if (previousVolume[encoderIndex] < 1.0):
                    previousVolume[encoderIndex] += digitalVolumeIncrement
            else:
                if (previousVolume[encoderIndex] > 0.0):
                    previousVolume[encoderIndex] -= digitalVolumeIncrement
            setDigitalVolume(previousVolume[encoderIndex], apps[encoderIndex])
            previousEncoder[encoderIndex][0] = clk
            previousEncoder[encoderIndex][1] = dt
        if (sw != previousEncoder[encoderIndex][2]):
            if (sw == 0):
                if (inputIndex == 1):
                    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
                elif (inputIndex == 2):
                    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
                elif (inputIndex == 3):
                    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
            previousEncoder[encoderIndex][2] = sw
    except Exception as e:
        print("rotaryEncoderHandler error:")
        print(e)

def potentiometerHandler(encoderIndex, encoderState):
    try:
        potentiometerSet = int(encoderIndex.split(" ")[1])

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
                if (muteIn == "1"):
                    sessionVolume.SetMute(0, None)
                else:
                    sessionVolume.SetMute(1, None)
    except Exception as e:
        print("setMute error:")
        print(e)

def setDigitalVolume(volumeIn, applicationNames):
    try:
        for i in applicationNames:
            print("Setting volume to " + str(round(volumeIn, 2)) + " for " + i)
            sessionVolume = getSessionVolume(i)
            if (sessionVolume != None):
                sessionVolume.SetMasterVolume(volumeIn, None)
    except Exception as e:
        print("setDigitalVolume error:")
        print(e)

def setAnalogVolume(volumeIn, applicationNames):
    try:
        for i in applicationNames:
            print("Setting volume to " + str(volumeIn) + " for " + i)
            volume = getSessionVolume(applicationNames[i])
            volume.SetMasterVolume(volumeIn, None)
            break
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