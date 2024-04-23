import tkinter as tk

# Function to update the lines
def update_lines():
    # Simulating backend events
    # You can replace this with your actual backend event handling logic
    # For demonstration purposes, I'm just updating the lines with dummy data
    line1.set(f"Line 1: Event 1 occurred")
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
root.mainloop()