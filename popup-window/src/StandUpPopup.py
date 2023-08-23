import tkinter as tk
import time
import pyautogui

# get resolution
x, y = pyautogui.size()

# calculate window size
windX = int(x*0.15625) # based on 300 = 1920x --> x = 300/1920 --> x = 0.15625 * target X-resolution
windY = int(y*0.125) # based on 150 = 1200 --> y = 150/1200 --> y = 0.125 * target Y-resolution

# calculate center
centX = int((x/2)-(windX/2))
centY = int((y/3)-(windY/2))

# popup function
def popup():
    # Create a window
    window = tk.Tk()
    window.overrideredirect(1)    
    window.wm_attributes("-topmost", True)
    window.config(bg="#111111")

    # set window dimensions and location
    window.geometry("{}x{}+{}+{}".format(windX, windY, centX, centY))

    # label
    label = tk.Label(text="Stand up")
    label.config(bg="#111111", fg="#FFFFFF", font=("Arial", 18, "bold"))
    label1 = tk.Label(text="Look at something 20 feet away for 20 seconds")
    label1.config(bg="#111111", fg="#FFFFFF", font=("Arial", 12), wraplength=200)

    # button
    button = tk.Button(text="Done", command=window.destroy)
    button.config(width=15, height=2)

    # Place the label and button in the window
    label.pack(side='top', pady=5)
    label1.pack(side='top', pady=0)
    button.pack(side='bottom', pady=10)

    # Show the window
    window.mainloop()

# time in seconds between notifications (default = 20min = 1200.0)
interval = 1200.0
startTime = time.time()
while True:
    popup()
    time.sleep(interval - ((time.time()-startTime)%interval))
