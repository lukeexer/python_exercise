import random

def get_user_input():
    input('What\'s your question?') or 'Will I be rich and famous?'

def get_answer_list():
    answers = list()
    answers.append('Yes')
    answers.append('No')
    answers.append('Maybe')
    answers.append('Ask again later.')
    return answers

def generate_answer(answer_list):
    index = random.randint(0, len(answer_list) - 1)
    return answer_list[index]

def display_answer():
    answer_list = get_answer_list()
    print(generate_answer(answer_list))

get_user_input()
display_answer()