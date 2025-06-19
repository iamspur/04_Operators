s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
total = s1 + s2
hour = (total // 3600)
minute = (total % 3600) // 60
second = (total % 3600) % 60
print(f"It is {hour} hours {minute} minutes and {second} seconds.")