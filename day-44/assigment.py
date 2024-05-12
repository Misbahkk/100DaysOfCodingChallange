amoun = int(input("Enter a amout: "))

deposit=0
fiveTH=0
TH=0
fiveHun = 0
Hun = 0
fivty=0
twenty=0
ten =0

while True:
    if amoun >= 5000:
        deposit += 5000
        amoun=amoun-5000
        fiveTH+=1
    elif amoun >=1000:
        deposit+=1000
        amoun=amoun-1000
        TH+=1
    elif amoun >=500:
        deposit+=500
        amoun=amoun-500
        fiveHun+=1
    elif amoun >=100:
        deposit+=100
        amoun=amoun-100
        Hun+=1
    elif amoun>=50:
        deposit+=50
        amoun=amoun-50
        fivty+=1
    elif amoun>=20:
        deposit+=20
        amoun=amoun-20
        twenty+=1
    elif amoun>=10:
        deposit+=10
        amoun=amoun-10
        ten+=1


    else:
        break



print(deposit)
if fiveTH>0:
    print("5000 ",fiveTH)
if TH>0:
    print("1000 ",TH)
if fiveHun>0:
    print("500 ",fiveHun)
if Hun>0:
    print("100 ",Hun)
if fivty>0:
    print("50",fivty)
if twenty>0:
    print("20 ",twenty)
if ten>0:
    print("10 ",ten)