#string

a="hello"
print(a.upper())
print(a.lower())

#Swapcase
c="Hello"
print(c.swapcase())

#capitalize
s="hello"
print(s.capitalize())

#starts with
a="python is a useful tool"
print(a.startswith("p"))

#endswith
name="strings.py"
print(name.endswith(".py"))

#strip
h="     hello     "
print(h)

#split
a="nancy love singing"
print(a.split())

#replace
a="time"
print(a.replace('t','l'))

#formatting Methods

b="nancy"
print(f"{b} loves ice cream")

#center
a="hello"
print(a.center(10))
print(a.center(10,'*'))

#ljust
g="hello"
print(g.ljust(20))

#rjust
g="spiderman"
print(g.rjust(5))

#zfill
z="hii"
print(z.zfill(6))

#checking numbers
#isdigit
a="1234wer"
print(a.isalnum())
b="1234"
print(b.isdigit())
c="heloo"
print(c.isalpha())
d="143dathu"
print(d.isascii())


#combained task
u="hello"
print(u.strip())
print(u.capitalize())
print(u.startswith('h'))

#check ascii,py,isalnum
r="124 is password of py"
print(r.isascii())
print(r.endswith('py'))
print(r.isalnum())

#mobile number
n="915067860"
print(n.isdigit)
print(n.zfill(15))


#sentence
s="my dog name is tobby"
print(s.upper())
print(s.split())



#for else task
for i in range(1,6):
    print(i)
else:
  print("loop completed")

#even numbers
'''for i in range(1.11):
  if i%2==0:
    print(i)
else:
  print("loop completes")'''

 #print python
for h in "python":
  print(h)  
else:
  print("loop completes")

'''#find 5
1=[1,6]
for i in numbers:
  if i==5:
    print("found 5")
    break
else:
  print("5 not found")'''


#apple
word='apple'
for i in word:
  if i=="a":
    print("happy")
    break
else:
  print("not happy")
