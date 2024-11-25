import math

# same result as herons_formula_no_function, 32 lines (no triangle area included) vs 49 in no_function
# easier to fix "herons_formula.py" as it only has one occurence of (a+b+c) // 2 as it is a funciton
def main():
    area = triangle_area(3, 3, 3)
    print(f"A triangle with sides 3, 3, 3 has an area of {area}")

    area = triangle_area(3, 4, 5)
    print(f"A triangle with sides 3, 4, 5 has an area of {area}")

    area = triangle_area(7, 8, 9)
    print(f"A triangle with sides 7, 8, 9 has an area of {area}")

    area = triangle_area(5, 12, 13)
    print(f"A triangle with sides 5, 12, 13 has an area of {area}")

    area = triangle_area(10, 9, 11)
    print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
    area = triangle_area(8, 15, 17)
    print(f"A triangle with sides 8, 15, 17 has an area of {area}")

    area = triangle_area(9, 9, 9)
    print(f"A triangle with sides 9, 9, 9 has an area of {area}")
    # very easy to add this extra function as it only needs to call the function and do a print


def triangle_area(a: int, b: int, c: int) -> float:
    """Calculates a triangles area.
    
    Args:
        a: length of side a
        b: length of side b
        c: length of side c
    
    Returns:
        The area of the triangle
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area
    # ^ after computing the area, "return" it


if __name__ == "__main__":
    main()