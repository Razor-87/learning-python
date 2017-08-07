# 07.08.2017
# working with multiple files


def count_words(filename):
    """Count the approximate number of the words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist"
        # print(msg)
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


filenames = [
    'text_files/alice.txt',
    'text_files/siddhartha.txt',
    'siddhartha.txt',
    'text_files/moby_dick.txt',
    'text_files/little_women.txt',
]

for filename in filenames:
    count_words(filename)
