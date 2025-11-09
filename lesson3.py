'''
#python Comments
#Comments များသည် သင်၏ code များတွင် မှတ်ချက်များ ထည့်သွင်းရန် အသုံးပြုသည်။မှတ်ချက်များသည်ကုဒ်၏ဖတ်နိုင်မှုကိုတိုးမြှင့်ပေးပြီးပရိုဂရမ်မာများအားကုဒ်ကိုသေချာစွာနားလည်ရန်ကူညီသည်။ Python တွင် Comments များကို # သင်္ကေတဖြင့် စတင်သည်။
#Python – တွင်comments သုံးမျိုးရှိသည်
Single line Comments
Multiline Comments
Docstring Comments

Python single-line မှတ်ချက်သည် hashtag သင်္ကေတ (#) ဖြင့်အဖြူရောင်နေရာမရှိဘဲလိုင်း၏အဆုံးအထိကြာသည်။ အကယ်၍ မှတ်ချက်သည်လိုင်းတစ်ခုထက်ကျော်လွန်ပါက hashtag ကိုနောက်လိုင်းပေါ်တွင်တင်ပြီးမှတ်ချက်ကိုဆက်လုပ်ပါ။ Python ၏ single-line မှတ်ချက်များသည် variable များ၊ function ကြေငြာချက်များနှင့်အသုံးအနှုန်းများအတွက်တိုတောင်းသောရှင်းလင်းချက်များကိုထောက်ပံ့ရန်အတွက်အသုံးဝင်သည်။ တစ်ခုတည်းလိုင်းမှတ်ချက်သရုပ်ပြအောက်ပါကုဒ် snippet ကိုကြည့်ပါ:
Python တွင် Multi-line Comments များကို သို့မဟုတ်  သင်္ကေတများဖြင့် ဖုံးအုပ်နိုင်သည်။

eg.
#This is a single-line comment  


Multiline Comments

Python သည်ရွေးစရာကိုမပေးပါ multiline မှတ်ချက်များ။ သို့သော်ကျွန်ုပ်တို့သည် multiline မှတ်ချက်များကိုရေးသားနိုင်သည့်နည်းလမ်းအမျိုးမျိုးရှိသည်။

Multiple Hashtags (#) ကိုအသုံးပြုခြင်း
Python တွင် multiline မှတ်ချက်များကိုရေးသားရန်ကျွန်ုပ်တို့ hashtags (#) မျိုးစုံလုပ်နိုင်သည်။ လိုင်းတစ်ခုစီကို single-line comment အဖြစ်သတ်မှတ်လိမ့်မည်။


Docstring Comments
Python docstring function ကိုပြီးနောက်ချက်ချင်းပေါ်လာသောသုံးဆကိုးကားနှင့်အတူ string ကိုစာတတ်မြောက်သည်။၎င်းကို Python module များ၊ လုပ်ဆောင်ချက်များ၊ အတန်းများနှင့်နည်းလမ်းများဖြင့်ရေးသားထားသောစာရွက်စာတမ်းများကိုတွဲဖက်အသုံးပြုသည်။ ၄ င်းတို့ကိုသူတို့ဘာလုပ်သည်ကိုဖော်ပြရန်လုပ်ဆောင်မှုများ၊ module များသို့မဟုတ်အတန်းများအောက်တွင်ထည့်သွင်းထားသည်။ Python တွင် docstring ကို __doc__ attribute မှတဆင့်ရရှိနိုင်သည်။



'''




#python input and output

#Python တွင် input() function ကို အသုံးပြု၍ Client (အသုံးပြုသူထံ) input များကို လက်ခံနိုင်သည်။
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, " + name + "! You are " + age + " years old.")
