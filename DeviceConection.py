import subprocess
import serial.tools.list_ports
import multiprocessing.process
import time
import os

adbPath = os.getcwd() + "\\Adb\\adb.exe"

class Devices():
    def __init__(self, portaCom):
        self.portaCom = portaCom
        getinfo = self.sendAT("AT+DEVCONINFO")
        self.SN = getinfo[getinfo.index("SN")+3:getinfo.index("SN")+14]
        self.IMEI = getinfo[getinfo.index("IMEI")+5:getinfo.index("IMEI")+20]
        self.Model = getinfo[getinfo.index("MN")+3:getinfo.index("MN")+11]
        self.__deviceShell = subprocess.Popen([adbPath, "-s", self.SN, "shell"], stderr=subprocess.PIPE,
                                              stdout=subprocess.PIPE,
                                              stdin=subprocess.PIPE,
                                              text=True)



    def sendAT(self, command: str):
        port = serial.Serial(self.portaCom,timeout=3)
        port.write(f"{command}\r\n".encode())
        resposta = port.read(1024)
        port.close()
        return resposta.decode()


    def adbShell(self, command):
        self.__deviceShell.stdin.write(command)
        saida, erro = self.__deviceShell.communicate()
        return saida, erro


class Conection:
    def __init__(self):
        self.__portas  = [port.device for port in serial.tools.list_ports.comports()]


    @property
    def ports(self):
        return self.__portas

conec = Conection()
processos = []

if __name__ == '__main__':
    for comP in conec.ports:

        test = Devices(comP)
        processos.append(test)

    for processo in processos:
        saida,a = processo.adbShell("getprop")
        print("saida:",saida)