import numpy as np
import queue,time
import serial,sys
from cross_corr_via_serial_class import serial_cross_corr

q =queue.Queue()
cross_corr=serial_cross_corr()
for i in range(4):
  cross_corr.cross_corr(sys.argv[1],sys.argv[2],q)
  ix = q.get()
  print(ix)
exit()