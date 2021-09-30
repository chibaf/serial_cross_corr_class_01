import numpy as np
import queue,time
import serial,sys
from cross_corr_via_serial_class import serial_cross_corr
import threading

q1=queue.Queue()
cross_corr1=serial_cross_corr()
q2=queue.Queue()
cross_corr2=serial_cross_corr()

th1 = threading.Thread(target=cross_corr1.cross_corr, args=(sys.argv[1],sys.argv[3],q1),daemon=True)
th1.start()
th2 = threading.Thread(target=cross_corr2.cross_corr, args=(sys.argv[2],sys.argv[3],q2),daemon=True)
th2.start()

i1=1;i2=1
print("start thread: "+str(i1))
while True:
  if th1.is_alive()==False:
    ix = q1.get()
    print(ix)
    i1=i1+1
    if i1>5:
      break;
    th1 = threading.Thread(target=cross_corr1.cross_corr, args=(sys.argv[1],sys.argv[3],q1),daemon=True)
    th1.start()
    print("start thread: "+str(i1))
  if th2.is_alive()==False:
    ix = q2.get()
    print(ix)
    i2=i2+1
    if i2>5:
      break;
    th2=threading.Thread(target=cross_corr2.cross_corr, args=(sys.argv[2],sys.argv[3],q2),daemon=True)
    th2.start()
    print("start thread: "+str(i2))

exit()
