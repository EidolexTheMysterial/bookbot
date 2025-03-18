
def count_words(contents):
	words = contents.split()

	count = len(words)

	# print(f"{count} words found in the document")
	return count


def count_chars(contents):
	char_lst = {}

	for c in contents:
		c = c.lower()

		if c in char_lst:
			char_lst[c] += 1
		else:
			char_lst[c] = 1

	# print(char_lst)
	return char_lst

def sort_on(dict):
	return dict["char"]

def sort_chars(char_lst):
	sorted_lst = []

	for c in char_lst:
		chr_set = {
			"char": c,
			"count": char_lst[c]
		}

		sorted_lst.append(chr_set)
	
	sorted_lst.sort(key=sort_on)

	return sorted_lst
