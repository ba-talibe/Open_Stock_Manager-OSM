from pygame import mixer

from gpiozero import Buzzer

mixer.init()
mixer.music.load('beep.mp3')
buzzer = Buzzer(4)


def play(time=3):
    for i in range(time):
        mixer.music.play()
        sleep(0.7)

def playBuzzur(time=2):
	buzzer.on()
	sleep(time)
	buzzer.off()

