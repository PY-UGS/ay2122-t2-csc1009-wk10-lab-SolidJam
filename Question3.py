#Tasked to create another Python project that is the repeat of Question 2b and 2c from Laboratory Wk01.

#Question2B
#ask for module code
modCode = input("Please enter the module code: ")

if (modCode == "CSC1006"):
    print("Mathematics 2")
    
elif (modCode == "CSC1007"):
    print("Operating Systems")
    
elif (modCode == "CSC1008"):
    print("Data Structures and Algorithms")
    
elif (modCode == "CSC1009"):
    print("Object-Oriented Programming") #when input CSC1009; OOP
    
elif (modCode == "CSC2902"):
    print("Career and Professional Development")
    
else:
    print("Invalid Module Code") #when key in invalid module code

#Question2C
#loop starting from 102 to 66 in descending order
print("Descending odd numbers from 102 to 66:")

#Loop from 102 to 65
for i in range(102, 65, -1):
    #Checks if i is an odd number
    if (i % 2 == 1): 
        #Prints out odd numbers
         print(i,end=" ")