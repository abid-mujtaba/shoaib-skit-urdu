#! /usr/bin/python3

"""
	This is a utility for converting english characters to their equivalent urdu characters as defined by the CRULP Urdu Keyboard Layout v1.1 (and vice versa).
"""

import click
import re


START = re.compile(r".*startUrdu.*", re.IGNORECASE)
BEGINPARA = re.compile(r"^\\begin{enpara}")
ENDPARA = re.compile(r"^\\end{enpara}")


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


	def convert_string(self, converter, string):
		"""
		Convert the specified 'string' using the 'converter' and return it.
		"""

		s = ""

		for c in string:
			s += converter(c)

		return s

	
	def convert(self, converter):
		"""
		Convert characters in lines using the function provided in 'converter'
		"""

		for line in self.lines:

			print(self.convert_string(converter, line))


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


	def latex(self):
		"""
		Convert urdu characters to english in a LaTeX file while preserving LaTeX commands and any text wrapped in \en{}.
		"""

		fEnPara = False

		# We start by ignoring all the lines before \startUrdu (or '% startUrdu')
		count = 0

		for line in self.lines:

			count += 1
			print(line)

			if START.match(line):
				break

		for i in range(count, len(self.lines)):
			
			line = self.lines[i]

			if fEnPara:			# If we are in the middle of an 'enpara' environment we should not translate
				
				print(line)

				if ENDPARA.match(line):

					fEnPara = False

			else:

				if BEGINPARA.match(line):			# 'enpara' environment is beginning

					fEnPara = True
					print(line)

				else:			# We are NOT in the 'enpara' environment

					i = 0
					s = ''		# Substrings
					os = ''		# Final translation of whole line to be printed

					while i < len(line):		# Iterate over all chracters
						
						c = line[i]

						if c in ['\\', '{']:		# A macro has begun

							if line[i + 1] == "\\":		# Double slash at end of line, just render it as is,
								os += "\\"
								i += 2
								continue

							END = " "		# We expect a \ started macro to end with a space (if it has NO arguments)

							os += self.convert_string(self.me2u, s)		# Dump the substring collected so far (translated) before we handle the macro
							s = ''										# Substring for macro itself

							while c != END:			# Loop until the macro ends

								if c == '{':		# If the macro contains an argument in { } we have to stop at '}' rather than a space
									END = '}'

								s += c
								i += 1
								c = line[i]

							i += 1
							os += s + c
							s = ''
							continue

						s += c		# No macro detected so we keep appending characters to 's'
						i += 1

					os += self.convert_string(self.me2u, s)			# Append the translated final substring to 'os' for printing in one go

					print(os)

					
							




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

		elif kwargs['latex']:
			t.latex()

		else:
			print("Missing conversion flag. See --help.")


if __name__ == '__main__':
	
	main()
