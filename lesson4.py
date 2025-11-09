# Python Conditions and If statements
# Python တွင် Conditions များနှင့် If statements များကို အသုံးပြု၍ သတ်မှတ်ထားသော အခြေအနေများအရ ကုဒ်များကို အကောင်အထည်ဖော်နိုင်သည်။
#if statement ဆိုတာ if ရဲ အဓိပ္ပာယ်က "အကယ်၍"ပါ။  အကယ်၍conditionတစ်ခုစစ်ဆေးပြီးမှန်ရင် အဖြေတစ်ခုထုတ်ပေးပြီး/မှားရင်လည်မှားတယ် အဖြေတစ်ခုထုတ်ပေးတယ် ။python မှာ if statement ရေးတယ် ပုံစံ (၃)မျိုးရှိတယ်။
#1. if statement
#2. if...else statement
#3. if...elif...else statement      

#Python supports the usual logical conditions from mathematics:
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b   


age = 29
a="mgmg"
if age < 18:
    print("You are a minor.")   


if a=="mgmg":
    print("Hello mgmg!")
# if...else statement
# if...else statement ကို သင်သည် condition တစ်ခုစစ်ဆေးပြီးမှန်ရင် အဖြေတစ်ခုထုတ်ပေးပြီး/မှားရင်လည်မှားတယ် အဖြေတစ်ခုထုတ်ပေးရန် အသုံးပြု
#if...else statement ရေးပုံမှာ if statement နောက်မှာ else statement ကို ထည့်သွင်းရမည်။
b=20

if b<18:
    print("You are a true.")
else:
    print("You are a false.")
# if...elif...else statement
# if...elif...else statement ကို သင်သည် condition များစွာကို စစ်ဆေးပြီး အခြေအနေတစ်ခုနှင့် ကိုက်ညီသော အဖြေကို ထုတ်ပေးရန် အသုံးပြု
# if...elif...else statement ရေးပုံမှာ if statement နောက်မှာ elif statement များကို ထည့်သွင်းနိုင်ပြီး နောက်ဆုံးတွင် else statement ကို ထည့်သွင်းရမည်။  

z="aung"
if z=="mgmg":
    print("Hello mgmg!")
elif z=="aung":
    print("Hello aung!")
else:
    print("Hello error!")    


#if statement and input()
name = input("Enter your name: ")
if name == "mgmg":
    print("Welcome back, mgmg!")
else:
    print("Hello, " + name + "!")

