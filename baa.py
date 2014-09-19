class Baa():

	BAA = ["b", "a", "a"]
	BIG = ["b", "i", "g"]

	def __init__(self):
		
		dir_self = dir(self)
		print dir_self

		dir_self = filter(lambda att: not att.startswith('_'), dir_self)
		print dir_self

		dir_self = filter(lambda att: att.isupper(),dir_self)
		print dir_self

b = Baa()