# num = input()
# print("you entered", num)

# try:
#     num = int(input("enter a number: ")) # input reads things as a string
#     print("you entered", num)
#     num += 1
#     print(num)
# except:
#     print("You need to enter an integer")

print("\nFile Practice:")

with open('movies.txt') as file:
    for line in file:
        print(line.strip(), end=' ') # strip() rips off \n character, end=' ' makes them not have their own new line

print("\n")

heights = {} # declare dictionary outside of algorithm

with open('heights.txt') as file:
    for line in file:
        line = line.strip()
        print(line)
        values = line.split() # breaks up and stores different line components into a list (here, 1st and last name and heights)
        print(values)
        heights[f'{values[0]} {values[1]}'] = int(values[2])
    print(heights)

    