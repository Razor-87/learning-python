# 09.08.2017
def count_the(book):
    """Count the approximate number of the words in a file."""
    with open(book, encoding="utf8") as f_obj:
        content = f_obj.read()
        print(content.lower().count('the'))


books = [
    'text_files/Jack London - South Sea Tales.txt',
    'text_files/Jack London - The Game.txt',
    'text_files/Jack London - The Road.txt',
]

for book in books:
    count_the(book)
