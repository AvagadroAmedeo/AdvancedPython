import os #Used to create files (second way) and delete files

# r = Read
# a = Append (update)
# w = Write
# x = Create

# The f's in this file are short for file...



# Read - error if it dosen't exist

# f = open("names.txt", "r") #Opens file in read, default is read though so no need to add "r"
# print(f.read()) #Read all characters and print them, does not seperate lines
# print(f.read(4)) #Read first four characters and print them, only works if the file hasnt been read before

# print(f.readline()) #Reads firt line and prints it, seperates lines
# print(f.readline()) #If after the one above, reads second line and prints it

# for line in f: #Reads all lines and pritns them, seperates lines
#     print(line) 

# f.close() #Makes the changes show up in the file


# try: #Try when file dosen't exist
#     f = open("names_list.txt")
#     print(f.read())
# except:
#     print("The file dosen't exist")
# finally:
#     f.close()


# try: #Try when file exists
#     f = open("names.txt")
#     print(f.read())
# except:
#     print("The file dosen't exist")
# finally:
#     f.close()



# Append - creates the file if it dosen't exist

# f = open("names.txt", "a") #Opens file in Append
# f.write("Neil") #Puts neil on the last line of the file, even if it isnt empty
# f.close()

# f = open("names.txt", "r")
# print(f.read())
# f.close()


# f = open("names.txt", "a")
# f.write("Neil\n") #Puts neil on a new line at the end
# f.close()

# f = open("names.txt", "r")
# print(f.read())
# f.close()



# Write (overwrite)

# f = open("context.txt", "w") #Opens file in Write
# f.write("I deleted all of the context") #Changes everything in file to "I deleted all the context"
# f.close()

# f = open("context.txt", "r")
# print(f.read())
# f.close()



# Two ways to create a new file

# f = open("name_list.txt", "w") #Opens a file for writing, creates the file if it does not exist
# f.close()


#Creates the specified file but returns an error if the file exists (Note: Could use for user data)
# if not os.path.exists("dave.txt"):
#     f = open("dave.txt", "x") #"x" means create
#     f.close()



# Delete a file

#Avoid an error if it dosen't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("File dosen't exist")