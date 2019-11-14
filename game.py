import pygame
pygame.init()
scLength = 800
scWidth = 800
win = pygame.display.set_mode((scLength,scWidth))

#class for paddle
class paddle(object):

	def __init__(self, x, y, length, width):
		self.x = x
		self.y = y
		self.length = length
		self.width = width

	def draw(self,win):
		pygame.draw.rect(win,(255,255,255),(self.x,self.y,self.length,self.width),9)

#as the name suggests
def redrawGameWindow():
	P1.draw(win)
	#P2.draw(win)
	pygame.display.update()

#main-loop
P1 = paddle(scLength-50,(scWidth-100)//2,10,100)
#P2 = paddle(40,(scWidth-100)//2,10,100)
run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	redrawGameWindow()

pygame.quit()