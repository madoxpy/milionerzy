from pygame import *
import numpy as np
from random import *
from time import sleep
from numpy import ceil,floor

green=(0,255,0)
greengrass=(1,166,17)
black=(0,0,0)
white=(255,255,255)
bluesky=(135,206,235)
red=(255,5,5)
bloodred=(138,7,7)
blue=(0,0,255)
darkblue=(0,0,139)
orange=(255,102,0)
yellow=(255,255,0)
colors = [(0,0,0),(255,0,0),(0,128,255),(255,128,0),(255,0,128),(128,255,0),(128,0,255),(0,255,0),(0,0,255)]


res=[800,640]

init()
window=display.set_mode(res)
clock = time.Clock()
Font=font.SysFont("arial",20)

photo = image.load("chairman.png")
photo=transform.scale(photo,(600,300))
photo2 = image.load("points.png")
photo2=transform.scale(photo2,(170,270))

class Button(object):
	def __init__(self,x,y,w,h,text="",ans=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",32)
		self.act=True
		self.ans=ans
		
	def event(self,game):
		if self.click() and self.act:
			draw.rect(window,orange,Rect(self.x,self.y,self.w,self.h),10)
			display.flip()
			sleep(1.5)
			if self.ans==game.ans:
				mixer.music.load('correct_answer.mp3')
				mixer.music.play(1)
				draw.rect(window,green,Rect(self.x,self.y,self.w,self.h),10)
				display.flip()
				sleep(4.5)
				game.next()
			else:
				mixer.music.load('wrong_answer.mp3')
				mixer.music.play(1)
				draw.rect(window,red,Rect(self.x,self.y,self.w,self.h),10)
				display.flip()
				sleep(3.5)
				game.lose()
		
	def click(self):
		if mouse.get_pressed()[0]:
			if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
				return True

	def draw(self):

		if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
			draw.rect(window,green,Rect(self.x,self.y,self.w,self.h),1)
		else:
			draw.rect(window,white,Rect(self.x,self.y,self.w,self.h),1)
		text = self.Font.render(self.text,True,white)
		window.blit(text,(self.x+5,self.y+5))

class gButton(Button):	
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",22)
		self.act=True
	def event(self,game):
		if self.click():
			money = ["0", "500", "1 000", "2 000","5 000", "10 000", "20 000", "40 000", "75 000", "125 000", "250 000", "500 000"]
			game.q ="Wygrales "+ money[game.num-1]
			game.b1=Button(60,450,300,50,"","A")	
			game.b2=Button(440,450,300,50,"","B")	
			game.b3=Button(60,550,300,50,"","C")	
			game.b4=Button(440,550,300,50,"","D")	
			game.ans=str("")
			game.b1.act=False
			game.b2.act=False
			game.b3.act=False
			game.b4.act=False
			self.act=False

class nButton(Button):	
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",22)
		self.act=True
	def event(self,game):
		if self.click():
			return Game()
		else:
			return game

class k50Button(Button):	
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",22)
		self.act=True
	def event(self,game):
		if self.click() and self.act:
			tab=["A","B","C","D"]
			l=choice(tab)
			while l==game.ans:
				l=choice(tab)
			p=choice(tab)
			while p==l or p==game.ans:
				p=choice(tab)
			if l=="A" or p=="A":
				game.b1.text=""
			if l=="B" or p=="B":
				game.b2.text=""
			if l=="C" or p=="C":
				game.b3.text=""
			if l=="D" or p=="D":
				game.b4.text=""
			self.act=False

class kphoneButton(Button):	
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",22)
		self.act=True
	def event(self,game):
		if self.click() and self.act :
			c=(95.-game.num*5.)/100.
			if random()<c:
				self.text = game.ans
			else:
				tab=["A","B","C","D"]
				l=choice(tab)
				self.text = l
			self.act = False
		
class kaudienceButton(Button):	
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",22)
		self.act=True
	def event(self,game):
		if self.click() and self.act:
			c=(85.-game.num*5.+randint(-5,5))
			a1 = floor((100-c)/3.+randint(-5,5))
			a2 = floor((100-c-a1)/2.+randint(-5,5))
			a3 = 100-c-a1-a2
			if game.ans=="A" or game.ans=="A":
				game.hint="A: "+str((c))+"%, "+"B: "+str((a1))+"%, "+"C: "+str((a2))+"%, "+"D: "+str((a3))+"% "
			if game.ans=="B" or game.ans=="B":
				game.hint="A: "+str((a1))+"%, "+"B: "+str((c))+"%, "+"C: "+str((a2))+"%, "+"D: "+str((a3))+"% "
			if game.ans=="C" or game.ans=="C":
				game.hint="A: "+str((a2))+"%, "+"B: "+str((a1))+"%, "+"C: "+str((c))+"%, "+"D: "+str((a3))+"% "
			if game.ans=="D" or game.ans=="D":
				game.hint="A: "+str((a3))+"%, "+"B: "+str((a1))+"%, "+"C: "+str((a2))+"%, "+"D: "+str((c))+"% "
			self.act = False
			
class Game(object):
	def __init__(self):
		
		self.num=1
		filenum = randint(1,12)
		self.file=open("q"+str(filenum)+".dat")


		self.q =str(self.num)+". "+str(self.file.readline()[0:-1])

		self.b1=Button(60,450,300,50,"A. "+str(self.file.readline()[0:-1]),"A")	
		self.b2=Button(440,450,300,50,"B. "+str(self.file.readline()[0:-1]),"B")	
		self.b3=Button(60,550,300,50,"C. "+str(self.file.readline()[0:-1]),"C")	
		self.b4=Button(440,550,300,50,"D. "+str(self.file.readline()[0:-1]),"D")	
		self.ans=str(self.file.readline()[0:-1])
		
		self.giveup=gButton(10,10,100,40,"Rezygnuj")	
		self.newgame=nButton(120,10,120,40,"Nowa Gra")	
		self.k50=k50Button(450,10,65,40,"50:50")	
		self.kphone=kphoneButton(530,10,100,40,"Telefon")	
		self.kaudience=kaudienceButton(645,10,130,40,"Publicznosc")	
		mixer.music.load('main_theme.mp3')
		mixer.music.play(0)
		self.hint = "" 

	def event(self):
		self.b1.event(self)
		self.b2.event(self)
		self.b3.event(self)
		self.b4.event(self)
		self.k50.event(self)
		self.kphone.event(self)
		self.kaudience.event(self)
		self.giveup.event(self)
	
	def next(self):
		self.hint = "" 
		self.kphone.text = "Telefon"
		if self.num!=12:
			self.num=self.num+1
			self.q =str(self.num)+". "+str(self.file.readline()[0:-1])
			self.b1=Button(60,450,300,50,"A. "+str(self.file.readline()[0:-1]),"A")	
			self.b2=Button(440,450,300,50,"B. "+str(self.file.readline()[0:-1]),"B")	
			self.b3=Button(60,550,300,50,"C. "+str(self.file.readline()[0:-1]),"C")	
			self.b4=Button(440,550,300,50,"D. "+str(self.file.readline()[0:-1]),"D")	
			self.ans=str(self.file.readline()[0:-1])
			mixer.music.load('main_theme.mp3')
			mixer.music.play(0)

		else:
			self.q ="Wygrales milion!"
			self.b1=Button(60,450,300,50,"","A")	
			self.b2=Button(440,450,300,50,"","B")	
			self.b3=Button(60,550,300,50,"","C")	
			self.b4=Button(440,550,300,50,"","D")	
			self.ans=str("")
			self.b1.act=False
			self.b2.act=False
			self.b3.act=False
			self.b4.act=False
			self.k50.act=False
			self.kphone.act=False
			self.kaudience.act=False
			
			self.giveup.act=False
		
	def lose(self):
		if self.num<=2:
			money="0"
		elif self.num>2 and self.num<=7:
			money="1 000"
		else:
			money="40 000"
		self.q ="Przegrales! Zdobyles "+money+" zl"
		self.b1=Button(60,450,300,50,"","A")	
		self.b2=Button(440,450,300,50,"","B")	
		self.b3=Button(60,550,300,50,"","C")	
		self.b4=Button(440,550,300,50,"","D")	
		self.ans=str("")
		self.b1.act=False
		self.b2.act=False
		self.b3.act=False
		self.b4.act=False
		self.k50.act=False
		self.kphone.act=False
		self.kaudience.act=False
		self.giveup.act=False

	
	def draw(self):
		window.fill(black)
		window.blit(photo,(0,20))
		window.blit(photo2,(600,50))
		self.b1.draw()
		self.b2.draw()
		self.b3.draw()
		self.b4.draw()
		self.k50.draw()
		self.kphone.draw()
		self.kaudience.draw()
		self.giveup.draw()
		self.newgame.draw()
		draw.rect(window,darkblue,Rect(50,320,700,100),1)
		text = Font.render(self.q,True,white)
		window.blit(text,(100,350))
		text = Font.render(self.hint,True,white)
		window.blit(text,(100,370))
		draw.rect(window,yellow,Rect(600,310-self.num*20,30,20),1)



game=Game()
end=False


while not end:
	
	for zet in event.get():
		if zet.type ==QUIT:
			end=True

	
	game.draw()
	game.event()
	if game.newgame.click():
		game = Game()
		sleep(1.5)
	clock.tick(20)
	display.flip()