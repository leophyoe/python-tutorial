'''
Loop

loop ဆို တာ "တိုင်ပတ်တယ်" ဆိုတယ်မြန်မာစကားနဲ့တူတယ် loop  တွေက အခြအနေတစ်ခုကို ကြိမ်ဖန်များစွာလုပ်တယ် သဘောပါ။ python programming language မှာ loop (၃)မျိူးရှိတယ်
while loop
for loop
'''
#while loop 
#while loop ဆိုတာ condition တစ်ခု မှန်ကန် နေစဥ်အတွင်း ထက်ခါထက်ခါလုပ်ဆောင်းပေးခြင်း။
#while loop တွင် အခြအနတစ်ခုကိုစစ်ဆေးရာမှာ Comparison (Relational) Operatorများကို အသုံးပြုနိုင်ပါတယ်

a=0
while a<20:       #aသည် 20ထက်ကြီး စဉ်အတွင်းအလုပ်လုပ်မယ်(Comparison (Relational) Operatorများအသုံပြုသည်
  print(a)             # aကို printထုတ်မယ်
  a+=1                #aတန်ဖိုးကို ၁ ထက်ပေါင်းသွားမယ်(ဒီ code မပါရင် ၀ တွေကြီးဘဲထုတ်ပေးမှာပါ)

  #break Statement with while loop

 #break statement ဆိုတာ while loop မှာ if statementကို အသုံပြု့ပြီး statement မှန်လျှင် loop ကို ရပ်တန့်မှာ ဖြစ်ပါတယ်


a=0
while a<20:      #aသည် 20ထက်ကြီး စဉ်အတွင်းအလုပ်လုပ်မယ်(Comparison (Relational) Operatorများအသုံပြုသည်
    print(a)            # aကို printထုတ်မယ်
    a+=1               #aတန်ဖိုးကို ၁ ထက်ပေါင်းသွားမယ်(ဒီ code မပါရင် ၀ တွေကြီးဘဲထုတ်ပေးမှာပါ)    
    if (a==10):       # "အကယ်၍" aသည် အမှန်တကယ် ၁၀နှင့်ညီပါက break (ရပ်ပါ)
        break            

#Else statement with while loop

#while loop ကအခြအနေတစ်ခု မှန်ကန် နေစဥ်အတွင်း ထက်ခါထက်ခါလုပ်ဆောင်းပေးပြီး မမှန်တယ်print တစ်ခုကို ထုတ်ပေးခြင်တယ် ဆိုရင်else statement ကို အသုံးပြုပါတယ်(condition က မမှန်းတော့ဘူးဆိုရင် else အောက်ကcode ကို run ပါတယ်)
a=0
while a<10:
    print(a)
    a+=1
else:
    print(a,"is not less than 10")
