bag_dict = {"red": 12, "green": 13, "blue": 14}
digit_str_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def set_parser(set_number: int, input_set: str):
    possible = True
    set_object = {
        "set_number": set_number,
        "red": 0,
        "blue": 0,
        "green": 0,
        "possible": possible,
    }
    colours = ["red", "blue", "green"]
    word_buffer = ""
    for letter in input_set:
        word_buffer += letter
        if letter == ",":
            word_buffer = word_buffer.replace(",", "")
            for colour in colours:
                if colour in word_buffer:
                    word_buffer = word_buffer.replace(colour, "")
                    # print(int(word_buffer))
                    set_object[colour] = int(word_buffer)
                    if bag_dict[colour] < int(word_buffer):
                        set_object["possible"] = False
                        break

            word_buffer = ""
    # print(set_object)
    return set_object


def game_parser(line: str):
    # print(line)
    Game = {
        "game": 0,
        "sets": [],
    }

    word_buffer = ""
    current_set = 1
    for x in line:
        # print(repr(x))
        if ":" in word_buffer:
            word_buffer = word_buffer.replace("Game", "")
            word_buffer = word_buffer.replace(":", "")
            Game["game"] = int(word_buffer)
            word_buffer += x
            word_buffer = ""

        if x == "\n" or x == ";":
            word_buffer = word_buffer.replace(";", "")
            Game["sets"].append(set_parser(current_set, word_buffer + ","))
            current_set = current_set + 1
            # print("set:", word_buffer)
            word_buffer = ""

        word_buffer += x
    # print("set:", word_buffer)
    possible = True
    for item in Game["sets"]:
        if item["possible"] == False:
            possible = item["possible"]

    return (Game["game"], possible)


#

if __name__ == "__main__":
    # game_parser("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n")
    sum_of_game_ids = 0
    with open("puzzle_inputs/day2.txt") as file:
        for line in file:
            # print(repr(line))
            game_result = game_parser(line)
            if game_result[1] == True:
                sum_of_game_ids += game_parser(line)[0]
    print(sum_of_game_ids)
