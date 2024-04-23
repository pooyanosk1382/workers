import threading
import time

startTime = time.time()
store = threading.RLock()
ship = threading.RLock()
eatingWorkers = 0
t = 10


class Workers(threading.Thread):
    def __init__(self, name, speed):
        threading.Thread.__init__(self)
        self.name = name
        self.speed = speed
        self.number = 0
        self.eaten = False

    def run(self) -> None:
        currentTime = time.time()
        while currentTime - startTime < t:
            if currentTime - startTime >= t / 2 and self.eaten is False:
                self.eating()
            self.loading()
            self.put()
            currentTime = time.time()

    def eating(self):
        self.eaten = True
        print('worker ' + self.name + ' is eating.')
        time.sleep(t/16)
        return 0

    def put(self):
        store.acquire()
        print('worker ' + self.name + ' is putting.')
        store.release()
        self.number += 3
        print('worker ' + self.name + ' is backing to ship.')
        time.sleep(self.speed)
        return 0

    def loading(self):
        ship.acquire()
        print('worker ' + self.name + ' is loading.')
        ship.release()
        print('worker ' + self.name + ' is going to store.')
        time.sleep(self.speed)
        return 0


worker1 = Workers('1', 0.2)
worker2 = Workers('2', 0.1)
worker3 = Workers('3', 0.15)
worker4 = Workers('4', 0.17)
worker5 = Workers('5', 0.22)
worker6 = Workers('6', 0.09)
worker7 = Workers('7', 0.13)
worker8 = Workers('8', 0.23)

worker1.start()
worker2.start()
worker3.start()
worker4.start()
worker5.start()
worker6.start()
worker7.start()
worker8.start()

worker1.join()
worker2.join()
worker3.join()
worker4.join()
worker5.join()
worker6.join()
worker7.join()
worker8.join()