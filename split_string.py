# 1

string = "monkey bat cat dog"

list_string = string.split(" ")

for i in list_string:
    print(i)


# 2
string = "65, 75, 32, 22"

list_string = string.split(", ")
new_list = []

for number in list_string:
    new_list.append(int(number))

for index, number in enumerate(new_list):
    print(f"{index}: {number}")


# 3
string = "one,two,three,four"

list_string = string.split(",")
new_list = []

for i in list_string:
    if i == "zero":
        new_list.append(0)
    elif i == "one":
        new_list.append(1)
    elif i == "two":
        new_list.append(2)
    elif i == "three":
        new_list.append(3)
    elif i == "four":
        new_list.append(4)
    else:
        new_list.append(5)

print(new_list)


#4
string = "W W L T T W"

list_string = string.split(" ")
new_list = []

for i in list_string:
    if i == "W":
        new_list.append(2)
    elif i == "L":
        new_list.append(0)
    else:
        new_list.append(1)
    
print(new_list)

#5
string = "x:3,x:6,x:14,x:22"

splice_one = string.split("x:")
string_two = ""

for i in splice_one:
    string_two += i
splice_two = string_two.split(",")
final_list = []

for a in splice_two:
    final_list.append(int(a))

print(final_list)


#6
string = "x:2,y:5 - x:5,y:11 - x:7,y:14"
new_string = ""
final_list = []
final_string = ""
y_found = False
x_found = False

splice_one = string.split(" - ")

for i in splice_one:
    splice_two = i.split(",")

    for a in splice_two:
        splice_three = a.split(":")
        final_list.append(splice_three)

for i in range(len(final_list)):
    for a in final_list[i]:
        if a == "x":
            final_string += "["
            y_found = False
        elif a == "y":
            y_found = True
            x_found = False
        elif a == " ":
            continue
        else:
            if y_found == True:
                final_string += a
                final_string += "]"

                if i+1 != len(final_list):
                    final_string += ", "
            
            else:
                final_string += a
                final_string += ", "

print(final_string)