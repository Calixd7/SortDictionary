books = [
  {"name": "The Color Purple", "author": "Walker, Alice", "price":19.99},
  {"name": "The Autobiography of Malcolm X", "author": "X, Malcolm", "price":29.99},
  {"name": "Sasha Savvy Loves to Code", "author": "Alson, Sasha Ariel", "price":10},
]

# Test one book under 20
x = books[1]["price"]
if x <= 20:
  print(x)
else:
  print ("All books over $20.00")

# Test one book over 20
y = books[2]["price"]
if y <= 20:
  print(y)
else:
  print ("All books over $20.00")
#prints the price but not the title

for b in books:
  print (b["price"])
#all prices print, no title


#SOULTION


def sortBooks(list):
  for i in list:
    if i["price"] <=20: #checks the price
      print (i["name"] + " is under $20.00,") #prints the title
    else:
      print (i["name"] + " is over $20.00,")

sortBooks (books)





#print just the books under 20
def underTwentyOnly(list):
  for i in list:
    if i["price"] <=20: #checks the price
      print (i["name"]) #prints the title
    else:
      print 

underTwentyOnly (books) 