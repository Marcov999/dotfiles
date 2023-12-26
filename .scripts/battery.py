from time import sleep
import os

cmd = 'cat /sys/class/power_supply/BAT0/capacity'
vol = os.popen(cmd).read()
cmd = 'acpi'
dis = os.popen(cmd).read()
plugged = not 'Discharging' in dis
vol = vol[0:len(vol)-1]
val = int(vol)
if not plugged:
    # plugged=""
    if val > 70:
        plugged = ''
    elif val > 50:
        plugged = ''
    elif val > 30:
        plugged = ''
    else:
        plugged = ''
else:
    plugged=""
print(plugged + ' ' + str(val) + '%')
