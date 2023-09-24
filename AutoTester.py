import serial.tools.list_ports
import sys

class Devices:
    def __init__(self, portaCom):
        self.portaCom = portaCom

    def sendAT(self, command):
        port = serial.Serial(self.portaCom,timeout=1)
        port.write(f"{command}\r\n".encode())
        resposta = port.read(1024)
        port.close()
        return resposta

    def adbShell(self): pass


class Conection:
    def __init__(self):
        self.__portas  = [port.device for port in serial.tools.list_ports.comports()]

    @property
    def ports(self):
        return self.__portas



conec = Conection()
for comP in conec.ports:
    print(Devices(comP).sendAT("ATI1"))