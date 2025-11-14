from time import sleep
from copy import deepcopy

class String:
	def __init__(self, length: int = 20):
		self.__string:	 list[str] = list('-' * self.__length)
		self.__forwards: 	  bool = True
		self.__pos:			   int = 0
		if length > 5:
			self.__length:	   int = length
		else:
			self.__length:	   int = 5
        
	@property
	def pos(self) -> int:
		self.__pos += self.step
		return self.__pos

	@pos.setter
	def pos(self, pos: int) -> None:
		if self.__pos < 0:
			self.__pos = 0
		elif self.__pos >= self.__length:
			self.__pos = self.__length - 1
		else:
			self.__pos = pos
       
	@property
	def step(self) -> int:
		return 1 if self.__forwards else -1

	@property
	def string(self) -> str:
		string = deepcopy(self.__string)
		below_zero = self.__pos + self.step < 0
		too_far = self.__pos + self.step >= self.__length
		if below_zero or too_far:
			self.__forwards = not self.__forwards
		string[self.pos] = 'O'
		return ''.join(i for i in string)


a: String = String()


how_long: int(print('How long do you want for animation to play in seconds?\n> '))
print()
for i in range(how_long * 10):
	print('\r' + a.string, end = '')
	sleep(0.1)
