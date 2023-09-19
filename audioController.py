import serial
import serial.tools.list_ports
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

serialPort = None

previousVolume = [0.0, 0.0, 0.0]
previousMute = ["0", "0", "0"]
apps = [["chrome.exe", "firefox.exe"], ["Teams.exe", "Discord.exe"], ["GenshinImpact.exe"]]

def processSerial(data):
    try:
        global previousVolume
        global apps
        split = data.split("|")
        switches = split[0].split(" ")
        potentiometers = split[1].split(" ")

        for i in range(len(potentiometers)):
            volume = round(float(potentiometers[i])/5.0, 2)
            if volume != previousVolume[i] or switches[i] != previousMute[i]:
                previousVolume[i] = volume
                previousMute[i] = switches[i]
                setVolume(float(volume), apps[i], switches[i] == "0")

    except Exception as e:
        print("processSerial error:")
        print(e)

def setVolume(volumeIn, applicationNames, muted=False):
    try:
        for i in applicationNames:
            print("Setting volume to " + str(volumeIn) + " for " + i)
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                if session.Process and session.Process.name() == i:
                    volume = session.SimpleAudioVolume
                    if muted:
                        print("Muting " + i + "")
                        volume.SetMute(1, None)  # Mute
                    else:
                        volume.SetMute(0, None)  # Unmute
                        volume.SetMasterVolume(volumeIn, None)
                    break
    except Exception as e:
        print("setVolume error:")
        print(e)

def listPorts():
    for port in serial.tools.list_ports.comports():
        info = dict({"Name": port.name, "Description": port.description, "Manufacturer": port.manufacturer, "Hwid": port.hwid})
        print(info)
        if (port.description.__contains__("Arduino")):
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