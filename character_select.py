from random import randrange

characterInfo = {
    "Yun": ("I Youhou", "II Sourai Rengeki", "III Gen'ei Jin"),
    "Gouki": ("I Messatsu Gou Hadou", "II Messatsu Gou Shouryuu", "III Messatsu Gou Rasen"),
    "Remy": ("I Hunnu no Supernova", "II Vierge ni Ansoku O", "III Shoushin no Nocturne"),
    "Ryu": ("I Shinkuu Hadou Ken", "II Shin Shouryuu Ken", "III Denjin Hadou Ken"),
    "Urien": ("I Tyrant Punish", "II Jupiter Thunder", "III Aegis Reflector"),
    "Q": ("I Tosshin Oyobi Chishi Renzoku Dageki (Kari)", "II Fukubu Oyobi Koutoubu e no Tsuuda (Kari)", "III Bakuhatsu o Tomonau Dageki ya Hokaku (Kari)"),
    "Oro": ("I Kishin Riki", "II Yagyou Dama", "III Tengu Ishi"),
    "Necro": ("I Chou Denji Storm", "II Slam Dance", "III Electric Snake"),
    "Chun-Li": ("I Kikou Shou", "II Houyoku Sen", "III Tensei Ranka"),
    "Dudley": ("I Rocket Upper", "II Rolling Thunder", "III Corkscrew Blow"),
    "Ibuki": ("I Kasumi Suzaku", "II Yoroi Dooshi", "III Yami Shigure"),
    "Makoto": ("I Seichuusen Godan-zuki", "II Abare Tosanami Kudaki", "III Tanden Renki: Seme no Kata"),
    "Elena": ("I Spinning Beat", "II Brave Dance", "III Healing"),
    "Sean": ("I Hadou Burst", "II Shouryuu Cannon", "III Hyper Tornado"),
    "Twelve": ("I X.N.D.L.", "II X.F.L.A.T.", "III X.C.O.P.Y."),
    "Hugo": ("I Gigas Breaker", "II Megaton Press", "III Hammer Mountain"),
    "Alex": ("I Hyper Bomb", "II Boomerang Raid", "III Stun Gun Headbutt"),
    "Yang": ("I Raishin Mahha Ken", "II Tenshin Senkyuutai", "III Sei'ei Enbu"),
    "Ken": ("I Shouryuu Reppa", "II Shinryuu Ken", "III Shippuujinrai Kyaku"),
    "Gill": ("I Resurrection", "II Meteor Strike", "III Seraphic Wing")
}

character_list = list(characterInfo.keys())

def display_characters():
    while True:
        for x in range(0, len(character_list), 1):
            if x == 0 or x == 19:
                print(character_list[x].center(22, " "))
            elif x % 3 == 0:
                print(f"{character_list[x]:8}")
            else:
                print(f"{character_list[x]:8}", end=" ")
        print()
        character_name = input("Choose a character (Type quit to quit program,\n or random to pick a random character): ").capitalize()
        if character_name.lower() == "quit":
            exit()
        elif character_name.lower() == "random":
            character_name = character_list[randrange(19)]
            break
        elif character_name not in characterInfo.keys():
            print()
            print(f"{character_name.capitalize()} is not a valid character. Please choose again.\n")
            continue
        else:
            break
    return character_name

def display_supers(character):
    super_list = list(characterInfo[character])
    while True:
        for x in range(0, len(super_list), 1):
            parts = super_list[x].split(" ", 1)
            print(f"{parts[0]:3}", end=" ")
            print(parts[1])
        print()
        try:
            super_number = int(input("Choose a Super Art (1, 2, or 3): "))
            if super_number not in range(1, 4):
                raise IndexError
            else:
                break
        except (IndexError, ValueError):
            print()
            print("You did not select a valid Super Art. Please choose again.\n")
            continue
    super_name = super_list[super_number - 1].split(" ", 1)
    return super_number, super_name

def main():
    while True:
        character = display_characters()
        print()
        print(f"Your character is {character.capitalize()}.\n")
        if character != "Gill":
            supers = display_supers(character)
            print()
            print(f"Your Super Art is {supers[1][1]}.")
            match character:
                case "Gouki":
                    match supers[0]:
                        case 1:
                            print("You also have access to the Super Arts Tenma Gou Zankuu, Shun Goku Satsu, and Kongou Kokuretsu Zan.")
                        case 2:
                            print("You also have access to the Super Arts Shun Goku Satsu and Kongou Kokuretsu Zan.")
                        case 3:
                            print("You also have access to the Super Arts Messatsu Gou Senpuu, Shun Goku Satsu, and Kongou Kokuretsu Zan.")
                case "Oro":
                    match supers[0]:
                        case 1:
                            print("You also have access to the Super Art Kishin Tsui.")
                        case 2:
                            print("You also have access to the Super Art Yagyou Oodama.")
                        case 3:
                            print("You also have access to the Super Art Tengu Midare Ishi.")
        else:
            print("Your Super Arts are Resurrection, Meteor Strike, and Seraphic Wing.")
        print()
        try:
            with open("../../Documents/output.txt", "w") as file:
                file.write(f"Your character is {character.capitalize()}.\n")
                file.write(f"Your Super Art is {supers[1][1]}.\n")
        except FileExistsError:
            print("That file already exists!")

if __name__ == "__main__":
    main()
