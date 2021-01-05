#import pandas as pd

# problem1
with open('gettysburg_address.txt') as f:
    text = f.read()
#text = 'but,'

text = text.split()
#print(text)
mydict = {}

for x in range(len(text)):  # extra credit
    text[x] = text[x].lower()  # makes every element lowercase

text.remove('but,')
text.append('but')

for x in text:
    if x in "-":  # removes extra dashes at end of file
        text.remove(x)
    if "," in x:  # removes all commas from words
        text.append(x[:-1])
        text.remove(x)
    if "." in x:  # removes all periods from words
        text.append(x[:-1])
        text.remove(x)

for x in text:  # populates dictionary
    if x not in mydict:
        mydict[x] = text.count(x)

print(mydict)
print(mydict['but'])
