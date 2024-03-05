letter_ranking = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}
hand_rankings = {
    "high_card": 0,
    "one_pair": 1,
    "two_pair": 2,
    "three_of_a_kind": 3,
    "full_house": 4,
    "four_of_a_kind": 5,
    "five_of_a_kind": 6,
}

one_dupe_list = {
    2: "one_pair",
    3: "three_of_a_kind",
    4: "four_of_a_kind",
    5: "five_of_a_kind",
}


class CamelCard:
    def __init__(self, line):
        self.line = line
        self.rank = None
        self.parse_line()

    def parse_line(self):
        self.hand = self.line[0:5]
        self.bet = self.line[6:-1]


def find_hand_rank(play):
    hand = play.hand
    # Using a dictionary to find duplicates and their occurrences
    count_dict = {}
    for item in hand:
        count_dict[item] = count_dict.get(item, 0) + 1

    # Extracting duplicates and their occurrences from the dictionary
    duplicates_with_count = {
        item: count for item, count in count_dict.items() if count > 1
    }

    num_dup_cards = len(duplicates_with_count.items())
    rank = "high_card"
    if num_dup_cards == 1:
        for duplicate_card in duplicates_with_count.items():
            rank = one_dupe_list[duplicate_card[1]]
    if num_dup_cards == 2:
        rank = "two_pair"
        for duplicate_card in duplicates_with_count.items():
            # print(duplicate_card)
            if duplicate_card[1] == 3:
                rank = "full_house"
                break
    play.rank = rank
    return rank


def sort_individual_rank(rank_list):
    # print(rank_list)
    index_list = {}
    for index in range(0, 5):
        index_list[index] = []
        for card in rank_list:
            index_list[index].append(letter_ranking[card.hand[index]])
        for duplicate in index_list[index]:
            duplicates = [
                item for item in index_list[index] if index_list[index].count(item) > 1
            ]
            print(index_list)
    # sorted_by = sorted(rank_list, key=lambda x: letter_ranking[x.hand[0]])[::-1]

    # for card in sorted_by:
    #     print(card.hand, card.rank)
    # print("\n")


if __name__ == "__main__":
    rank = 0
    card_list = []
    with open("puzzle_inputs/test7.txt", "r") as file:
        for line in file:
            card_list.append(CamelCard(line))
    # find_camelcard_ranks(card_list)
    for card in card_list:
        print(card.hand)
        find_hand_rank(card)
        print(card.rank)
    print("\n")
    sorted_cards_list = sorted(card_list, key=lambda x: hand_rankings[x.rank])

    # for card in sorted_cards_list:
    #     print(card.hand)
    #     print(card.rank)
    final_list = []
    for card_rank in hand_rankings.keys():
        card_rank_list = []
        for card in sorted_cards_list:
            if card.rank == card_rank:
                card_rank_list.append(card)
        # print(card_rank_list)
        # sorted_rank = sort_individual_rank(card_rank_list)
        # final_list.append(sorted_rank)
    for card in card_rank_list:
        print(card.hand)
    sort_individual_rank(card_rank_list)
    # print(lists_object)
