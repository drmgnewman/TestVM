# Collections
# String: str
# Bytes: bytes
# Arrays: list
# Dictionary: dict

# 1) Strings: Immutable sequence of unicode codepoints

# Single and double quotes

h = 'This is a string'

print(h)

h = "This is a string with double quotes"
print(h)

# Multiline strings: triple double or single quotes

h = """This is a
long multi line
string"""

print(h)

m = "This\\ is\nmulti\nline"
print(m)

# Raw strings
path = r'C:\User\Documents\Books'
path = r"C:\Use'r\Documents\Books"
print(path)

# String as sequences
s = "parrot"
print(s)
print(s[0])
print(s[4])
# Use the type() function to get the object's type
print(type(s))

# Bytes: similar to strings, but instead a sequence
# of Unicode points is a sequence of bytes.
# use for raw binary data, fixed-width, ASCII

bt = b'data'
print(bt)

# Encode data: utf-8
# o = Alt+162

l = "Visitamos el zoologico"
print(l)
data = l.encode("utf-8")
print(data)
# now decode it
s = data.decode("utf-8")
print(s)

# Arrays: A list of mutable objects
# Replace, remove or append elements
# Delimited by [] and items are
# separated by commas
l = [1, 2, 3]
print(l)
print(type(l))
a = ["apple", "orange", "pear"]
print(a[1])
# print(a[3])
b = ["Waldo", 2, 4.5]
print(b)
ll = ["apple", "john", [1, 2, 3]]
print(ll)

c = ["bear", "horse", "elephant",]
print(c)

# Add members
c.append("giraffe")
print(c)

# list constructor: list()
m = list("Characters")
print(m)

m.insert(2,"bird")
print(m)

# Dictionaries: Mutable mapping of keys to values
# Values are not in any particular order
# {k1: v1, k2: v2}

d = {'alice':"(801)789-4562", 'pedro':"(956)123-7845"}
print(type(d))
print(d)

# Access a member

print(d['alice'])

# Update the member's value
d['alice'] = '(801)789-4562'
print(d)
# If value exist, it is updated
# If value does not exit, it will add it
d['maria'] = '(801)459-7845'
print(d)

# e = {}

# For loops: visit each item in an iterable series

cities = ["London", "Madrid", "Paris", "Ogden"]
for city in cities:
    print(city)

# Access members of dictionary, a for loop gets
# the key value.

for i in d:
    print(i, "->", d[i])

# Access members with index notation
