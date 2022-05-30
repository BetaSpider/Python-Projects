import random
lc="abcdefghijklmnopqrstuvwxyz"
uc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
sym="~!@#$%^&*()_+=-{}[];:\|<>,.?/"
pwd=lc+uc+num+sym
length=10

password="".join(random.sample(pwd,length))

print("Your password is:",password)
