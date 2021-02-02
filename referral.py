import math
import random

alph="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
number="0123456789"
string=alph+number

l=len(string)
referral_code=""
for i in range(8):
    referral_code += string[math.floor(random.random()*l)]
print("Your Refferal Code: ",referral_code) 