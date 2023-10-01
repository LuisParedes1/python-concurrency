# By default, Python does not provide abstract classes.

# Python comes with a module that provides the base for defining Abstract Base classes(ABC)
# and that module name is ABC. ABC works by decorating methods of the base class as an abstract 
# and then registering concrete classes as implementations of the abstract base.

# A method becomes abstract when decorated with the keyword @abstractmethod

# https://www.geeksforgeeks.org/abstract-classes-in-python/

# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass


class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")


class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")


class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")


class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

# No se puede instanciar una clase abstracta
# p = Polygon()