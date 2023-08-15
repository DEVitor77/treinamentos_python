from time import sleep

for m in range (60):
    for s in range (60):
        print (f' 00:{m:02}:{s:02}')
        sleep(0.01)
