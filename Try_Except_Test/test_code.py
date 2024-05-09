#Try loop to check if file exists when it dosen't exist
# try:
#     f = open("testfile.txt")
# except Exception:
#     print("File dosen't exist")


#Try loop to check if file exists when it does exist
# try:
#     f = open("test_file.txt")
# except Exception:
#     print("File dosen't exist")


#Try loop to check if file exists when it does exist but something else isn't true/dosen't work
# x = "NotAnInt"

# try:
#     f = open("test_file.txt")
#     int(x)
# except Exception:
#     print("File dosen't exist")


#Try loop to check if file exists when it does exist but another variable/thing dosen't match the excpetion type
# x = "NotAnInt"

# try:
#     f = open("test_file.txt") #Creates a FileNotFoundError
#     int(x) #Creates a ValueError
# except FileNotFoundError:
#     print("File dosen't exist")


#Try loop to check if file exists when it does exist but another variable/thing dosen't match the FileNotFoundError
#exception but it matches a latter exception
# x = "NotAnInt"

# try:
#     f = open("test_file.txt")
#     int(x)
# except FileNotFoundError:
#     print("File dosen't exist")
# except Exception:
#     print("Something went wrong")


#Prints the exception
# x = "NotAnInt"

# try:
#     f = open("test_file.txt")
#     int(x)
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e) #Prints "invalid literal for int() with base 10: 'NotAnInt'"


#Using else

# x = 10 #Changed to work in try, it will not raise an exception

# try:
#     f = open("test_file.txt")
#     int(x)
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else: #If there is no exception, this runs
#     print(f.read()) #Prints every line in "test_file.txt"
#     f.close()


#Using finally

# x = 10

# try:
#     f = open("test_file.txt")
#     int(x)
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else: 
#     print(f.read()) 
#     f.close()
# finally: #Runs no matter what
#     print("Executing Finally...")


#Raising exception manually

# x = 10

# try:
#     f = open("normal_file.txt")
#     if f.name == "normal_file.txt":
#         raise Exception
#     int(x)
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e) #Prints empty space
#     print("Error!")
# else: 
#     print(f.read()) 
#     f.close()
# finally:
#     print("Executing Finally...")