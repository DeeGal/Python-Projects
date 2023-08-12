class Book:
    favourites = []

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False

    def __int__(self):
        return f"{self.title} is {self.pages} pages long."

    def __eq__(self, other):
        if self.title == other.title and other.pages:
            return True
        return False

    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)


book = Book("Are you my mother?", 72)

file = open("bookInput.txt", 'w')
file.write("TextBooks:\n")
file.write("Are you my mother?\t  72\n")
file.write("Success\t 72")
file.close()

file = open("bookInput.txt", 'r')
data = file.read()
file.close()
print(data)

file = open("bookInput.txt", 'a')
file.write('Novels:')
file.close()

# 1D AND 2D arrays

ar_1 = [2, 4, 6, 8]  # show the array
print(ar_1)

ar_2 = [2, 4, 6, 8, 10]  # append the array
ar_2.append(20)
print(ar_2)

ar_3 = [2, 4, 6, 8, 10]  # insert the array
ar_3.insert(0, 1)
print(ar_3)

ar_3 = [2, 4, 6, 8, 10]  # sort ASC the array
ar_3.sort()
print(ar_3)

ar_3 = [2, 4, 6, 8, 10]  # sort DESC the array
ar_3.reverse()
print(ar_3)

ar_3 = [2, 4, 6, 8, 10]  # sort length the array
print(len(ar_3))

for i in ar_3:
    print(i)
    
# 2D arrays
ar_4 = [[2, 4, 6, 8], [1, 2, 3, 4, 5]]  # show the array
print(ar_4)

ar_5 = [[2, 4, 6, 8], [1, 2, 3, 4, 5]]  # append the array
ar_5.append(20)
print(ar_5)

ar_6 = [[2, 4, 6, 8], [1, 2, 3, 4, 5]] # insert the array
print(ar_6[1][2])


ar_7 = [[2, 4, 6, 8], [1, 2, 3, 4, 5]]  # sort ASC the array
ar_7[0][2] = 15
print(ar_7)

ar_8 = [[2, 4, 6, 8], [1, 2, 3, 4, 5]]  # sort DESC the array
ar_8.reverse()
print(ar_8)

ar_9 = [[2, 4, 6, 8], [1, 2, 3, 4, 5]]  # sort length the array
print(len(ar_9))

for i in ar_9:
    print(i)

item = [
    ("prod", 10),
    ("prod", 4),
    ("prod", 12),
]


def sort_item(items):
    return items[1]


item.sort(key=sort_item)
print(item)


def search(arraq, num5):
    count = 0
    while i < len(arraq):
        if arraq == num5:
            return True
    count += 1
    return False


arraq = [2, 4, 6, 8, 10]
nu = 7
