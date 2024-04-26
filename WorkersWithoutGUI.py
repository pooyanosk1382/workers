import threading
import time

startTime = time.time()
store = threading.RLock()
ship = threading.RLock()
eatingWorkers = 0
t = 60


class Workers(threading.Thread):
    def __init__(self, name, speed):
        threading.Thread.__init__(self)
        self.name = name
        self.speed = speed
        self.number = 0
        self.eaten = False

    def run(self) -> None:
        global eatingWorkers
        currentTime = time.time()
        while currentTime - startTime < t + t/16:
            if currentTime - startTime >= t / 2 and self.eaten is False and eatingWorkers < 4:
                eatingWorkers += 1
                self.eating()
            self.loading()
            self.put()
            currentTime = time.time()

    def eating(self):
        global eatingWorkers
        self.eaten = True
        print('worker ' + self.name + ' is eating.')
        print('There are ' + str(eatingWorkers) + ' workers that are eating')
        time.sleep(t/16)
        eatingWorkers -= 1

    def put(self):
        store.acquire()
        print('worker ' + self.name + ' is delivering.')
        store.release()
        self.number += 3
        print('worker ' + self.name + ' is backing to ship.')
        time.sleep(self.speed)

    def loading(self):
        ship.acquire()
        print('worker ' + self.name + ' is loading.')
        ship.release()
        print('worker ' + self.name + ' is going to store.')
        time.sleep(self.speed)


worker1 = Workers('1', 5)
worker2 = Workers('2', 7)
worker3 = Workers('3', 9)
worker4 = Workers('4', 6)
worker5 = Workers('5', 6.5)
worker6 = Workers('6', 4.75)
worker7 = Workers('7', 8)
worker8 = Workers('8', 6)

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

print(worker1.number)
print(worker2.number)
print(worker3.number)
print(worker4.number)
print(worker5.number)
print(worker6.number)
print(worker7.number)
print(worker8.number)