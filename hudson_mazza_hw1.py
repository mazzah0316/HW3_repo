year = input("Enter Year: ")
try:
    year_int = int(year)
    if year_int % 4 == 0 and year_int % 100 != 0:
        print(year_int, "is a Leap Year")
    elif year_int % 400 ==0:
        print(year_int, "is a Leap Year")
    else:
        print(year_int, "is not a Leap Year")
except ValueError:
    print ("Input is not a valid year")