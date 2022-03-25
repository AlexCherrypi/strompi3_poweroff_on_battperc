# strompi3_poweroff_on_battperc
Rebooting the RaspberryPi when the Strompi3 looses power and reaches specified battery percentage

for V1.73

```
---------------------------------
StromPi-Status:
---------------------------------
Time: 05:33:36
Date: Tuesday 01.05.18

StromPi-Output: mUSB

StromPi-Mode: mUSB -> Battery

Raspberry Pi Shutdown: Disabled
 Shutdown-Timer: 60 seconds

Powerfail Warning: Enabled

Serial-Less Mode: Disabled

Power Save Mode: Disabled

PowerOn-Button: Enabled

 PowerOn-Button-Timer: 30 seconds

Battery-Level Shutdown: 10%

Powerfail-Counter: 52

PowerOff Mode: Disabled
---------------------------------
Alarm-Configuration:
---------------------------------
WakeUp-Alarm: Disabled
 Alarm-Mode: Time-Alarm
 Alarm-Time: 01:01
 Alarm-Date: 01.01
 WakeUp-Alarm: Monday
 Weekend Wakeup: Enabled
 Minute Wakeup Timer: 01 minutes

PowerOff-Alarm: Disabled
 PowerOff-Alarm-Time: 00:00

Interval-Alarm: Disabled
 Interval-On-Time: 01 minutes
 Interval-Off-Time: 01 minutes

---------------------------------
Voltage-Levels:
---------------------------------
Wide-Range-Inputvoltage:  not connected
LifePo4-Batteryvoltage: 3.316V [100%] [charging]
microUSB-Inputvoltage: 4.926V
Output-Voltage: 4.885V
```

There is also a version to reboot with the shutdown.py script as a systemd service as described in https://strompi.joy-it.net/en/helpdesk/252
