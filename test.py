import time
import random
from collections import Counter
import threading

class TypingTest:
    def __init__(self, words_to_type):
        self.words_to_type = words_to_type
        self.errors = 0

    def display_test(self):
        print("Get ready! The test will start in 10 seconds.")
        self.countdown_timer(10)
        print("\nType the following words and press Enter:")
        print(' '.join(self.words_to_type))

    def countdown_timer(self, seconds):
        for i in range(seconds, 0, -1):
            print(f"\rStarting in {i} seconds...", end="")
            time.sleep(1)
        print("\rStarting now!                                ")

    def take_test(self):
        user_input = input()
        user_words = user_input.split()

        if user_words != self.words_to_type:
            self.errors += sum((Counter(self.words_to_type) - Counter(user_words)).values())

    def calculate_wpm(self, elapsed_time):
        total_words = len(self.words_to_type)
        accuracy = 1 - (self.errors / total_words)
        typing_speed = (total_words / elapsed_time) * 60 * accuracy
        return typing_speed

if __name__ == "__main__":
    words_to_type = ["the", "be", "of", "and", "a", "to", "in", "he", "have", "it", "that", "for", "they", "with", 
                     "as", "not", "on", "she", "at", "by", "this", "we", "you", "do", "but"]

    typing_test = TypingTest(words_to_type)
    typing_test.display_test()

    start_time = time.time()
    typing_test.take_test()
    elapsed_time = time.time() - start_time

    typing_speed = typing_test.calculate_wpm(elapsed_time)

    print(f"\nElapsed Time: {elapsed_time:.2f} seconds")
    print(f"Typing Speed: {typing_speed:.2f} WPM")
