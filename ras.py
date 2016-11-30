import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)

def long_sound():
    time.sleep(.1)
    gpio.output(7,1)
    time.sleep(.5)
    gpio.output(7,0)

def short_sound():
    time.sleep(.1)
    gpio.output(7,1)
    time.sleep(.3)
    gpio.output(7,0)


def pause():
    time.sleep(.5)

def main():
    code = '-.-. --- -.. . -.-. --- --- .-.. '
    try:
        while True:
            for i in code:
                if i == '-':
                    long_sound()
                elif i == '.':
                    short_sound()
                else:
                    pause()
    except KeyboardInterrupt:
        gpio.cleanup()
        exit


if __name__ == '__main__':
    main()