#! /usr/bin/python3

"""
	This is a utility for converting english characters to their equivalent urdu characters as defined by the CRULP Urdu Keyboard Layout v1.1 (and vice versa).
"""

import click


class Translate:
	
	# Define the map between english and urdu characters (the latter defined using their Unicode code-points)
	# The Urdu characters are easily identifiable as their unicode point starts with 06 i.e. \u06XX

	e2u = {
		# Lower-case mappings
		'1': u'\u06f1',
		'2': u'\u06f2',
		'3': u'\u06f3',
		'4': u'\u06f4',
		'5': u'\u06f5',
		'6': u'\u06f6',
		'7': u'\u06f7',
		'8': u'\u06f8',
		'9': u'\u06f9',
		'0': u'\u06f0',
		'q': u'\u0642',
		'a': u'\u0627',
		'z': u'\u0632',
		'w': u'\u0648',
		's': u'\u0633',
		'x': u'\u0634',
		'e': u'\u0639',
		'd': u'\u062f',
		'c': u'\u0686',
		'r': u'\u0631',
		'f': u'\u0641',
		'v': u'\u0637',
		't': u'\u062a',
		'g': u'\u06af',
		'b': u'\u0628',
		'y': u'\u06d2',
		'h': u'\u062d',
		'n': u'\u0646',
		'u': u'\u0621',
		'j': u'\u062c',
		'm': u'\u0645',
		'i': u'\u06cc',
		'k': u'\u06a9',
		',': u'\u060c',
		'o': u'\u06c1',
		'l': u'\u0644',
		'.': u'\u06d4',
		'p': u'\u067e',
		';': u'\u061b',

		# Upper-case (Shift-ed) mapping
		'~': u'\u064b',
		'Q': u'\u0652',
		'A': u'\u0622',
		'Z': u'\u0630',
		'W': u'\u0651',
		'S': u'\u0635',
		'X': u'\u0698',
		'E': u'\u0670',
		'D': u'\u0688',
		'C': u'\u062b',
		'R': u'\u0691',
		'V': u'\u0638',
		'T': u'\u0679',
		'G': u'\u063a',
		'Y': u'\u064e',
		'H': u'\u06be',
		'N': u'\u06ba',
		'U': u'\u0626',
		'J': u'\u0636',
		'M': u'\u0658',
		'I': u'\u0650',
		'K': u'\u062e',
		'O': u'\u06c3',
		'>': u'\u066b',
		'P': u'\u064f',
		'?': u'\u061f',
	}


	def __init__(self, fin):

		# Reverse the e2u mapping to create the u2e mapping
		self.u2e = {}

		for k in self.e2u:
			self.u2e[ self.e2u[k] ] = k

		# Create list of mapped characters in both languages
		self.en = [k for k in self.e2u]
		self.ur = [k for k in self.u2e]

		# Retrieve the text from the input file and remove extraneous '\n' from the end of each line
		self.lines = [x.rstrip() for x in fin.readlines()]


	def mu2e(self, char):
		"""
		Convert the urdu character to english. A non-urdu character is preserved.
		"""
		
		try:
			return self.u2e[char]
		
		except KeyError:
			return char


	def me2u(self, char):
		"""
		Convert the english character to urdu. A non-english character is preserved.
		"""

		try:
			return self.e2u[char]

		except KeyError:
			return char

	
	def convert(self, converter):
		"""
		Convert characters in lines using the function provided in 'converter'
		"""

		for line in self.lines:

			s = ""

			for c in line:
				s += converter(c)

			print(s)


	def urdu_to_english(self):
		"""
		Convert urdu characters to english.
		"""

		self.convert(self.mu2e)


	def english_to_urdu(self):
		"""
		Convert ALL english characters to urdu.
		"""

		self.convert(self.me2u)


# We use click to access the arguments, commands and flags

@click.command()			# Essential to get click working
@click.argument('file')		# Declare a mandatory argument which will be the input file
@click.option('--urdu-to-english', '-u', is_flag=True, help="Convert all Urdu characters to English")		# Optional Flag which decides if we are translating from urdu to english
@click.option('--english-to-urdu', '-e', is_flag=True, help="Convert all English characters to Urdu")
@click.option('--latex', '-l', is_flag=True, help="Convert Urdu characters in LaTeX file to English while preserving LaTeX commands and text wrapped in \en{}")
def main(file, **kwargs):

	with open(file) as fin:

		t = Translate(fin)

		if kwargs['urdu_to_english']:			# The options passed are stored in the 'kwargs' dictionary received by this function ('main')
			t.urdu_to_english()

		elif kwargs['english_to_urdu']:
			t.english_to_urdu()


if __name__ == '__main__':
	
	main()
