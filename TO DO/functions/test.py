def makeChange(Amount):
          c=int(Amount) # c = change

          #coins
          quarters = c//0.25,
          c = c%0.25
          dimes = c//0.10,
          c = c%0.10
          nickels = c//0.05,
          c = c%0.05
          pennies = c//0.01,

          #bills
          hundred = c//100.00,
          c = c%100.00
          fifty  = c//50.00,
          c = c%50.00
          twenty = c//20.00,
          c = c%20.00
          ten  = c//10.00,
          c = c%10.00
          five  = c//5.00,
          c = c%5.00
          one  = c//1.00,
          c = c%1.00

          #printing out of the values:

          Dvalues = f" the change is:\n DOllARS:\n $1: {one}\n $5: {five}\n $10: {ten}\n $20: {twenty}\n $50: {fifty}\n $100: {hundred}"
          Cvalues =f"CENTS:\n $0.01: {pennies}\n $0.05: {nickels}\n $0.10: {dimes}\n 0.25 {quarters}"

          results = Dvalues + "\n" + Cvalues
    
          return results

makeChange()