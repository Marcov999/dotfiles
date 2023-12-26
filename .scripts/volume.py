from time import sleep
import os


cmd = 'amixer -D pulse sget Master | grep \'Right:\' | awk -F\'[][]\' \'{ print $2 }\''
vol = os.popen(cmd).read()
vol = int(vol[0:-2])
if vol > 50:
    icon = ''
elif vol > 0:
    icon = ''
else:
    icon = ''
cmd = 'amixer -c0 | grep -A 5 \'Headphone\''
cmdu = 'amixer -D pulse sget Master | grep \'Right:\''
sleep(0.3)
info = os.popen(cmd).read()
infou = os.popen(cmdu).read()
mute = infou[-4:-2]
cuffie = info[-4:-2]
if cuffie == 'on':
    if mute == 'on':
        print('  ' + icon + ' ' + str(vol))
    else:
        print('  ')
else:
    if mute == 'on':
        print(icon + ' ' + str(vol))
    else:
        print('')
