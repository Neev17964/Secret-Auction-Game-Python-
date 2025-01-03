from random import choice as c
import time

print("\t\t\t  AUCTION!!")
Auction_Items = ['Lamborgini Luxury Car','Beach-Side Mansion','Mars Planet','Indo-Raptor Dinosaur','Private Island']
print(f"Today's Auction Item is {c(Auction_Items)}")

Auctioners = {

}


player1 = input("What is your Name? ")
bid_1 = int(input("What is your bid? "))
Auctioners[player1] = bid_1

while True:
    question = input("Are there any more Auctioners?(yes/no)")

    if(question == 'yes'):
            print("\n" * 100)
            user = input("What is your Name? ")
            bid = int(input("What is your bid? "))
            Auctioners[user] = bid
            
    elif(question == 'no'):
          print("Auction Ending")
          print("3")
          time.sleep(1)
          print("2")
          time.sleep(1)
          print("1")
          time.sleep(1)
          break

biddings_list = list(Auctioners.values())

max_value = biddings_list[0]
for i in biddings_list:
      if(i > max_value):
            max_value = i

reversed_Auctioners_dict = {}

for key, value in Auctioners.items():
      reversed_Auctioners_dict[value] = key

print(f"Congratulations {reversed_Auctioners_dict[max_value]} has won the Auction")