string = input("Entre a string: ")
index = 0
even_characters = ""
#len length se nikla hy  or yh python ka ek built in function hy or < ka sign islie lgaya hy ta k loop stop hojae
while index < len(string):
# % ka mtl remainder h yh even find krny ka rule hy, 0 ki jagah 1 likhy gy to odd values dy ga
    if index %2 == 0:
         even_characters = even_characters + string[index]
    index+=1
print("Characters at even position", even_characters)