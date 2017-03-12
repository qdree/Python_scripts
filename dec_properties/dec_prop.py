class Naming(object):
	def __init__(self, name):
		self.name = name
		self._sure_name = ""
		self.comp_name = ""
		self.full = ""

	@property
	def sure_name(self):
		return self._sure_name

	@sure_name.setter
	def sure_name(self, sure_name):
		self._sure_name = sure_name
		self.full = self.name+" "+self._sure_name


class CompNaming(Naming):
	def __init__(self, name):
		super().__init__(name)
		self._sure_name = ""

	@property
	def sure_name(self):
		return self._sure_name

	@sure_name.setter
	def sure_name(self, sure_name):
		self._sure_name = sure_name
		self.comp_name = "LLC \"{} {}\" corp.".format(self.name, self._sure_name)

naming = naming("Oleksandr")
c_naming = CompNaming("Alex")

print ("Before: ", c_naming.comp_name)
c_naming.sure_name = "Serdiuk"
print ("After: ", c_naming.comp_name)


print ("Before: ", naming.full)
naming.sure_name = "Serdiuk"
print ("After: ", naming.full)