class Configuration:
	def __init__(self, env):
		self.env = env
		self.__dict = {"currency": "USD"}

	def load(self):
		pass

	def get_value(self, key):
		return self.__dict[key]

