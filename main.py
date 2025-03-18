import sys
from stats import count_words, count_chars, sort_chars

def get_book_text(filepath):
	with open(filepath) as f:

		file_contents = f.read()

		return file_contents

def main():
	book_path = ""

	args = sys.argv

	if len(args) > 1:
		book_path = args[1]
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	contents = get_book_text(book_path)

	# print(contents)

	word_count = count_words(contents)

	char_counts = count_chars(contents)
	char_lst = sort_chars(char_counts)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print(f"--------- Character Count -------")

	for chr in char_lst:
		char = chr["char"]
		count = chr["count"]

		if char.isalpha():
			print(f"{char}: {count}")

	print("============= END ===============")

main()
