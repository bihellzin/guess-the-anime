from requests import get
import random


def get_anime() -> dict:
    anime_id = random.randint(1, 46491)
    anime = get("https://api.jikan.moe/v3/anime/%d" % anime_id)

    while anime.status_code != 200:
        anime_id = random.randint(1, 46491)
        anime = get("https://api.jikan.moe/v3/anime/%d" % anime_id)

    return anime.json()


def get_number_of_questions() -> int:
    try:
        num = int(input("How many questions ?\n"))

    except ValueError:
        num = "a"
        while not num.isdecimal():
            print("Only integer numbers, stupid weeb")
            num = input("How many questions ?\n")

    finally:
        return num


def print_information(anime_json: dict):
    if anime_json["synopsis"]:
        print("Synopsis:", anime_json["synopsis"].replace(anime_json["title"], "ANIME_NAME"), end="\n\n")
    else:
        print("No synopsis provided")
    print("Native title:", anime_json["title_japanese"], end="\n\n")


def list_of_correct_answers(anime_json: dict) -> list:
    titles = []
    titles.append(remove_special_characters(anime_json["title"]))

    if anime_json["title_english"]:
        titles.append(remove_special_characters(anime_json["title_english"]))

    if anime_json["title_synonyms"]:
        for title in anime_json["title_synonyms"]:
            titles.append(remove_special_characters(title))

    return titles


def remove_special_characters(title: str) -> str:
    new_title = ""

    for char in title:
        if char != "'" or char != "\"" or char != "?" or char != "-" or char != "!": 
            new_title += char

    return new_title.lower()


if __name__ == '__main__':
    num_questions = get_number_of_questions()
    cont = 0
    correct_answers = 0
    print("\n")
    
    while cont < num_questions:
        anime = get_anime()
        print_information(anime)
        
        titles = list_of_correct_answers(anime)
        title = remove_special_characters(input("What's the name of this anime ?\n"))
        print("\n")
        if title in titles:
            correct_answers += 1
            print("CORRECT, F*CKING WEEB")
            print(correct_answers, "correct answers\n")
        
        print("+--------------------------------+\n")
        cont += 1
