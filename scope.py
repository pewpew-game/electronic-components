import pew
import analogio
import board

adc = analogio.AnalogIn(board.P5)

pew.init()
screen = pew.Pix()

while pew.keys():
	pew.tick(0.1)

while True:
	screen.blit(screen, 0, 0, 1, 0, 7, 8)
	screen.box(0, 7, 0, 1, 8)
	screen.pixel(7, 7 - (adc.value >> 13), 3)
	pew.show(screen)
	if pew.keys():
		break
	pew.tick(0.1)

adc.deinit()
