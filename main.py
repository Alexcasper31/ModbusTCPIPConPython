import time
from pyModbusTCP.client import ModbusClient

c=ModbusClient(host='192.168.1.130',port=5050,auto_open=True,debug=False)

while True:
    coils_l=c.read_coils(0,10)
    if coils_l:
        print("oo",coils_l)
    else :
        print("nel")
    time.sleep(2)