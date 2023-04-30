import string
import random 
low_len=int(input("Enter the no. of lowercase characters : "))
upp_len=int(input("Enter the no. of uppercase characters : "))
dig_len=int(input("Enter the no. of digits : "))
symbol_len=int(input("Enter the no. of symbols : "))
pwd_len=low_len+upp_len+dig_len+symbol_len
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbol = string.punctuation
str=random.choices(lower,k=low_len)+random.choices(upper,k=upp_len)+random.choices(digit,k=dig_len)+random.choices(symbol,k=symbol_len)
print(str)
random.shuffle(str)
password="".join(str)
print("Password is : ",password)