```
1.
**โจทย์**  
รับค่า n ซึ่งเป็นเลขจำนวนเต็มบวก และรับอักขระ 2 ตัว (บรรทัดละตัว)  
พิมพ์อักขระสลับกัน ความยาว n ตัวในบรรทัดเดียวกัน โดยไม่ใช้ if-else หรือ loop
**ข้อมูลเข้า**  
- บรรทัดที่ 1: จำนวนเต็มบวก n  
- บรรทัดที่ 2: อักขระตัวที่ 1  
- บรรทัดที่ 3: อักขระตัวที่ 2
**ข้อมูลออก**  
- บรรทัดเดียว: อักขระสลับกันความยาว n ตัว
INPUT 
6 
$ 
#
OUTPUT
$#$#$#
INPUT
5 
# 
$
OUTPUT
#$#$#
n = int(input("รับจำนวนตัวเลข: "))
str1 = input("อักขระตัวที่หนึ่ง: ")
str2 = input("อักขระตัวที่สอง: ")
m = n % 2
result = (str1 + str2) * (n // 2) + (m * str1)
print(result)

2.
**โจทย์**  
เขียนโปรแกรมเพื่อรับค่าเศษ (numerator) และค่าส่วน (denominator) ของเศษส่วนสองจำนวน  
แล้วคำนวณหาผลรวมของเศษส่วนทั้งสอง  
สมมติว่าเศษส่วนแรกเป็น a/b และเศษส่วนที่สองเป็น c/d  
แสดงผลลัพธ์ p/q ซึ่งเป็นผลรวมของเศษส่วนทั้งสองในรูปเศษส่วน โดยไม่ต้องทำให้เป็นเศษส่วนอย่างต่ำ
print("first fraction: ")
a = int(input("Enter a numerator a: "))
b = int(input("Enter a denominator b: "))
print("Second fraction: ")
c = int(input("Enter a numerator c: "))
d = int(input("Enter a denominator d: "))
p = (a * d) + (b * c)
q = (b * d)
print(f"Summation of the two fractions is {p} / {q}")

3.
**โจทย์**  
จงเขียนโปรแกรมเพื่อรับจำนวนวินาทีที่ใช้ออกกำลังกาย 2 ครั้ง  
แล้วแสดงผลเวลารวมที่ใช้ในการออกกำลังกายในรูปของจำนวน  
ชั่วโมง นาที และวินาที ตามลำดับ
s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
total = s1 + s2
hour = (total // 3600)
minute = (total % 3600) // 60
second = (total % 3600) % 60
print(f"It is {hour} hours {minute} minutes and {second} seconds.")
