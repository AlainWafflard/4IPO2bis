# Python Code for factory method
# it comes under the creational
# Design Pattern

class Translator:

	def __init__(self):
		self._translation_d = {}

	@classmethod
	def factory(cls, language="English"):
		"""Factory Method"""
		translator_l = {
			"French":  FrenchTranslator,
			"English": EnglishTranslator,
			"Spanish": SpanishTranslator,
		}
		return translator_l[language]()

	def localize(self, msg):
		"""change the message using translations"""
		return self._translation_d.get(msg, msg)


class FrenchTranslator(Translator):
	""" it simply returns the french version """
	def __init__(self):
		super().__init__()
		self._translation_d = dict(car="voiture", bike="bicyclette", scooter="trottinette")


class SpanishTranslator(Translator):
	"""it simply returns the spanish version"""
	def __init__(self):
		super().__init__()
		self._translation_d = dict(car="coche", bike="bicicleta", scooter="patineta")


class EnglishTranslator(Translator):
	"""Simply return the same message"""
	def localize(self, msg):
		return msg


if __name__ == "__main__":

	f = Translator.factory("French")
	e = Translator.factory("English")
	s = Translator.factory("Spanish")

	for msg in ["car", "bike", "scooter"]:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))

