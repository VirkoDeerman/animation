from time import sleep
from copy import deepcopy

class String:
	def __init__(self, pos: int):
		self.__len:			  int = 20
		self.__string:	list[str] = list('-' * self.__len)
		self.forwards:		 bool = True
		self.__pos:			  int = pos
        
	@property
	def pos(self) -> int:
		self.__pos += self.step
		return self.__pos

	@pos.setter
	def pos(self, pos) -> None:
		self.__pos = pos
       
	@property
	def step(self) -> int:
		return 1 if self.forwards else -1

	@property
	def string(self) -> str:
		string = deepcopy(self.__string)
		below_zero = self.__pos + self.step < 0
		too_far = self.__pos + self.step >= self.__len
		if below_zero or too_far:
			self.forwards = not self.forwards
		string[self.pos] = 'Ø'
		return ''.join(i for i in string)


a: String = String(pos = 0)


for i in range(50):
	print('\r' + a.string, end = '')
	sleep(0.1)
