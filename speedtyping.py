import time
import random

def calculate_words_per_minute(text, elapsed_time):
    words = len(text.split())
    minutes = elapsed_time / 60
    words_per_minute = words / minutes
    return words_per_minute

def run_speed_typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    start_time = time.time()
    texts = [
        'The quick brown fox jumps over the lazy dog.',
        'the five boxing wizards jump quickly.',
        'Jackdaws love my big sphinx of quartz.'
    ]
    # Chosing one of the texts randomly with the choice function
    text = random.choice(texts).lower()
    print(f"\nType the following sentence:\n{text}\n")
    user_input = input("-> ")
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    words_per_minute = calculate_words_per_minute(user_input, elapsed_time)
    if (user_input == text):
        print(f"\nTime elapsed: {elapsed_time} seconds")
        print(f"Words per minute: {words_per_minute:.2f}")
    else:
        count = 0
        for i in range(len(user_input.split())):
            if text.split()[i] != user_input.split()[i]:
               count += 1
               user_input.split().pop(i)
        words_per_minute = calculate_words_per_minute(user_input, elapsed_time)
        print(f"\nTime elapsed: {elapsed_time} seconds")
        print(f"Words per minute: {words_per_minute:.2f}")
        print(f"Number of words incorrect are : {count}")

run_speed_typing_test()