def parse_card(card):
    string_buffer = ""
    card_obj = {"card": 000, "winners": [], "card_num": []}
    for letter in card:
        string_buffer += letter
        if letter == ":":
            card_obj["card"] = int(string_buffer[4:-1])
            string_buffer = ""
        if letter == "|":
            winners = string_buffer[1:-1].split(" ")
            while "" in winners:
                winners.remove("")

            card_obj["winners"] = winners
            string_buffer = ""

        else:
            card_num = string_buffer[1:-1].split(" ")
            while "" in card_num:
                card_num.remove("")

            card_obj["card_num"] = card_num

    return card_obj


if __name__ == "__main__":
    test_str = "Card 123: 41 48  3 86 17 | 83 86  6 31 17  9 48 53\n"
    print(parse_card(test_str))
    # with open("puzzle_inputs/test4.txt", "r") as file:
    #     for line in file:
    #         parse_card(line)
