import random

random.seed()
acceptable_inputs = ["0", "1"]
full_input = ""
full_next_input = ""
triad_numbers = ["000", "001", "010", "011", "100", "101", "110", "111"]
triad_results = {}
original_triad = str(random.randint(0, 1)) + str(random.randint(0, 1)) + str(random.randint(0, 1))
prophecy = original_triad
full_list = []
full_next_list = []
capital = 1000


def main():
    global full_input, full_next_input, full_list, full_next_list, prophecy
    print("Please give AI some data to learn...\nThe current data length is 0, 100 symbols left")
    while len(full_input) < 100:
        print("Print a random string containing 0 or 1:\n")
        user_input = input()
        split_input = list(user_input)
        for i in split_input:
            if i not in acceptable_inputs:
                split_input.remove(i)
            else:
                full_input += i
        if len(full_input) < 100:
            print(f"Current data length is {len(full_input)}, {100 - len(full_input)} symbols left")
    print(f"Final data string:\n{full_input}\n")
    full_list = list(full_input)
    for number in triad_numbers:
        join_the_triad(number, full_list)
    print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
    print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
    while True:
        full_next_input = ""
        full_next_list = []
        prophecy = original_triad
        print("\nPrint a random string containing 0 or 1:")
        user_next_input = input()
        if user_next_input == "enough":
            print("Game over!")
            exit()
        split_next_input = list(user_next_input)
        for i in split_next_input:
            if i not in acceptable_inputs:
                split_next_input.remove(i)
            else:
                full_next_input += i
        full_next_list = list(full_next_input)
        if not full_next_list:
            continue
        mystic_greg()
        print(f"prediction:\n{prophecy}\n")
        scores_on_the_doors()
        for number in triad_numbers:
            join_the_triad(number, full_next_list)


def join_the_triad(triad_number, list):
    counts_of_0 = 0
    counts_of_1 = 0
    for index in range(len(full_list) - 3):
        if list[index] + list[index + 1] + list[index + 2] == triad_number:
            if list[index + 3] == "0":
                counts_of_0 += 1
            else:
                counts_of_1 += 1
    triad_results[triad_number] = [counts_of_0, counts_of_1]


def mystic_greg():
    global prophecy
    for index in range(len(full_next_list) - 3):
        triad = full_next_list[index] + full_next_list[index + 1] + full_next_list[index + 2]
        triad_list = triad_results[triad]
        if triad_list[0] > triad_list[1]:
            prediction = "0"
        elif triad_list[0] < triad_list[1]:
            prediction = "1"
        else:
            prediction = str(random.randint(0, 1))
        prophecy += prediction


def scores_on_the_doors():
    global capital
    correct_guesses = 0
    prophecy_list = list(prophecy)
    for index in range(len(full_next_input) - 3):
        if full_next_list[index + 3] == prophecy_list[index + 3]:
            correct_guesses += 1
    print(f"Computer guessed right {correct_guesses} out of {len(full_next_input) - 3} symbols "
          f"({round((correct_guesses / (len(full_next_input) - 3) * 100), 2)} %)")
    capital = capital - correct_guesses + (len(full_next_input) - 3 - correct_guesses)
    print(f"Your capital is now ${capital}")


main()
