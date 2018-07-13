import random
i = 0
def set_answer():
    while i < 4:
        correct_answer[i] = random.randint(0, 10)
        i += 1 
        return correct_answer[i]
correct_answer = 
answer = input("Enetr a number(4-digit): ")

def judge_guess(*args):
