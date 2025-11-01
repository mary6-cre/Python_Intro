def main():
    difficulty= input("Difficult  or casual? ")
    players= input("Single or Multiplayer? ")

    if difficulty== "Difficult" :
        if players == "Single":
            recommend("candy crush")
        elif players == "Multiplayer":
            recommend("poker")
        else:
            print("Enter valid number of players ")
    elif difficulty== "casual" :
        if players == "Single":
            recommend("Temple run")
        elif players == "Multiplayer":
            recommend("Min miltia")
        else:
            print("Enter valid number of players ")
    else:
            print("Enter a valid difficulty " )
    
            
def recommend(game):
    print("you might like ",game)
main()
