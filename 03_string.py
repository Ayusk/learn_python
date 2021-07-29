a="ayushkumar"
print(a[0:2])
print(a[0::3])


# use of replace function 
s = '''hey <|NAME|> 
you have been selected
on date <|DATE|>'''

name = input("Enter your name")
date = input("Enter a date")

s = s.replace("<|DATE|>",date)
s = s.replace("<|NAME|>",name)

print(s)