
# 1. Reading all lines in a file

# f = open("Txtfile.txt", "r")
# print(f.read())
# f.close()



# 2. Read last n lines of a file

# f = open("Txtfile.txt", "r")
# print(f.readline())
# f.close()



# 3. Read from first downwards

# f = open("Txtfile.txt", "r")
# lines = f.readlines() # Returns array of all lines in file
# n = int(input("Enter number:"))

# for i in range(0, n): # For each line between first to n
#     print(lines[i])
# f.close()



# 4. Append then read file

# f = open("Txtfile2.txt", "a")
# f.write("Har\n")
# f.write("Ho\n")
# f.close()

# f = open("Txtfile2.txt", "r")
# print(f.read())
# f.close()



# 5. Read from last upwards

# f = open("Txtfile.txt", "r")
# lines = f.readlines() # Returns array of all lines in file
# n = int(input("Enter number:"))

# for i in range(len(lines) - 1, len(lines) - 1 - n, -1): # For each line between last and last - n
#     print(lines[i])
# f.close()



# 6. Read all lines and assign varaibles

# doubles = dict()
# x = 0
# f = open("Txtfile.txt", "r")
# lines = f.readlines()
# for i in lines:
#     x = x + 1
#     doubles[x] = i
# print(doubles)
# f.close()