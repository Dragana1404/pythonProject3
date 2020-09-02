File1 = open('C:/Users/Nenad/Desktop/Data/fajl1.csv', "r")  #Loading CSV File 1
content1 = File1.read() #Creating first array from File 1
array1 = content1.splitlines()  #Dissection lines
File1.close()
print("\n")
print("File 1: ")
print(content1)
print("\n")

File2 = open('C:/Users/Nenad/Desktop/Data/fajl2.csv', "r") #Loading CSV File 2
content2 = File2.read() #Creating second array from File 2
array2 = content2.splitlines() #Dissection lines
File2.close()
print("\n")
print("File 2: ")
print(content2)
print("\n")

print("Different lines in File 1: ")

for elements in array1: #Passing through first array
  if elements not in array2 or elements==None: #examining the conditions of whether an element from the first array not exists in the second array and whether it is an empty line
        print(elements) #showing the elements of the first array that meets the conditions
