import os
import sys

#get the path from the user and check if the path is valid
path=input("give the path: ")
if os.path.exists(path):
  print("Path OK")
else:
  print("wrong path")
  sys.exit()


#list the files in that path
files=os.listdir(path)
print(type(files))
print(files)   #files variable type is List

#use for loop to check each value in the list i.e., file
for each_file in files:
  #join method to concatinate each of file and its path
  relativePath=os.path.join(path,each_file)
  if(os.path.isfile(relativePath)):
    print(f"{relativePath} is a file")
  else:
    print(f"{relativePath} is a directory")