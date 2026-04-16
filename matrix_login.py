import time
import random
import sys
import getpass

def glitch(text):
    """Tiny fake glitch effect"""
    symbols = ["#", "%", "@", "█", "▒", "░", "⟟"]
    return "".join(random.choice(symbols) if random.random() < 0.1 else c for c in text)

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# MATRIX INTRO
print("\n")
slow_print("INITIALIZING SYSTEM...")
time.sleep(1)

for _ in range(3):
    slow_print(glitch("ACCESSING MAINFRAME..."))
    time.sleep(0.5)

slow_print("\nWELCOME, USER")
slow_print("SECURE NODE: ████████")
print("\n")

# credentials
correct_username = "admin"
correct_password = "1234"
security_answer = "blue"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input(">> USER ID: ")
    password = getpass.getpass(">> ACCESS KEY: ")

    slow_print("VERIFYING...", 0.05)
    time.sleep(1)

    if username == correct_username and password == correct_password:
        slow_print("\nACCESS NODE MATCHED")
        time.sleep(1)

        answer = input(">> SECURITY PROTOCOL (favorite color): ").lower()

        if answer == security_answer:
            slow_print("\n✔ AUTHORIZATION COMPLETE")
            slow_print("WELCOME BACK, OPERATOR.")
            slow_print("ENTERING SYSTEM...\n")
        else:
            slow_print("\n✖ SECONDARY PROTOCOL FAILED")
            slow_print("ACCESS DENIED.")
        break

    else:
        attempts += 1
        remaining = max_attempts - attempts

        slow_print("\n✖ NODE REJECTED")

        if remaining > 0:
            slow_print(f"RETRY SEQUENCE AVAILABLE: {remaining}\n")
        else:
            slow_print("\n🚫 SYSTEM LOCKED")
            slow_print("TRACE INITIATED...")
            slow_print("CONNECTION TERMINATED.\n")
