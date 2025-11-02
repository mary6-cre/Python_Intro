def main():
    difficulty= input("Difficult  or casual? ")
    if not (difficulty== "Difficult" or difficulty== "casual" ):
        print("Enter a valid difficulty " )
        return

    players= input("Single or Multiplayer? ")
    if not (players == "Single" or players == "Multiplayer"):
        print("Enter valid number of players ")
        return

    if difficulty== "Difficult" and players == "Single":
        recommend("candy crush")
    elif difficulty== "Difficult" and players =="Multiplayer":
        recommend("poker")
        
    elif difficulty== "casual" and players == "Single" :
        recommend("Temple run")
    else:
        recommend("Min miltia")
          
def recommend(game):
    print("you might like ",game)
main()
