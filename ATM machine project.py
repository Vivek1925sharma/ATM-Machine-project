print("Welcome to my Bank ATM")
balance=1000
chance=3
restart=("YES")
pin=1234
while chance>0:
  print("First enter your pin number=")
  n=int(input("Enter Pin number="))
  if n==pin:
    while restart not in ("NO,no"):
      print("What u want to do:\n")
      print("1.Check BAlance:\n")
      print("2.Pay in:\n")
      print("3.WithDraw:\n")
      print("4.Backout or Return:\n")
      option=int(input("Choose the Num above:"))
      if option==1:
        print("\nYour Avaiable balance is:",balance)
        restart=input("Would u like to go back?(YES/NO)")
        if restart in ("no","No"):
          print("Thank you")
          break
      elif option==2:
        add=int(input("\nHow much amount would like to add in your balace?"))
        add=balance+add
        print("Total amount is:",add)
        restart=input("Would u like to go back?(YES/NO)")
        if restart in ("no","No"):
          print("Thank you")
          break
      elif option==3:
        dec=int(input("\nHow much amount would like to withdrawl from your balace?"))
        dec=balance-dec
        print("Total Available balance is:",dec)
        restart=input("Would u like to go back?(YES/NO)")
        if restart in ("no","No"):
          print("Thank you")
          break
      elif option==4:
        print("Wait for a second to take your card\n")
        print("Thank for your service")
        break
  elif n!=pin:
    print("Incorrect Pin,please enter correct pin")
    chance=chance-1
    if chance==0:
      print("\nSorry no more tries")
      break