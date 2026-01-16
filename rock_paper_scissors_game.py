import random
a=random.randint(1,3)
b=int(input("press 1 for rock 2 for paper and 3 for scissor...."))
if b==1:
    print("You choose rock\n")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif b==2:
    print("You choose paper\n")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
elif b==3:
    print("You choose scissor\n")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Enter the valid input")
if a==1:
    print("Computer choose rock\n")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif a==2:
    print("Computer choose paper\n")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
elif a==3:
    print("Computer choose scissor\n")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("An error occured!")
if a==b:
    print("IT'S A TIE")
elif a==1 and b==2:
    print("YOU WON")
elif a==1 and b==3:
    print("COMPUTER WON")
elif a==2 and b==1:
    print("COMPUTER WON")
elif a==2 and b==3:
    print("YOU WON")
elif a==3 and b==1:
    print("YOU WON")
elif a==3 and b==2:
    print("COMPUTER WON")
else:
    print("An error occured")






