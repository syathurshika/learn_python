num=int(input("Enter a number between 1 and 100:"))

if num<50:
    print(f"{num} is too low")
elif num>80:
    print(f"{num} is too high")
elif num!=75:
        print(f"{num} is just right")
else:
    print(f"{num} is perfect!")