##########SOlid Design Principle:
# Single Responsibilty prinicple:
#   A class should have only one responsibility and only one reason to change. That means a class does not perform multiple jobs

class Animal:
	def leg_count(self):
		return 'lovda mera'
class Lion:
	def leg_count(self):
		return 4
class pegion(Animal):
	pass
	# def leg_count(self):
	# 	return 2

def animal_leg_count(animals: list):
	for animal in animals:
		print(animal.leg_count())

animals=[Lion(),pegion(),Animal()]
animal_leg_count(animals)       