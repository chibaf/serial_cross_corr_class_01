# serial_cross_corr_class_01
class of computing cross-correlation from arduino serial

cross_corr_via_serial_class.py: class reading serial from arduino and compute cross-correlation

find_index.py: find index of maximum element in cross_corr_via_serial_class.py

cross_corr_via_serial_main.py: call cross_corr_via_serial_class.py

cross_corr_via_serial_thread.py: use cross_corr_via_serial_class.py as thread

usage: python3 cross_corr_via_serial_main.py  "/dev/tty.usbmodem146301" 19200

usage: python3 cross_corr_via_serial_thread.py "/dev/tty.usbmodem146301" 19200

logger_simulator_01.ino, logger_simulator_02.ino: signal generators on arduino
