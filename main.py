def CheckLeap(Year):    
  if (Year % 4 == 0):   
    print("Given Year is a leap Year");    
  else:  
    print ("Given Year is not a leap Year")   
Year = int(input("Enter the year: ")) 
CheckLeap(Year)
