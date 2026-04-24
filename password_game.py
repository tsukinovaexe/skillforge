teksti = "Welcome to my secret game"

yritykset = 3

print("Welcome to wordsearch game!")
print("Tip: Word is conncected to the game ;)")

while yritykset > 0:
  sana = input("Guess the word: ")

  sijainti = teksti.lower().find(sana.lower())

  if sijainti != -1:
    print(f"Correct! The word was found in {sijainti}")
    break
  else:
    yritykset -= 1
    print(f"Didn't find. Attempts left: {yritykset}")
  
   if yritykset == 0:
      print("You lost the game buddy")
      print("The text was:", teksti)
    
