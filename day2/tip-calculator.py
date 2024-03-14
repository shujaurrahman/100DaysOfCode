print("Welcome to tip-calculator!")
totalBill=float(input("What was the total bill? "))
tipPaid=int(input("How much tip would you like to give in percentage ? 10,12 or 15 "))
peopleSplitting=float(input("How many people to split the bill? "))
tipPaid=tipPaid/100*totalBill
billAfterTip=totalBill+tipPaid
billPerHead=billAfterTip/peopleSplitting
billPerHead=round(billPerHead,2)
billPerHead="{:.2f}".format(billPerHead)
print(f"Each person should pay : {billPerHead} Rupees")