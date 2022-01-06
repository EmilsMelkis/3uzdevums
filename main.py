terifs=float(input("ievadi liguma terminu:"))
sk1=int(input("ievadi ieprieksejo liguma terminu:"))
sk2=int(input("ievadi esoso liguma terminu:"))
kwh=sk2-sk1
def maksa(ter,kwh):
 if ter==1:
   summa=0.20159*kwh
 elif ter==2:
   summa=0.16961*kwh
 elif ter==3:
   summa=0.16427*kwh
 elif ter==4:
   summa=0.15964*kwh
 else:
   print("ir ievadits nepareizs liguma termins")
  print(summa)

  maksa(ter, kwh)