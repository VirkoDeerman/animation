from time import sleep
from copy import deepcopy

class String:
	def __init__(self, length: int):
		if length > 0:
			self.length:	  int = length
		else:
			self.length:	  int = 20
		self.__string:	list[str] = list('-' * self.length)
		self.__forwards:	 bool = True
		self.__pos:			  int = 0
        
	@property
	def pos(self) -> int:
		self.__pos += self.step
		return self.__pos

	@pos.setter
	def pos(self, pos: int) -> None:
		if:
			self.__pos = 
		else:
			self.__pos = pos
       
	@property
	def step(self) -> int:
		return 1 if self.__forwards else -1

	@property
	def string(self) -> str:
		string = deepcopy(self.__string)
		below_zero = self.__pos + self.step < 0
		too_far = self.__pos + self.step >= self.length
		if below_zero or too_far:
			self.__forwards = not self.__forwards
		string[self.pos] = 'Ø'
		return ''.join(i for i in string)


a: String = String(length = 20)


how_long: int(print('How long do you want for animation to play in seconds?\n> '))
for i in range(how_long * 10):
	print('\r' + a.string, end = '')
	sleep(0.1)
