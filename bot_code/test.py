# Type 1: The words share 3 letters in common.
# Excludes the first 2 letters of the first word and the last 2 of the second.
# If so, removes from the first word everything after the common string and removes from the second word the common
# string and everything before it and concatenates them
# Ex. hamster + termite = hamstermite
def common3String(string1, string2):
	for i in range(2, len(string1), -1):
		for j in range(0, len(string2) - 3):
			if string1[i-3:i] == string2[j:j+3]:
				return string1[:i] + string2[j+3:]
	return "n/a"

# Type 2: The words share a common consonant.
# Excludes the first letter and last 2 letters of the second word, and the first two letters of the first word.
# The letter is removed from the second word and the words are appended.
# Ex. beeffalo = beef + buffalo; Reagan + economics = Reaganomics
def commonEndConsonant(string1, string2):
	vowels = ["a", "e", "i", "o", "u", "y"]
	for i in range(len(string1) - 1, 2, -1):
		for j in range(1, len(string2) - 3):
			if string1[i] == string2[j] and string1[i] not in vowels and string2[j] not in vowels:
				pme = string1[:i] + string2[j:]
				return pme
	return "n/a"

# Type 3: the strings contain the same vowel
# Excludes the first 2 letters of the first word and the last 2 letters of the second word)
# If so, removes from the first word everything after the common vowel and removes from the second word the common
# vowel and everything before it and concatenates them
def sameVowelComp(string1, string2):
	vowels = ["a", "e", "i", "o", "u", "y"]
	for i in range(2, len(string1)):
		for j in range(len(string2) - 3, 0, -1):
			if string1[i] == string2[j] and string1[i] in vowels and string2[j] in vowels:
				return string1[:i] + string2[j:]
	return "n/a"

# Type 4: The strings contain differing vowels (should cover all the other cases)
# If so, takes the last vowel in the first word and the first vowel in the second word...
# Removes from the first word the chosen vowel and everything after and removes from the second word everything before
# the chosen vowel and concatenates them
# (Note: keeping the vowel from the second word facilitates rhyming the portmanteau with the original phrase
def diffVowelComp(vowelList1, vowelList2, string1, string2):
	max1 = max(vowelList1)
	min2 = min(vowelList2)
	return string1[:max1] + string2[min2:]

# Returns a list with vowel positions in input string
def vowelFinder(string):
	vowels = ["a", "e", "i", "o", "u", "y"]
	counter = 0
	vowelList = []
	for i in string:
		if i in vowels:
			vowelList.append(counter)
		counter += 1
	return vowelList

# Portmanteau handler function
def portmanteau(string1, string2):
	if common3String(string1, string2) != "n/a":  # Type 1
		return common3String(string1, string2)
	elif commonEndConsonant(string1, string2) != "n/a":  # Type 2
		return commonEndConsonant(string1, string2)
	elif sameVowelComp(string1, string2) != "n/a":  # Type 3
		return sameVowelComp(string1, string2)
	else:  # Type 4 (everything else)
		return diffVowelComp(vowelFinder(string1), vowelFinder(string2), string1, string2)

def main():
	word1 = input("Enter a word: ")
	word2 = input("Enter another word: ")

	pme = portmanteau(word1, word2)
	if pme == "n/a":
		print("No portmanteau found.")
	else:
		print(word1 + " + " + word2 + " = " + pme)

main()
