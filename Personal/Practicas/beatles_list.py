beatles = []
names =["John Lennon","Paul McCartney","George Harrison"]

for i in names:
    beatles.append(i)

for i in range(2):
    name = input("Type name: ")
    beatles.append(name)
    del beatles[-1]
beatles.insert(0,'Ringo Starr')
print(beatles)