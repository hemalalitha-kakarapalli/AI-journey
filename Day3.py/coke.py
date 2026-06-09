amount_Due=50
while amount_Due>0:
 user = int(input("enter coin:"))
 rem = int(amount_Due)-user
 if user in [25,10,5]:
      if  rem <= 0:
        print(f"Change Owed:{abs(rem)}")
        break
      else:
        print(f"amt due:{rem}")
        amount_Due=rem
 else:
     print(f"amt due:{amount_Due}")
 
 
