# Part 1: Numbers
books_owned = 5 # Integer
book_price = 24.99 # Float
total_pages = 1250 # Integer

totalBooksCost= book_price*books_owned
print(totalBooksCost) #1 Working with Numbers

averagePagesPerBook= total_pages/books_owned
print(averagePagesPerBook) #2 Working with Numbers   

DaysToCompleteAllBooks= 3*books_owned
print(DaysToCompleteAllBooks) #3 Working with Numbers

# Part 2: Strings
book_name = "Alice in Wonderland"
author_name = "Lewis Carroll"

bookTitle= book_name+ " - " +author_name
print(bookTitle) #1 Working with Strings
print(book_name.upper()) #2 Working with Strings> use upper()
print(book_name.count("a")) #3 Working with Strings> use count()
print(author_name.lower()) #4 Working with Strings> use lower()

# Part 3: Collections
my_books = ["Harry Potter", "Percy Jackson", "Charlotte's Web"]
book_categories = ("Fantasy", "Adventure", "Mystery")
favorite_book = {
"title": "Harry Potter",
"pages": 223,
"price": 19.99,
"is_hardcover": True
}

print(my_books)
newBookList= my_books.append("The Hobbit")
print(my_books) #1 Working with Collections> use append to add to the list
print(book_categories[1])  #2 Working with Collections
favorite_book.update({"year": 1997})  
print(favorite_book) #3 Working with Collections> use update to add to dictionary
print(my_books[0], my_books[-1]) #4 Working with Collections first and last 

book_prices= [19.99, 24.99, 12.50,34.99, 9.99]
print(book_prices) #5 Working with Collections
price1= book_prices[0]*.80
price2= book_prices[1]*.80
price3= book_prices[2]*.80
price4= book_prices[3]*.80
price5= book_prices[4]*.80

booksDiscounted= (price1 + price2 +price3 + price4 + price5)/5 
print(booksDiscounted)