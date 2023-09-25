import subprocess as sb
import serial.tools.list_ports
import sys

class Devices():
    def __init__(self, portaCom):
        self.portaCom = portaCom
        getinfo = self.sendAT("AT+DEVCONINFO")
        self.SN = getinfo[getinfo.index("SN")+3:getinfo.index("SN")+14]
        self.IMEI = getinfo[getinfo.index("IMEI")+5:getinfo.index("IMEI")+20]
        self.Model = getinfo[getinfo.index("MN")+3:getinfo.index("MN")+11]


    def sendAT(self, command: str):
        port = serial.Serial(self.portaCom,timeout=1)
        port.write(f"{command}\r\n".encode())
        resposta = port.read(1024)
        port.close()
        return resposta.decode()


    def adbShell(self): pass


class Conection:
    def __init__(self):
        self.__portas  = [port.device for port in serial.tools.list_ports.comports()]


    @property
    def ports(self):
        return self.__portas

conec = Conection()
md = []
for comP in conec.ports:
    test = Devices(comP)
    md.append(test)

for obj in md:
    print(f"Serial: {obj.SN}\nIMEI:{obj.IMEI}\nModel:{obj.Model}")

#test[test.index("MN")+3:test.index("MN")+11]
