
Auction_members = {}
choice=""

def clear_screen():
    print("\n"*100)

def auction ():
    name = input("Name :")
    if name in Auction_members :
        print("Name already Exist !")
    else:
        price = float(input("Your Bid : $"))
        Auction_members[name] = price
def result ():
    if Auction_members == False:
        print("No BIDS yet !")
    else:
        winner=max(Auction_members, key = Auction_members.get)
        print(f"The Bid goes to :{winner} for ${Auction_members[winner]}")

while True:
    choice=input("Any Bids ? ('Yes' or 'No' ) :").lower()
    if choice == "yes":
        auction()
        clear_screen()
    elif choice == "no":
        result()
        break
    else:
        print("Not a Valid Comment !")