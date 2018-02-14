import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

L_Pin = 0
R_Pin = 1

def stopAll():
    pass

def L_RN():
    RPL.servoRead(L_Pin)
    print L_RN

def R_RN():
    RPL.servoRead(R_Pin)
    print R_RN

def L_open():
    RPL.servoWrite(0,L_RN - 10)
    print ("Left servo step open")

def L_close():
    RPL.servoWrite(0,L_RN + 10)
    print ("Left servo step close")

def R_open():
    RPL.servoWrite(1,R_RN + 10)
    print ("right servo step open")

def R_close():
    RPL.servoWrite(1,R_RN - 10)
    print ("Left servo step close")

fd = sys.stdin.fileno() # I don't know what this does
old_settings = termios.tcgetattr(fd) # this records the existing console settings that are later changed with the tty.setraw... line so that they can be replaced when the loop ends

######################################
## Other motor commands should go here
######################################

def interrupted(signum, frame):
    stopAll()

signal.signal(signal.SIGALRM, interrupted) # this calls the 'interrupted' method when the alarm goes off
tty.setraw(sys.stdin.fileno()) # this sets the style of the input

print "Ready To Drive! Press * to quit.\r"
## the SHORT_TIMEOUT needs to be greater than the press delay on your keyboard
## on your computer, set the delay to 250 ms with `xset r rate 250 20`
SHORT_TIMEOUT = 0.255 # number of seconds your want for timeout
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
      print "left closed"
    elif ch == "a":
      L_open
      print "left opened"
    elif ch == "s":
      R_close
      print "right close"
    elif ch == "d":
      R_open
      print "right opened"
    else:
      stopAll()
