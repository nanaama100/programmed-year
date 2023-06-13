year = int(input("enter year: "))

if year % 4 == 0:
    if year % 400 == 0: 
        print("Leap Year")
else:
        print("Not a Leap Year")
        
