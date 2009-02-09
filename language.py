from errors import *
import codecs
import os

class language:
	def __init__(self):
		self.__clear()
		
	def __clear(self):
		self.language_items = {}
		
	def load(self, culture):
		self.__clear()
		file_name = "language_" + culture + ".txt"
		languages_path = os.path.join(os.path.abspath(os.curdir), "languages")
		file_path = os.path.join(languages_path, file_name)
		
		try:
			fsock = open(file_path)
			lines = [line.strip() for line in fsock.readlines() if line.strip() != ""]
			fsock.close()
		except ValueError:
			raise LanguageParseError(culture)
		
		for line in lines:
			if not line.startswith("#"):
				key, value = line.split("=")			
				self.language_items[key.strip()] = value.strip()
	
	def __getitem__(self, key): 
		if self.language_items.has_key(key):
			return self.language_items[key]
		return None
	
if __name__ == "__main__":
	lang = language()
	lang.load("pt-br")
	print lang.language_items
	print lang["default_pattern"]