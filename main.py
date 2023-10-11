# this program quizzes the user on the capital cities of countries in europe

import random
import time
from dict_capitals_and_countries import countries_and_capitals

def select_random_country(used_countries):
    unused_countries = [c for c in countries_and_capitals.keys() if c not in used_countries]
    if unused_countries:
        return random.choice(unused_countries)
    else:
        return None

def ask_question(country, capital):
    print(f"What is the capital of {country}? ")
    start_time = time.time()
    user_answer = input().strip()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return user_answer, elapsed_time

def main():
    while True:
        used_countries = []
        score = 0
        total_questions = 5

        print("Welcome to a capital cities of Europe Quiz!")

        for _ in range(total_questions):
            country = select_random_country(used_countries)
            if country is None:
                print("You've named all the countries")
                break
            used_countries.append(country)

            capital = countries_and_capitals[country]
            user_answer, elapsed_time = ask_question(country, capital)

            if user_answer.lower() == capital.lower():
                print("Correct!")
                score += 1
                print(f"Time taken: {elapsed_time: .2f} seconds")
            else:
                print(f"Sorry, the correct answer is {capital}.")

        print(f"Your final score is {score}/{total_questions}.")

        play_again = input("Would you like to play again? (yes/no)")
        if play_again != "yes":
            print("Bye!")
            break

if __name__ == "__main__":
    main()