n = int(input("รับจำนวนตัวเลข: "))
str1 = input("อักขระตัวที่หนึ่ง: ")
str2 = input("อักขระตัวที่สอง: ")
m = n % 2
result = (str1 + str2) * (n // 2) + (m * str1)
print(result)