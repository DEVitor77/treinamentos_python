from time import sleep

while True:
    for h in range (23, 24):
        for m in range (60):
            for s in range (60):
                print (f' {h:02}:{m:02}:{s:02}')
                #sleep(0.01)
