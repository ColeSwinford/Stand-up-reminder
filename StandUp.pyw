from win10toast import *
import time

toaster = ToastNotifier()

# time in seconds between notifications (default = 20min = 1200.0)
interval = 1200.0

startTime = time.time()
while True:
    toaster.show_toast("Stand up", "Look at something 20 feet away for 20 seconds", duration = 5)
    time.sleep(interval - ((time.time()-startTime)%interval))