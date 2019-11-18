import pygame
pygame.init()

scLength = 1000
scWidth = 800

win = pygame.display.set_mode((scLength,scWidth))
pygame.display.set_caption('Pong-Game')

pad = pygame.image.load('paddle.png')

clock = pygame.time.Clock()

#class for paddle
class paddle(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.vel = 50

	#display the paddle on screen
	def draw(self,win,t1,t2):
		self.move(t1,t2)
		win.blit(pad,(self.x,self.y))

	#respnsible for movement of paddle
	def move(self,type1,type2):
		keys = pygame.key.get_pressed()

		if keys[type1] and self.y - self.vel >= 0:
			self.y -= self.vel
		elif keys[type2] and self.y + self.vel + 100 < 800:
			self.y += self.vel 

#ball class
class ball(object):
	def __init__(self,x,y,win):
		self.x = x
		self.y = y
		self.vel = 30
		self.xm = self.vel
		self.ym = -self.vel
		self.win = win

	def draw(self):
		self.move()
		pygame.draw.circle(win,(255,255,255),(self.x,self.y),12,12)

	def move(self):
		self.x = self.x + self.xm
		self.y = self.y + self.ym
		if self.y <= 0:
			self.ym = +self.vel
		if self.y >= scWidth:
			self.ym = -self.vel

#as the name suggests
def redrawGameWindow():
	win.fill((0,0,0))
	P1.draw(win,pygame.K_UP,pygame.K_DOWN)
	P2.draw(win,pygame.K_w,pygame.K_s)
	B.draw()
	pygame.display.update()

#main-loop
P1 = paddle(scLength-50,(scWidth-180)//2)
P2 = paddle(30,(scWidth-180)//2)
B = ball(30,scWidth//2,win)

run = True
while run:
	clock.tick(30)

	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	redrawGameWindow()

pygame.quit()