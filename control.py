import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

L_Pin = 0
R_Pin = 1

# Maximum Range
R_min = 2500
R_max = 1940
L_min = 500
L_max = 950

# Motor RN
def L_RN():
    RPL.servoRead(L_Pin)

def R_RN():
    RPL.servoRead(R_Pin)

# L and R open and close
def L_open():
  RPL.servoWrite(L_Pin,L_RN - 10)
  print ("Left servo step open")

def L_close():
  RPL.servoWrite(L_Pin,L_RN + 10)
  print ("Left servo step close")
def R_open():
  RPL.servoWrite(R_Pin,R_RN + 10)
import pdb; pdb.set_trace()
print ("right servo step open")
def R_close():
  RPL.servoWrite(R_Pin,R_RN - 10)
  print ("Left servo step close")

# inputs
while True:
  signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT) # this sets the alarm
  ch = sys.stdin.read(1) # this reads one character of input without requiring an enter keypress
  signal.setitimer(signal.ITIMER_REAL,0) # this turns off the alarm
  if ch == '*': # pressing the asterisk key kills the process
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # this resets the console settings
    break # this ends the loop
else:
    if ch == 'w':
      L_close
    elif ch == "a":
      L_open
    elif ch == "s":
      R_open
    elif ch == "d":
      R_close
    else:
      stopAll()
