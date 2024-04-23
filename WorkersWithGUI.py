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
        line1.set(f"Line 1: Event 1 occurred")
        print('worker ' + self.name + ' is eating.')
        print('There are ' + str(eatingWorkers) + ' workers that are eating')
        time.sleep(t/16)
        eatingWorkers -= 1

    def put(self):
        store.acquire()
        print('worker ' + self.name + ' is putting.')
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


# Function to update the lines
def update_lines():
    # Simulating backend events
    # You can replace this with your actual backend event handling logic
    # For demonstration purposes, I'm just updating the lines with dummy data
    line2.set(f"Line 2: Event 2 occurred")
    line3.set(f"Line 3: Event 3 occurred")
    line4.set(f"Line 4: Event 4 occurred")
    line5.set(f"Line 5: Event 5 occurred")
    line6.set(f"Line 6: Event 6 occurred")
    line7.set(f"Line 7: Event 7 occurred")
    line8.set(f"Line 8: Event 8 occurred")
    # Schedule the update after 1000ms (1 second)
    root.after(1000, update_lines)

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

# Start the update loop
update_lines()

# Run the main loop


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