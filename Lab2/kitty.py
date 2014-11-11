class Animal():
	def __init__(self,name,age):
		self.age=age
		self.name=name

	#def sleep(self): 
	#	print self.name + " of " + str(self.age) + " is sleeping."
	def eat(self,food): 
		print self.name + " of " + str(self.age) + " is eating "+ food

kitty=Animal("Peuit",5.5)

#kitty.sleep()
kitty.eat("pineapple")

class bird(Animal):

	def __init__(self,name,age,wings_color):
		Animal.__init__(self,name,age)	
		self.wings_color=wings_color

	def fly(self):
		print self.name +", who is " + str(self.age) + ", and has " + self.wings_color + " wings, is flying."

birdy=bird("Nicki",3,"blue")

birdy.fly()
