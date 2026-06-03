age=int(input("Enter your age:"))
citizen=input("Are you a citizen? (yes/no)")
print(f"Eligible to vote: {age>=18 and citizen=='yes'}")