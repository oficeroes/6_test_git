class Gun():
	def __init__(self,model):
		self.model = model
		self.bullet_count = 0

	def add_bullet(self,count):
		self.bullet_count += count

	def shoot(self):
		if self.bullet_count <= 0:
			print('%s没有子弹' %(self.model))
		else:
			self.bullet_count -= 1
			print('%s的子弹数量为%s' %(self.model,self.bullet_count))
class Soldier():
	def __init__(self,name):
		self.name =name
		self.gun = None
	def fire(self):
		if self.gun == None:
			print('%s没有枪' %(self.name))
		else:
			self.gun.add_bullet(5)
			self.gun.shoot()
ak47 = Gun('AK47')
ak47.add_bullet(10)
ak47.shoot()
ruien = Soldier('RE')
ruien.gun = ak47
ruien.fire()