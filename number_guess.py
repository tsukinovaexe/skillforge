import random

print("🎲 Welcome to the Lucky Number Game!!")
print("I am thinking of a number between 1 and 10...")

secret_number = random.randint(1,10)
attempts = 0

while True:
  guess = input("Take a guess buddy: ")

  if not guess.isdigit():
    print("Please enter a number already")
    continue

  guess = int(guess)
  attempts += 1

  if guess < secret_number:
    print("📉 Nah, that's too low")
  elif guess > secret_number:
    print("📈 Toooo high")
  else:
    print(f"Correct! You got it in {attempts} tries")
    break
