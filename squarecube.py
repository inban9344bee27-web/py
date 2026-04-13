squares = {i**2 for i in range(1,11)}
cubic = {i**3 for i in range(1,11)}
print("Square = ",squares)
print("Cubic = ",cubic)
squares.update(cubic)
print("Square + cubic = ",squares)
popelem=squares.pop()
print("Popped element = ",popelem)
print("Square after pop = ",squares)
remove=4
if remove in squares:
   squares.remove(remove)
   print("Removed element {remove} from squares")
else:
   print("Element {remove}notfound in squares")
print(squares)
squares.clear()
print(squares)
print(cubic)
