from dataclasses import dataclass


@dataclass
class Card:
    line: str
    card_id = 0
    winners = []
    card_nums = []
    winning_numbers = []
    copies = 1

    def __post_init__(self):
        string_buffer = ""
        for letter in self.line:
            string_buffer += letter
            if letter == ":":
                self.card_id = int(string_buffer[4:-1])
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
        self._calc_winners()

    def _calc_winners(self):
        print(self.winners)
        print(self.card_nums)
        self.winning_numbers = list(set(self.winners) & set(self.card_nums))
        print(self.winning_numbers)
        print("\n")
        return


def calculate_copies(cards):
    return


if __name__ == "__main__":
    # test_str = "Card 123: 41 48  3 86 17 | 83 86  6 31 17  9 48 53\n"
    # card_obj = Card(test_str)
    # print(card_obj)
    card_list = []
    with open("puzzle_inputs/test4.txt", "r") as file:
        for line in file:
            card_list.append(Card(line))
            # print(Card(line).winning_numbers)
    calculate_copies(card_list)

    # print("Points in cards:", calc_total_points(card_list))
