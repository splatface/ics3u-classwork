earth_weight = float(input("What is your earth weight in lbs?"))

planet = int(input("(1) Venus, (2) Mars, (3) Jupiter, \n(4) Saturn, (5) Uranus, (6) Neptune. Input the planet:"))

if planet == 1:
    p_weight = 0.78 * earth_weight

if planet == 2:
    p_weight = 0.39 * earth_weight

if planet == 3:
    p_weight = 2.65 * earth_weight

if planet == 4:
    p_weight = 1.17 * earth_weight

if planet == 5:
    p_weight = 1.05 * earth_weight

if planet == 6:
    p_weight = 1.23 * earth_weight

print(f"Your weight would be {p_weight} on that planet.")
