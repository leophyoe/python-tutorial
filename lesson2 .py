#python Operators
#python များတွင် သင်ယူမည့် ပထမဆုံး အကြောင်းအရာမှာ Operator များ ဖြစ်သည်။ Arithemetic Operator များသည် သင်၏ ကုဒ်များတွင် အရေးပါသော အခန်းကဏ္ဍတစ်ခု ဖြစ်သည်။ Operator များကို သင်သည် သင်၏ ကုဒ်များတွင် အမျိုးအစားအလိုက် ခွဲခြား အသုံးပြုနိုင်သည်။ 

#Arithmetic Operators
#Arithmetic Operators များသည် သင်၏ codeများကို ဂဏန်းဆိုင်ရာ လုပ်ဆောင်ချက်များကို ဆောင်ရွက်ရန် အသုံးပြုသည်။
a=10
b=5
c=a+b #Addition (Python, + ဖြည့်စွက်အော်ပရေတာဖြစ်ပါတယ်။ တန်ဖိုးနှစ်ခုကိုထည့်ရန်အသုံးပြုသည်။)
d=a-b #Subtraction (Python, - အဆိုပါနုတ်အော်ပရေတာဖြစ်ပါတယ်။ ၎င်းကိုပထမတန်ဖိုးမှဒုတိယတန်ဖိုးကိုနုတ်ရန်အသုံးပြုသည်။)
e=a*b #Multiplication (Python, * မြှောက်အော်ပရေတာဖြစ်ပါတယ်။ ၎င်းသည်တန်ဖိုးနှစ်ခု၏ထုတ်ကုန်ကိုရှာဖွေရန်အသုံးပြုသည်။)
f=a/b #Division (Python, / ဌာနခွဲအော်ပရေတာဖြစ်ပါတယ်။ ၎င်းကိုပထမ ဦး ဆုံးအော်ပရာကိုဒုတိယပိုင်းခွဲသောအခါ၎င်းကိုကိုးကားရန်အသုံးပြုသည်။)
g=a%b #Modulus (Python, % modulus အော်ပရေတာဖြစ်ပါတယ်။ရာခိုင်နှုန်များအတွက် အသုံးပြုသည် )
h=a**b #Exponentiation (Python, ** အဆိုပါ exponentiation အော်ပရေတာဖြစ်ပါတယ်။ ၂ ထပ် ကိန်းများ အတွက် အသုံးပြုသည်။)
i=a//b #Floor Division (python ,, //သည် အချိူးအတွက် သုံးသည်)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
#Comparison(relationship) Operators
#Comparison Operators များသည် သင်၏ codeများတွင် နှိုင်းယှဉ်မှုများကို ဆောင်ရွက်ရန် အသုံးပြုသည်။



print(a == b) #Equal
print(a != b) #Not Equal !
print(a > b)  #Greater Than
print(a < b)  #Less Than
print(a >= b) #Greater Than or Equal To
print(a <= b) #Less Than or Equal To

#Assignment Operators
#Assignment Operators များသည် သင်၏ codeများတွင် တန်ဖိုးများကို သတ်မှတ်ရန် အသုံးပြုသည်။
x = 10 #Assignment
x += 5 #Add and Assign
x -= 3 #Subtract and Assign
x *= 2 #Multiply and Assign
x /= 4 #Divide and Assign
x %= 3 #Modulus and Assign
x **= 2 #Exponentiation and Assign
x //= 2 #Floor Division and Assign
print(x)

#Logical Operators
#Logical Operators များသည် သင်၏ codeများတွင် လိုဂျစ်စ်ဆိုင်ရာ လုပ်ဆောင်ချက်များကို ဆောင်ရွက်ရန် အသုံးပြုသည်။
#တနည်း Boolean အသုံးအနှုန်းများကိုပေါင်းစပ်ရန်အသုံးပြုသည်
p = True        
q = False
print(p and q) #Logical AND ()
print(p or q)  #Logical OR
print(not p)   #Logical NOT

#Bitwise Operators      
#Bitwise Operators များသည် သင်၏ codeများတွင် ဘစ်စိုင် လုပ်ဆောင်ချက်များကို ဆောင်ရွက်ရန် အသုံးပြုသည်။
m = 10  # In binary: 1010
n = 4   # In binary: 0100
print(m & n)  #Bitwise AND
print(m | n)  #Bitwise OR
print(m ^ n)  #Bitwise XOR
print(~m)     #Bitwise NOT

#Membership Operators
#Membership Operators များသည် သင်၏ codeများတွင် အဖွဲ့ဝင်မှု စစ်ဆေးမှုများကို ဆောင်ရွက်ရန် အသုံးပြုသည်။   
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      #Membership IN
print(6 not in my_list)  #Membership NOT IN

#Identity Operators
#Identity Operators များသည် သင်၏ codeများတွင် အထူးသတ်မှတ်မှု စစ်ဆေးမှုများကို ဆောင်ရွက်ရန် အသုံးပြုသည်။
a = 50
b = 50  
print(a is b)      #Identity IS
print(a is not b)  #Identity IS NOT

#Python Operators များကို သင်၏ ကုဒ်များတွင် အမျိုးအစားအလိုက် အသုံးပြုခြင်းဖြင့် သင်၏ ကုဒ်များကို ပိုမို ထိရောက်စွာ ရေးသားနိုင်ပါသည်။

