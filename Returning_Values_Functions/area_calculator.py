import math

def area_circle(radius: int) -> float:
    area = math.pi*(radius**2)

    return area

def area_rectangle(length: float, width: float) -> float:
    area = length * width

    return area

def area_square(side: float) -> float:
    area = side**2

    return area

def area_triangle(base: float, height: float) -> float:
    area = (base * height) / 2

    return area

def main():
    choice = int(input("(1) circle, (2) rectangle, (3) square, (4) triangle, (5) quit: "))

    if choice == 1:
        area = area_circle(int(input("Radius: ")))
        print(f"The area of the circle is {area}.")
    
    elif choice == 2:
        area = area_rectangle(int(input("Length: ")), int(input("Widht: ")))
        print(f"The area of the rectangle is {area}.")
    
    elif choice == 3:
        area = area_square(int(input("Side Length: ")))
        print(f"The area of the square is {area}.")
    
    elif choice == 4:
        area = area_triangle(int(input("Base: ")), int(input("Height: ")))
        print(f"The area of the triangle is {area}.")
    
    else:
        quit()

while True:
    if __name__ == "__main__":
        main()