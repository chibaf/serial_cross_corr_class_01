import numpy as np
import queue,time
import serial,sys
from cross_corr_via_serial_class import serial_cross_corr
import threading

q =queue.Queue()
cross_corr=serial_cross_corr()

th = threading.Thread(target=cross_corr.cross_corr, args=(sys.argv[1],sys.argv[2],q),daemon=True)
th.start()

i=1
print("start thread: "+str(i))
while True:
  if th.is_alive()==False:
    ix = q.get()
    print(ix)
    i=i+1
    if i>5:
      break;
    th = threading.Thread(target=cross_corr.cross_corr, args=(sys.argv[1],sys.argv[2],q),daemon=True)
    th.start()
    print("start thread: "+str(i))
  else:
    time.sleep(2)

exit()
