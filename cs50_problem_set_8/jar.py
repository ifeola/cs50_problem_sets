class Jar:
	def __init__(self, capacity=12):
		if type(capacity) != int or capacity <= 0:
			raise ValueError()
		self.size = 0
		self.capacity = capacity

	def __str__(self):
		return f"🍪" * self.size

	def deposit(self, n):
		self.size = n + self.size
		if self.size > self.capacity:
			raise ValueError()
		return self.size

	def withdraw(self, n):
		self.size = self.size - n
		if self.size < 0:
			raise ValueError()

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, size):
		self._size = size

	@property
	def capacity(self):
		return self._capacity

	@capacity.setter
	def capacity(self, capacity):
		if type(capacity) != int or capacity < 0:
			raise ValueError()
		self._capacity = capacity



def main():
  numb = int(input("Enter number of cookies to add: "))
  cookies = Jar(numb)
  print(cookies)


if __name__ == "__main__":
  main()
