import random

options = ["אבן", "נייר", "מספריים"]

def check_winner(player, computer):
    if player == computer:
        return "תיקו!"
    elif (player == "אבן" and computer == "מספריים") or \
         (player == "נייר" and computer == "אבן") or \
         (player == "מספריים" and computer == "נייר"):
        return "ניצחת!"
    else:
        return "הפסדת..."

def main():
    print("ברוך הבא לאבן, נייר ומספריים!")
    print("האפשרויות הן: אבן,נייר,מספריים")
    player_choice = input("בחר: אבן, נייר או מספריים: ").strip()

    if player_choice not in options:
        print("בחירה לא חוקית.")
        return

    computer_choice = random.choice(options)
    print(f"המחשב בחר: {computer_choice}")

    result = check_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
