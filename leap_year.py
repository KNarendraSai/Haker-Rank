n=int(input("enter the year :"))
def leap_year(n):
    if n % 4==0:
        if n % 100==0:
            if n % 400==0:
                return True


            else:
               return False
        else:
          return False
    else:
        False

k=leap_year(n)
print(k)