import os
import json
import random


def check_for_kanji_json() -> bool:
    if not os.path.exists("kanjis.json"):
        print("There does not seem to be an existing kanji JSON file")
        print("Do you want to create a new kanji JSON file?")
        answer = input("[Y/n]\n> ")
        if answer.lower() == "y":
            print("Creating kanji JSON file...")
            create_kanji_json()
        else:
            print("\nYou can't use this program without creating a new kanji JSON file")
            print("Restart the program to try again.")
            return False
    else:
        add_kanji = input("A kanji file exists. Do you want to add new kanji? [Y/n]\n> ")
        if add_kanji.lower() == "y":
            new_data = get_kanji_and_meaning()
            add_kanji_json(new_data)
        else:
            return True
    return True


def add_kanji_json(new_data: dict):
    with (open("kanjis.json", 'r+', encoding='utf-8', errors='ignore') as file):
        # Load the existing JSON data into a Python dictionary
        data = json.load(file)
        data.update(new_data)
        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Write the updated data back to the JSON file
        json.dump(data, file, indent=4)


def get_kanji_and_meaning() -> dict:
    data = {}
    number_of_kanji = input("How many kanjis do you want to add?\n> ")

    for i in range(5):
        if not number_of_kanji.isnumeric():
            print("You must enter a number")
            print("Please try again")
            number_of_kanji = input("How many kanjis do you want to add?\n> ")

    if not number_of_kanji.isnumeric():
        print("You still did not enter a number. This program will now terminate")
        print("\nThank you for using Kanji Learner")
        input("\nPress Enter to close...\n>")
        exit()

    for i in range(int(number_of_kanji)):
        kanji = input("Please put in the kanji you want to add and press enter\n> ")
        meaning = input("Please put in the meaning you want to add and press enter\n> ")
        data[kanji] = meaning
    return data


def create_kanji_json():
    with open("kanjis.json", "w", encoding='utf-8', errors='ignore') as kanji_json:
        new_data = get_kanji_and_meaning()
        json.dump(new_data, kanji_json, indent=4)


def read_kanji_json() -> dict:
    return json.load(open("kanjis.json", encoding='utf-8', errors='ignore'))


def create_quiz_list(kanji_dict: dict) -> list:
    keys_list = list(kanji_dict.keys())
    number_of_kanji = len(keys_list) if len(keys_list) < 10 else 10
    rand_keys_list = random.sample(keys_list, number_of_kanji)
    return rand_keys_list


def quiz_the_user():
    kanji_dict = read_kanji_json()
    rand_keys_list = create_quiz_list(kanji_dict)

    print("What do these kanji mean?\n")
    for index, keys in enumerate(rand_keys_list):
        print(f"{index}. {keys}")

    input("\nPress Enter to continue...\n>")
    print("The following are the meanings of the kanji:\n")
    for index, keys in enumerate(rand_keys_list):
        print(f"{index}. {kanji_dict[keys]}")


if __name__ == '__main__':
    print("Welcome to your kanji learning app")
    if check_for_kanji_json():
        quiz_the_user()
    print("\nThank you for using Kanji Learner")
    input("\nPress Enter to close...\n>")
