#!/usr/bin/env python3
import serial
import os
from time import sleep

##############################################################################
# 1 = [10%], 2 = [25%], 3 = [50%], 4 = [100%]
shutdown_battery_level = 2;
##############################################################################
shutdown = False #Temporary variable

ser = serial.Serial(
 port='/dev/serial0',
 baudrate = 38400,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)

breakS = 0.1
breakL = 0.5

def checkPower():
 global shutdown
 x=ser.readline()
 try : 
  y = x.decode(encoding='UTF-8',errors='strict')
  if y.find('xxx--StromPiPowerBack--xxx\n') != -1:
    print ("PowerBack - Raspberry Pi Shutdown aborted")
    shutdown = False
  elif y.find('xxx--StromPiPowerfail--xxx\n') != -1:
    print (f"PowerFail - Raspberry Pi Shutdowwn on battery level {shutdown_battery_level}")
    shutdown = True
  else: 
    return y 
 except Exception as e:
     pass

while 1:
 checkPower()
 if shutdown is True:
  ser.write(str.encode('quit'))
  sleep(breakS)
  ser.write(str.encode('\x0D'))
  sleep(breakL)

  ser.write(str.encode('status-rpi'))
  sleep(1)
  ser.write(str.encode('\x0D'))
  for n in range(22):
    checkPower()
  battery_level = int(checkPower())
  for n in range(15):
    checkPower()
  if battery_level <= shutdown_battery_level and shutdown is True :
    print("Shutting down...")
    os.system("sudo shutdown -h now")
