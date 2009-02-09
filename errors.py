class TestFailedError(Exception):
	pass
	
class LanguageParseError(Exception):
	def __init__(self, culture, error_message = "The language file for the specified culture could not be parsed!"):
		self.culture = culture
		self.error_message = error_message
	
	def __str__(self):
		return "Language file for %s - %s" % (self.culture, self.error_message)