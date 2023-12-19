from deck import deck

file = input("Pick a file: ")
t = input("Pick the type: ")
front = input("Pick a color for front: ")
back = input("Pick a color for back: ")
height = float(input("The height: "))
width = float(input("The width: "))


# deck('cards.json',"sentences", "#f0f0f0", "#ffcc00", 3.5, 2.5)
# deck('cards.json',"objects", "#f0f0f0", "#f2a5e5", 1, 2.5)
deck(file, t, front, back, height, width)

