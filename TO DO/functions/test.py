import math

def makeChange(Amount):
      try:
          NewAmount =math.modf(Amount)
          #dec first, doller second
          b=int(Amount[1]) # b = bills
            #bills
          hundred = b//100.00
          b = b%100.00
          fifty  = b//50.00
          b = b%50.00
          twenty = b//20.00
          b = b%20.00
          ten  = b//10.00
          b = b%10.00
          five  = b//5.00
          b = b%5.00
          one  = b//1.00
          b = b%1.00

          #coins
          c=float(NewAmount[0])
          quarters = c// 0.25
          c = c%0.25
          dimes = c//0.10
          c = c%0.10
          nickels = c//0.05 
          c = c%0.05
          pennies = c//0.01
          c =c%0.05

          #printing out of the values:

          Dvalues = f" the change is:\n DOllARS:\n $1: {one}\n $5: {five}\n $10: {ten}\n $20: {twenty}\n $50: {fifty}\n $100: {hundred}"
          Cvalues =f"CENTS:\n $0.01: {pennies}\n $0.05: {nickels}\n $0.10: {dimes}\n $0.25: {quarters}"

          results = Dvalues + "\n" + Cvalues
          return results
      except:
         error = input("an error has occoured counting\n are you sure you entered a string?\n try again? (Y or N)")
         if(error=="Y"):
             try:
              makeChange()
             except:
                 print("exit code 1, a fatal error has occurred")
         else:
             quit()


def getChange(Owed, Paid):
    try:
          TOTALOWED = Paid-Owed
          NewAmount =math.modf(TOTALOWED)
          #dec first, doller second
          b=int(Paid[1]) # b = bills
            #bills
          hundred = b//100.00
          b = b%100.00
          fifty  = b//50.00
          b = b%50.00
          twenty = b//20.00
          b = b%20.00
          ten  = b//10.00
          b = b%10.00
          five  = b//5.00
          b = b%5.00
          one  = b//1.00
          b = b%1.00

          #coins
          c=float(NewAmount[0])
          quarters = c// 0.25
          c = c%0.25
          dimes = c//0.10
          c = c%0.10
          nickels = c//0.05 
          c = c%0.05
          pennies = c//0.01
          c =c%0.05
          Dvalues = f" the change is:\n DOllARS:\n $1: {one}\n $5: {five}\n $10: {ten}\n $20: {twenty}\n $50: {fifty}\n $100: {hundred}"
          Cvalues =f"CENTS:\n $0.01: {pennies}\n $0.05: {nickels}\n $0.10: {dimes}\n $0.25: {quarters}"
          changegiven = Dvalues + "\n" + Cvalues
          return "we Owe you ${TOTALTOTALOWED}\n" + changegiven 
    except:
       error = input("an error has occoured counting\n are you sure you entered a string?\n try again? (Y or N)")
    if(error=="Y"):
     try:
       getChange()
     except:
      print("exit code 1, a fatal error has occurred")
     else:
      quit()
