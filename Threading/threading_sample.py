import threading as th
import time

class Alphabets(th.Thread):
    def run(self):
        for i in range(65,91):
            print(chr(i))
            time.sleep(1)
        
t=Alphabets()
t.start()

for i in range(65,91):
    print(i)
    time.sleep(1)
    
t.join()