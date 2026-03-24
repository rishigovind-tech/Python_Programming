import threading as th

def display():
    for i in range(65,91):
        print(chr(i))
        
t=th.Thread(target=display,name='Alphabets')
t.start()
for i in range(65,91):
    print(i)
t.join