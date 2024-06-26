# brain_games/engine.py
import prompt

MAX_ROUND = 3


def run_game(game_module):
    user_name = prompt.string(
        'Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {user_name}\n{game_module.INSTRUCTION}")

    for _ in range(MAX_ROUND):
        question, correct_answer = game_module.get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            return

    print(f'Congratulations, {user_name}!')
