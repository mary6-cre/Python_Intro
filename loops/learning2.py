tweets = [
     "I LOVE MACHINE LEARNING**" ,
     " THE PHONE STOORAGE IS ALMOST FULL ##" ,
     "AM ABOUT TO GO HOME ##" ,

]

def clean_text(text):
    text= text.lower().strip("#*").strip().capitalize().replace("oo", "o")
    return text

for tweet in tweets:
    cleanTweet = clean_text(tweet)
    print(cleanTweet)
