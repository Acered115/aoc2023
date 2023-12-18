from dataclasses import dataclass


@dataclass
class Card:
    line: str
    card = 0
    winners = []
    card_nums = []

    def __post_init__(self):
        string_buffer = ""
        for letter in self.line:
            string_buffer += letter
            if letter == ":":
                self.card = int(string_buffer[4:-1])
                string_buffer = ""
            if letter == "|":
                winners = string_buffer[1:-1].split(" ")
                while "" in winners:
                    winners.remove("")

                self.winners = winners
                string_buffer = ""

            else:
                card_num = string_buffer[1:-1].split(" ")
                while "" in card_num:
                    card_num.remove("")

                self.card_nums = card_num


def calc_total_points(card_list):
    summ = 0
    for card in card_list:
        point = 1
        # print("Card num:", card.card)
        winning_set = list(set(card.winners) & set(card.card_nums))
        if len(winning_set) > 1:
            for number in winning_set[:-1]:
                point *= 2
        elif len(winning_set) == 0:
            point = 0

        summ += point
    return summ


if __name__ == "__main__":
    # test_str = "Card 123: 41 48  3 86 17 | 83 86  6 31 17  9 48 53\n"
    # card_obj = Card(test_str)
    # print(card_obj)
    card_list = []
    with open("puzzle_inputs/day4.txt", "r") as file:
        for line in file:
            card_list.append(Card(line))
    print("Points in cards:", calc_total_points(card_list))
