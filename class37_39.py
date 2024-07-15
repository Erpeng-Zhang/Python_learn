'''
class from Bro Code
https://youtu.be/XKHEtdqhLK8?si=L-c30rp08X7KOpD9
# 37modules 模块
# 38rock,paper,scissors game 石头剪子布游戏
# 39quiz game 小测验游戏
'''


# # class37: module = a file containing Python code. may contain functions, classes, etc.
# #                   used with modular programming, which is to separate a program into separate parts

# import message as msg
# from message import *
# from message import hello,bye

# msg.hello()
# msg.bye()
# hello()
# bye()

# help("modules") # 查看模块的帮助文档

# # class38 rock,paper,scissors game 石头剪子布游戏
# import random
# def compare(choice1, choice2):
#     if choice1 == choice2:
#         return "It's a tie!"
#     elif choice1 == "rock":
#         if choice2 == "scissors":
#             return "Rock smashes scissors! You win!"
#         else:
#             return "Paper covers rock! You lose."
#     elif choice1 == "paper":
#         if choice2 == "rock":
#             return "Paper covers rock! You win!"
#         else:
#             return "Scissors cuts paper! You lose."
#     elif choice1 == "scissors":
#         if choice2 == "paper":
#             return "Scissors cuts paper! You win!"
#         else:
#             return "Rock smashes scissors! You lose."

# while True:
#     choices = ["rock", "paper", "scissors"]

#     computer = random.choice(choices)
#     player = None

#     while player not in choices:
#         player = input("rock, paper, or scissors? ").lower()

#         print("computer:", computer)
#         print("player:", player)
#         print(compare(player, computer))
    
#     play_again = input("Play again? (yes/no): ").lower()
#     if play_again == "no":
#         break
    

#  class39: quiz game 小测验游戏
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(anwser, guess):
    if anwser == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print("----------------")
    print("Results:")
    print("----------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = (correct_guesses / len(questions)) * 100
    print("Your score: ", str(score) + "%")

def play_again():
    respond = input("Do you want to play again? (yes or no): ").lower()
    if respond == "yes":
        print("let's play again!")
        return True
    elif respond == "no":
        print("Thanks for playing!")
        return False
    else:
        play_again()

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "A",
    "Python is tributed to which comedy group?: ": "B",
    "Is the Earth round?: ": "B",
    "Is the Sun hot?: ": "B"
}

options = [["A.Guido van Rossum", "B.Elon Musk", "C.Bill Gates", "D.Mark Zuckerberg"],
              ["A.1989", "B.1991", "C.2000", "D.2016"],
              ["A.Lonely Island", "B.Monty Python", "C.Smosh", "D.Snake"],
              ["A.No", "B.Yes", "C.IDK", "D.Maybe"],
              ["A.No", "B.Yes", "C.IDK", "D.Maybe"]]
new_game()
while play_again():
    new_game()

