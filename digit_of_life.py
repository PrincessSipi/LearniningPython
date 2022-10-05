birthday = input("Enter your birthday: in the format YYYYMMDD or YYYYDDMM or MMDDYYYY ")
num_birthday = birthday.replace(" ","")
digit_of_life = 0
for num in num_birthday:
    digit_of_life += int(num)
if len(digit_of_life) > 1:
    for nums in digit_of_life:
        digit_of_life += nums
print(digit_of_life)
