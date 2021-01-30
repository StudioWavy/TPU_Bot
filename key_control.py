#import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

#curses window, turn off echoing
#instant key respone
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
#13 --> GPIO27
#15 --> GPIO22
#16 --> GPIO23
#18 --> GPIO24
try:
    while True:
        char = screen.getch()
        if char == ord("q"):
            break
        elif char == curses.KEY_UP:
            print ("up")
            GPIO.output(13,True)
            GPIO.output(15,False)
            GPIO.output(16,False)
            GPIO.output(18,True)
        elif char == curses.KEY_DOWN:
            print ("down")
            GPIO.output(13,False)
            GPIO.output(15,True)
            GPIO.output(16,True)
            GPIO.output(18,False)
        elif char == curses.KEY_RIGHT:
            print ("right")
            GPIO.output(13,True)
            GPIO.output(15,False)
            GPIO.output(16,True)
            GPIO.output(18,False)
        elif char == curses.KEY_LEFT:
            print ("left")
            GPIO.output(13,False)
            GPIO.output(15,True)
            GPIO.output(16,False)
            GPIO.output(18,True)
        elif char == 10:
            print ("stop")
            GPIO.output(13,False)
            GPIO.output(15,False)
            GPIO.output(16,False)
            GPIO.output(18,False)

finally:
    #closes down curses, and turns echo back on
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()

