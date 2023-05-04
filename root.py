import os
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# filename1 = os.path.join('password.txt')
# filename = "C:\Users\hamza\Desktop\Scripting\password.txt"

filename2 = "C:/Users/hamza/Desktop/Scripting/password.txt"
print("the filename is 2 is : ",filename2)

# Open the password file with read-only access for the owner (root)
with open(filename2,'r') as f:
    # Read the login and password from the file
   login, password = f.read().strip().split()
   

# Use the login and password in the command
cmd = f'pmchat "" "{login}\n{password}" [ /dev/serial/by-opengear-id/port03'
os.system(cmd)

