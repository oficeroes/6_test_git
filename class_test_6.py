class Box():
	def __init__(self,length1,width1,height1):
		self.length1=length1
		self.width1=width1
		self.height1=height1
	def volume(self):
		return self.length1 * self.width1 * self.height1
my_box=Box(10,20,30)
print("长方体体积是%.2f"%my_box.volume())