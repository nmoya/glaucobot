# -*- coding: utf-8-*-
import pkgutil
import os
import sys


class Brain(object):

	def __init__(self):
		self.modules = self.get_modules(os.path.join(os.getcwd(),
													 "glaucobot/modules/"))

	@classmethod
	def get_modules(self, path):
		"""
		Dynamically loads all the modules in the modules folder and sorts
		them by the PRIORITY key. If no PRIORITY is defined for a given
		module, a priority of 0 is assumed.
		"""
		modules = []
		for finder, name, ispkg in pkgutil.walk_packages([path]):
			try:
				loader = finder.find_module(name)
				mod = loader.load_module(name)
			except:
				print "Skipped module '%s' due to an error." %(name)
			else:
				if hasattr(mod, 'WORDS'):
					modules.append(mod)
				else:
					print "Skipped module %s because it misses the \
						WORDS constant." % (name)
		modules.sort(key=lambda mod: mod.PRIORITY if hasattr(mod, 'PRIORITY')
					 else 0, reverse=True)
		return modules

	def query(self, text):
		"""
		Passes user input to the appropriate module, testing it against
		each candidate module's isValid function.
		"""
		response = None
		for module in self.modules:
			if module.isValid(text):
				try:
					response = module.handle(text)
				except:
					response = "[!] Error on module %s with the given arguments" % (module.__name__)
				finally:
					return response



if __name__ == "__main__":
	b = Brain()







