import threading

class abhimessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
x = abhimessenger(name = 'send out messages')
y = abhimessenger(name = 'recieve messages')

x.start()
y.start()
