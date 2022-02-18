
def extract_pattern(p):
	return [(i, c) for i, c in enumerate(p) if c != '*']

def getwordmasks(words):
	newwords = []
	for w in words:
		np = 0
		for c in w:
			i = ord(c) - ord('A')
			if i < 0:
				print(c, len(w), ord(c) - ord('A'), "!"+w+"!")
			np = (1 << i) | np 
		newwords.append((w, np))
	return newwords

def lookup(pattern, mask, negmask, words):
	res = []
	for w, wm in words:
		if mask & wm == mask and negmask & wm == 0:
			match = True
			for i, c in pattern:
				if w[i] != c:
					match = False
			if match:
				res.append(w)
	return res
		

def getmask(pattern, others, hasnot):
	np = 0
	for c in pattern:
		if c != '*':
			i = ord(c) - ord('A')
			np = (1 << i) | np 
	for c in others:
		i = ord(c) - ord('A')
		if i < 0:
			print(c, others)
		np = (1 << i) | np 
	negm = 0
	for c in hasnot:
		i = ord(c) - ord('A')
		negm = (1 << i) | negm 
	return np, negm

		

f = open("words", "r")
words = f.readlines()[0].rstrip('\n').split(' ')

pattern="S*AKE"
others=[]
hasnot="GTRPB"
new_p = extract_pattern(pattern)
mask, negmask = getmask(pattern, others, hasnot)
wordmasks = getwordmasks(words) 

possible_words = lookup(new_p, mask, negmask,  wordmasks) 
print(possible_words)
