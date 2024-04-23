import tkinter as tk
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
                self.eating()
            self.loading()
            self.put()
            currentTime = time.time()

    def eating(self):
        global eatingWorkers
        eatingWorkers += 1
        self.eaten = True
        match self.name:
            case '1':
                line1.set('worker 1 is eating')
            case '2':
                line2.set('worker 2 is eating')
            case '3':
                line3.set('worker 3 is eating')
            case '4':
                line4.set('worker 4 is eating')
            case '5':
                line5.set('worker 5 is eating')
            case '6':
                line6.set('worker 6 is eating')
            case '7':
                line7.set('worker 7 is eating')
            case '8':
                line8.set('worker 8 is eating')
        print('worker ' + self.name + ' is eating.')
        print('There are ' + str(eatingWorkers) + ' workers that are eating')
        time.sleep(t/16)
        eatingWorkers -= 1

    def put(self):
        store.acquire()
        match self.name:
            case '1':
                line1.set('worker 1 is putting and backing to ship')
            case '2':
                line2.set('worker 2 is putting and backing to ship')
            case '3':
                line3.set('worker 3 is putting and backing to ship')
            case '4':
                line4.set('worker 4 is putting and backing to ship')
            case '5':
                line5.set('worker 5 is putting and backing to ship')
            case '6':
                line6.set('worker 6 is putting and backing to ship')
            case '7':
                line7.set('worker 7 is putting and backing to ship')
            case '8':
                line8.set('worker 8 is putting and backing to ship')
        print('worker ' + self.name + ' is putting.')
        store.release()
        self.number += 3
        print('worker ' + self.name + ' is backing to ship.')
        time.sleep(self.speed)

    def loading(self):
        ship.acquire()
        match self.name:
            case '1':
                line1.set('worker 1 is loading and going to store')
            case '2':
                line2.set('worker 2 is loading and going to store')
            case '3':
                line3.set('worker 3 is loading and going to store')
            case '4':
                line4.set('worker 4 is loading and going to store')
            case '5':
                line5.set('worker 5 is loading and going to store')
            case '6':
                line6.set('worker 6 is loading and going to store')
            case '7':
                line7.set('worker 7 is loading and going to store')
            case '8':
                line8.set('worker 8 is loading and going to store')
        print('worker ' + self.name + ' is loading.')
        ship.release()
        print('worker ' + self.name + ' is going to store.')
        time.sleep(self.speed)


# Create the main window
root = tk.Tk()
root.title("Real-Time GUI with Eight Lines")
root.geometry("600x400")

# Create StringVar variables for each line
line1 = tk.StringVar()
line2 = tk.StringVar()
line3 = tk.StringVar()
line4 = tk.StringVar()
line5 = tk.StringVar()
line6 = tk.StringVar()
line7 = tk.StringVar()
line8 = tk.StringVar()

# Create labels for each line with padding
label1 = tk.Label(root, textvariable=line1)
label1.pack(pady=10)  # Add vertical padding
label2 = tk.Label(root, textvariable=line2)
label2.pack(pady=10)  # Add vertical padding
label3 = tk.Label(root, textvariable=line3)
label3.pack(pady=10)  # Add vertical padding
label4 = tk.Label(root, textvariable=line4)
label4.pack(pady=10)  # Add vertical padding
label5 = tk.Label(root, textvariable=line5)
label5.pack(pady=10)  # Add vertical padding
label6 = tk.Label(root, textvariable=line6)
label6.pack(pady=10)  # Add vertical padding
label7 = tk.Label(root, textvariable=line7)
label7.pack(pady=10)  # Add vertical padding
label8 = tk.Label(root, textvariable=line8)
label8.pack(pady=10)  # Add vertical padding


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

root.mainloop()

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