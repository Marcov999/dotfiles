import os
cmd='cat /sys/class/backlight/intel_backlight/brightness'
bri=os.popen(cmd).read()
bri=bri[0:-1]
bri=int(int(bri)/9600)
bri=str(bri)
print(' '+bri)
