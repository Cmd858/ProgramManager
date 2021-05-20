from SigListener import SigListener
import time

listener = SigListener(port=50000)
listener.start()

while 1:
    time.sleep(1)
    print('running')