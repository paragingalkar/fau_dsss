import random


def get_number(min, max):
    """
    Returns a random integer.
    """
    return random.randint(min, max)


def select_operator():
    """
    Returns a random operator from 3 choices.
    """
    return random.choice(['+', '-', '*'])


def do_math(num1, num2, operator):
    """
    Calculates a mathematical expression and return the equation and the answer
    """
    equation = f"{num1} {operator} {num2}"
    if operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    else:
        ans = num1 * num2
    return equation, ans

def math_quiz():
    """
    Main function containing the code for the quiz
    """
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = get_number(1, 10); n2 = get_number(1, 55); o = select_operator()

        PROBLEM, ANSWER = do_math(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        valid_input = False
        while not valid_input:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                valid_input = True
            except ValueError:
                print("Please enter an integer")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    """
    The main_quiz function will run only when this file is run and not when imported.
    """
    math_quiz()
