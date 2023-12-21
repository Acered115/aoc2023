from dataclasses import dataclass


@dataclass
class Card:
    """Class used to create Card objects which calculate all the
    relevant data per card
    """

    line: str
    card_id = 0
    win_nums = []
    card_nums = []
    winners = []
    copies = 1

    def __post_init__(self):
        string_buffer = ""
        for letter in self.line:
            string_buffer += letter
            if letter == ":":
                self.card_id = int(string_buffer[4:-1])
                string_buffer = ""
            if letter == "|":
                win_nums = string_buffer[1:-1].split(" ")
                while "" in win_nums:
                    win_nums.remove("")

                self.win_nums = win_nums
                string_buffer = ""

            else:
                card_nums = string_buffer[1:-1].split(" ")
                while "" in card_nums:
                    card_nums.remove("")

                self.card_nums = card_nums
        self.winners = list(set(self.win_nums) & set(self.card_nums))


def calculate_copies(cards: [Card]):
    """Loops through each copy of each card and increments the future cards according to the card's number of winners

    :param cards: Pass im a list of Card objects created by the Class in this file
    :type cards: List of Cards
    :return: returns an int of the number of total copies
    :rtype: integer
    """
    total_copies = 0

    for index, card in enumerate(cards):
        # print("Current Card:", card)
        copies = card.copies
        ### Run through each copy of this card
        while copies != 0:
            copies -= 1
            num_of_winners = len(card.winners)
            ### Increment the copies of the next winners by 1
            while num_of_winners != 0:
                cards[index + num_of_winners].copies += 1
                num_of_winners -= 1

        ### Add the copies of this card to the total number of copies
        total_copies += card.copies

    return total_copies


if __name__ == "__main__":
    card_list = []
    with open("puzzle_inputs/day4.txt", "r") as file:
        for line in file:
            card_list.append(Card(line))
    total_copies = calculate_copies(card_list)
    print(f"Total number of cards: {total_copies}")
