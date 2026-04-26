#to take input
password=input("enter a password:")
#for check length
length_ok= len(password) >=8

has_upper= any(c.isupper() for c in password)
has_lower= any(c.islower() for c in password)
has_digit= any(c.isdigit() for c in password)
has_special= any( c in "!@#$%^&*()_+-=[]{}|;:,.<>" for c in password)
#to give score
score=0
if length_ok:
    score +=1
if has_upper:
    score +=1    
if has_lower:
    score=+1
if has_digit:
    score+=1
if has_special:
    score+=1

if score<=2:
    result="weak"
elif score<=4:
    result="average"
else:
    result="strong"

print(f"password strength:{result}")
print(f"score:{score}/5")
       