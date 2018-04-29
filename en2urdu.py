#! /usr/bin/python3

"""
	This is a utility for converting english characters to their equivalent urdu characters as defined by the CRULP Urdu Keyboard Layout v1.1 (and vice versa).
"""

# Define the map between english and urdu characters (the latter defined using their Unicode code-points)
# The Urdu characters are easily identifiable as their unicode point starts with 06 i.e. \u06XX

e2u = {
	# Lower-case mappings
	1: f1,
	2: f2,
	3: f3,
	4: f4,
	5: f5,
	6: f6,
	7: f7,
	8: f8,
	9: f9,
	10: f0,
	q: 42,
	a: 27,
	z: 32,
	w: 48,
	s: 33,
	x: 34,
	e: 39,
	d: 2f,
	c: 86,
	r: 31,
	f: 41,
	v: 37,
	t: 2a,
	g: af,
	b: 28,
	y: d2,
	h: 2d,
	n: 46,
	u: 21,
	j: 2c,
	m: 45,
	i: cc,
	k: a9,
	,: 0c,
	o: c1,
	l: 44,
	.: d4,
	p: 7e,
	;: 1b,

	# Upper-case (Shift-ed) mapping
	~: 4b,
	Q: 52,
	A: 22,
	Z: 30,
	W: 51,
	S: 35,
	X: 98,
	E: 70,
	D: 88,
	C: 2b,
	R: 91,
	V: 38,
	T: 79,
	G: 3a,
	Y: 4e,
	H: be,
	N: ba,
	U: 26,
	J: 36,
	M: 58,
	I: 50,
	K: 2e,
	O: c3,
	>: 6b,
	P: 4f,
	?: 1f,
}

def main():

	print("Hello, World")


if __name__ == '__main__':
	
	main()
