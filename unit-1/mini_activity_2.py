#Calculate the perimeter of a rectangle

#get dimensions
rectangle_length = int(input("How long is the rectangle? "))
rectangle_width = int(input("How wide is the rectangle? "))

#calculate and output
rectangle_perimeter = rectangle_length * 2 + rectangle_width * 2
print(f"The perimeter of the rectangle is {rectangle_perimeter}")