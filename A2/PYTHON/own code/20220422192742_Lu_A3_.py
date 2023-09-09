"""Hudson Xingcheng Lu              2031140
420-LCU Computer Programming, Section # 
S. Hilal, instructor 
Assignment 3 
"""

 #dictionary of dictionaries
dx = open('books.txt') #

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
    book_dict['sold']=int(book_record[4])
    Books_1.setdefault(k, book_dict)
    Books ={}
for Books_1 in sorted(Books_1.items()):
    Books.setdefault(Books_1[0], Books_1[1])

for lines in Books.items():
    a = '{:51s}'.format(lines[0])
    b = '{:26s}'.format(lines[1]["author"])
    c = '{:11s}'.format(lines[1]["lang"])
    d = '{:23s}'.format(lines[1]["type"])
    e = '{:11d}'.format(int(lines[1]["sold"])) 
    #print(a,b,c,d,e)
dx.close()

#################################

menu="""

Here’s the list of available options: 

1- How many different languages are there? 
2- What language has the most books?  
3- Display all the books in a language. 
4- How many different types of books are there? Print a numbered list of the types? Which type has most copies sold? 
5- List all authors who have more than one book on the list.  
6- List the top 10 authors based on the number of books they have authored.
7- For a given author, what is the total number of books sold?
8- List all books of a given type. 
9- What are the top 5 types of books based on total sold? 
10- Display a pie chart plot to show the distribution of books among the top 5 types of books. 
11- Exit 
"""

option = 1
while option !=11:
    option = int(input(menu+ '\nEnter your option:'))
######################
    if Books == {}:
        print('Error! The dictionary is empty!')
        break
    elif option == 1: #1

        languages_1 = {} # dictionary with a list of languages numbered. (e.g 1: 'English')
        x = 0
        for b in Books.values():
            if not b['lang'] in languages_1.values():
                x += 1
                languages_1.setdefault( x , b['lang'])
        print ( '\nThere are', max(languages_1), 'different languages\n')    
        for key , val in languages_1.items():
            print ('{:1d}'.format(key)+'-' , '{:10s}'.format(val) )
######################        
    elif option == 2: #2
        languages_2 = {} #each book's language(value) numbered(key)
        x = 0
        for b in Books.values():
            if not b['lang'] in languages_2:
                x += 1
                languages_2.setdefault( x , b['lang'])


        languages = {}
        for y in languages_2.values():
            languages.setdefault (y, 0) # create key if missing
            languages[y] += 1

        z = max(languages, key = languages.get)  #language with the most books   
        print ( '\nThe language that has the most books is' , z )
######################
    elif option == 3: #3
        language = input('\nInput a language:')

        b = {} #books(key) of a specific language with their data(value)
        for a in Books.items():
            if a[1]['lang'] == language:
                a_1 = a[1]
                a_0 = a[0]
                b.setdefault(a_0, a_1)

        for lines in b.items():        
            a_1 = '{:51s}'.format(lines[0])
            b_1 = '{:26s}'.format(lines[1]["author"])
            d_1 = '{:23s}'.format(lines[1]["type"])
            e_1 = '{:11d}'.format(int(lines[1]["sold"]))
            print(a_1,b_1,d_1,e_1)
######################
    elif option == 4: #4
        types = {} # all types of books
        x = 0
        for c in Books.values():
            if not c['type'] in types.values():
                x += 1
                types.setdefault( x , c['type'])

        print ('\nThere are', max(types), 'different types of books\n')
        for key , val in types.items():
            print ('{:1d}'.format(key)+'-' , '{:20s}'.format(val) )



        types_1 = {} #all types for each book
        x = 0
        for b in Books.values():
            if not b['type'] in types_1:
                x += 1
                types_1.setdefault( x , b['type'])

        types_0 = {}   ##of each type with book
        for y in types_1.values():
            types_0.setdefault (y, 0) # create key if missing
            types_0[y] += 1
            

        types_2 = {} # total sum
        for y in types_1.values():
            types_2.setdefault (y, 0) # create key if missing
            for lines in Books.items():
                a_1 = lines[1]
                a_0 = lines[0]
                types_2[y] += lines[1]['sold']

        w= max(types_2, key = types_2.get)
        print('\nThe type has most copies sold is', w)
######################
    elif option == 5: #5
        authors = {} # the authors(value) of each single book numbered(key)
        x = 0

        for b in Books.values():
            if not b['author'] in authors:
                x += 1
                authors.setdefault( x , b['author'])

        authors_1 = {}
        for y in authors.values():
            authors_1.setdefault (y, 0) # create key if missing
            authors_1[y] += 1



        for key_1 , val_1 in authors_1.items():
            if val_1 > 1:     # authors with more than 1 book
                print ('{:17s}:'.format(key_1) , '{:1d}'.format(val_1) )
######################
    elif option == 6: #6
        authors = {} # the authors(value) of each single book numbered(key)
        x = 0

        for b in Books.values():
            if not b['author'] in authors:
                x += 1
                authors.setdefault( x , b['author'])

        authors_1 = {}
        for y in authors.values():
            authors_1.setdefault (y, 0) # create key if missing
            authors_1[y] += 1
        ###### from the previous option
        x = 0
        y = list(range(1,11))
        w = []
        while x != 11:
            z = max (authors_1, key =authors_1.get )
            w = w + [z]
            x +=1
            authors_1. pop(z, 0)
        print('The top 10 authors based on the number of books they have authored:')   
        for key,value in dict(zip(y, w)).items():
            o = str(key)+'-'
            print(o, value)
######################
    elif option == 7: #7
        author = input('Input an author name:')
        z = 0
        for a in Books.items():
            if a[1]['author'] == author:
                z = z + a[1]['sold']
        print('The total number of books sold is', z)

######################
    elif option == 8: #8
        types = {} # all types of books
        x = 0
        for c in Books.values():
            if not c['type'] in types.values():
                x += 1
                types.setdefault( x , c['type'])

        print ('List of different types of books:')
        for key , val in types.items():
            print ('{:1d}'.format(key)+'-' , '{:20s}'.format(val) )

        #####similar to option 4

        types_1 = {} #all types for each book
        x = 0
        for b in Books.values():
            if not b['type'] in types_1:
                x += 1
                types_1.setdefault( x , b['type'])

        types_0 = {}   #of each type with book
        for y in types_1.values():
            types_0.setdefault (y, 0) # create key if missing
            types_0[y] += 1
            
        #######
        types = input('\nInput a type:')

        b = {}
        for a in Books.items():
            if a[1]['type'] == types:
                a_1 = a[1]
                a_0 = a[0]
                b.setdefault(a_0, a_1)
                #print(a[0])

        for lines in b.items():        
            a_1 = '{:51s}'.format(lines[0])
            b_1 = '{:26s}'.format(lines[1]["author"])
            d_1 = '{:23s}'.format(lines[1]["lang"])
            e_1 = '{:11d}'.format(int(lines[1]["sold"]))
            print(a_1,b_1,d_1,e_1)

######################
    elif option == 9: #9
        types = {} # all types of books
        x = 0
        for c in Books.values():
            if not c['type'] in types.values():
                x += 1
                types.setdefault( x , c['type'])

        #for key , val in types.items():    
            #print ('{:2d}'.format(key) , '{:20s}'.format(val) )
        types_1 = {} #all types for each book
        x = 0
        for b in Books.values():
            if not b['type'] in types_1:
                x += 1
                types_1.setdefault( x , b['type'])

        types_0 = {}   ##of each type with book
        for y in types_1.values():
            types_0.setdefault (y, 0) # create key if missing
            types_0[y] += 1
        
        types_2 = {} # total sum
        for y in types_1.values():
            types_2.setdefault (y, 0) # create key if missing
            for lines in Books.items():
                a_1 = lines[1]
                a_0 = lines[0]
                types_2[y] += lines[1]['sold']
        ###similar to previous options
        x = 0
        y = list(range(1,6))
        w = []
        while x != 6:
            z = max (types_2, key =types_2.get )
            w = w + [z]
            x +=1
            types_2. pop(z, 0)
            
        print('The top 5 types of books based on total sold:')
        for key,value in dict(zip(y, w)).items():
            o = str(key)+'-'
            print(o, value)
######################
    elif option == 10: #10
        types = {} # all types of books
        x = 0
        for c in Books.values():
            if not c['type'] in types.values():
                x += 1
                types.setdefault( x , c['type'])

        #for key , val in types.items():    
            #print ('{:2d}'.format(key) , '{:20s}'.format(val) )



        types_1 = {} #all types for each book
        x = 0
        for b in Books.values():
            if not b['type'] in types_1:
                x += 1
                types_1.setdefault( x , b['type'])

        types_0 = {}   #(value)#of each type(key) with book
        for y in types_1.values():
            types_0.setdefault (y, 0) # create key if missing
            types_0[y] += 1

        #####similar to previous options
        types_2 = {} # total sum
        for y in types_1.values():
            types_2.setdefault (y, 0) # create key if missing
            for lines in Books.items():
                a_1 = lines[1]
                a_0 = lines[0]
                types_2[y] += lines[1]['sold']
        x = 1
        y = list(range(1,6))
        w = []#keys
        while x != 6:
            z = max (types_2, key =types_2.get )
            w = w + [z]
            x +=1
            types_2. pop(z, 0)

        #values
        w0= types_0[w[0]]
        w1= types_0[w[1]]
        w2= types_0[w[2]]
        w3= types_0[w[3]]
        w4= types_0[w[4]]

        Nbooks= [w0, w1, w2, w3, w4]#number of books for top 5 types

        #Statistics on Banking Fraud that occurred in India circa 2016
        import matplotlib
        import matplotlib.pyplot as pl

        Books5 = w
        colors = ["blue", 'yellow', 'green', 'red', 'grey']
        Nofbooks = Nbooks
        pl.pie(Nofbooks, labels=Books5, colors=colors, startangle=90, autopct='%1.1f%%')
        pl.axis('equal')
        pl.title('Statistics on the distribution of books among the top 5 types of books published in Time magazine')
        pl.show()

######################
    elif option == 11: #11
        break
        







