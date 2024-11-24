book_for_search = input()
founded = False
stoped = False
searched_books = 0
while not founded and not stoped:
    book = input()
    if book == 'No More Books':
        stoped = True
        break

    if book == book_for_search:
        founded = True
        break
    searched_books += 1

if founded:
    print(f'You checked {searched_books} books and found it.')
else:
    print(f'The book you search is not here!\r\nYou checked {searched_books} books.')
