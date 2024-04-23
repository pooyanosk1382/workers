import tkinter as tk
from tkinter import PhotoImage
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
        match self.name:
            case '1':
                line1.set('number of boxes of worker 1 is ' + str(self.number))
            case '2':
                line2.set('number of boxes of worker 2 is ' + str(self.number))
            case '3':
                line3.set('number of boxes of worker 3 is ' + str(self.number))
            case '4':
                line4.set('number of boxes of worker 4 is ' + str(self.number))
            case '5':
                line5.set('number of boxes of worker 5 is ' + str(self.number))
            case '6':
                line6.set('number of boxes of worker 6 is ' + str(self.number))
            case '7':
                line7.set('number of boxes of worker 7 is ' + str(self.number))
            case '8':
                line8.set('number of boxes of worker 8 is ' + str(self.number))

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
        time.sleep(t/16)
        eatingWorkers -= 1

    def put(self):
        store.acquire()
        match self.name:
            case '1':
                line1.set('worker 1 is delivered and backing to ship')
            case '2':
                line2.set('worker 2 is delivered and backing to ship')
            case '3':
                line3.set('worker 3 is delivered and backing to ship')
            case '4':
                line4.set('worker 4 is delivered and backing to ship')
            case '5':
                line5.set('worker 5 is delivered and backing to ship')
            case '6':
                line6.set('worker 6 is delivered and backing to ship')
            case '7':
                line7.set('worker 7 is delivered and backing to ship')
            case '8':
                line8.set('worker 8 is delivered and backing to ship')
        store.release()
        self.number += 3
        time.sleep(self.speed)

    def loading(self):
        ship.acquire()
        match self.name:
            case '1':
                line1.set('worker 1 is loaded and going to store')
            case '2':
                line2.set('worker 2 is loaded and going to store')
            case '3':
                line3.set('worker 3 is loaded and going to store')
            case '4':
                line4.set('worker 4 is loaded and going to store')
            case '5':
                line5.set('worker 5 is loaded and going to store')
            case '6':
                line6.set('worker 6 is loaded and going to store')
            case '7':
                line7.set('worker 7 is loaded and going to store')
            case '8':
                line8.set('worker 8 is loaded and going to store')
        ship.release()
        time.sleep(self.speed)


root = tk.Tk()
root.title("Workers situation")
root.geometry("800x800")

# Create StringVar variables for each line
line1 = tk.StringVar()
line2 = tk.StringVar()
line3 = tk.StringVar()
line4 = tk.StringVar()
line5 = tk.StringVar()
line6 = tk.StringVar()
line7 = tk.StringVar()
line8 = tk.StringVar()

image1 = PhotoImage(file="worker1.png").subsample(40, 40)
image2 = PhotoImage(file="worker2.png").subsample(40, 40)
image3 = PhotoImage(file="worker3.png").subsample(40, 40)
image4 = PhotoImage(file="worker4.png").subsample(40, 40)
image5 = PhotoImage(file="worker5.png").subsample(40, 40)
image6 = PhotoImage(file="worker6.png").subsample(40, 40)
image7 = PhotoImage(file="worker7.png").subsample(40, 40)
image8 = PhotoImage(file="worker8.png").subsample(40, 40)

# Create labels for each line with padding
label1 = tk.Label(root, image=image1, textvariable=line1, font=("Arial", 14), compound="left")
label1.pack(pady=10)  # Add vertical padding
label2 = tk.Label(root, image=image2, textvariable=line2, font=("Arial", 14), compound="left")
label2.pack(pady=10)  # Add vertical padding
label3 = tk.Label(root, image=image3, textvariable=line3, font=("Arial", 14), compound="left")
label3.pack(pady=10)  # Add vertical padding
label4 = tk.Label(root, image=image4, textvariable=line4, font=("Arial", 14), compound="left")
label4.pack(pady=10)  # Add vertical padding
label5 = tk.Label(root, image=image5, textvariable=line5, font=("Arial", 14), compound="left")
label5.pack(pady=10)  # Add vertical padding
label6 = tk.Label(root, image=image6, textvariable=line6, font=("Arial", 14), compound="left")
label6.pack(pady=10)  # Add vertical padding
label7 = tk.Label(root, image=image7, textvariable=line7, font=("Arial", 14), compound="left")
label7.pack(pady=10)  # Add vertical padding
label8 = tk.Label(root, image=image8, textvariable=line8, font=("Arial", 14), compound="left")
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