#Hudson Xingcheng Lu              2031140
#420-LCU Computer Programming, Section #00002
# S. Hilal, instructor
# Lab 10


 #dictionary of dictionaries

dx = open('books.txt') #/Users/hudson/Desktop/books.txt

Books_1 ={}
for line in dx.readlines(): # Or just fp:
    line = line.strip('\n')
    book_record = line.split(',')
    values = book_record[1:]
    k = book_record[0] #title
    keys = 'author', 'lang', 'type', 'sold'
    books = dict(zip(keys, values))
    book_dict = {}
    book_dict['author']=book_record[1]
    book_dict['lang']=book_record[2]
    book_dict['type']=book_record[3]
    book_dict['sold']=book_record[4]
    Books_1.setdefault(k, book_dict)
    Books ={}
for Books_1 in sorted(Books_1.items()):
    Books.setdefault(Books_1[0], Books_1[1])

for lines in Books.items():
    a = '{:51s}'.format(lines[0])
    b = '{:26s}'.format(lines[1]["author"])
    c = '{:11s}'.format(lines[1]["lang"])
    d = '{:23s}'.format(lines[1]["type"])
    e = '{:8s}'.format(lines[1]["sold"])
    print(a,b,c,d,e)

dx.close()

