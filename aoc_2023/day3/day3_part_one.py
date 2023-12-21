from pprint import pprint


def find_symbol_footprint(index, symbol):
    symbol_object = {}

    # if index==0:


def line_parser(line: str):
    """This function just parses each line into its important parts,
    numbers and symbols, it takes not of their indexes as this will be useful later

    :param line: incoming line string
    :type line: str
    :return: Object storing the indexes and symbols found in this line
    :rtype: Dictionary
    """
    number_list = []
    symbols_list = []
    number_buffer = ""
    number_index_buffer = []
    for index, x in enumerate(line):
        if x.isdigit():
            number_buffer += x
            number_index_buffer.append(index)
        else:
            if len(number_buffer) != 0:
                number = int(number_buffer)
                number_list.append({"index": number_index_buffer, "number": number})
                number_buffer = ""
                number_index_buffer = []

            if x != "." and x != "\n":
                symbols_list.append({"index": [index], "symbol": x})
    # print(symbols_list)
    # print(number_list)
    return_object = {"numbers": number_list, "symbols": symbols_list}
    return return_object


def symbol_appender():
    """Function responsible for broadening the index footprint so that
    in the following function i can just do an intersection with the numbers
    which share an index with the symbols
    """
    for row in lines_list:
        # symbol_appender(index, row)
        for symbol in row["symbols"]:
            symbol["index"].insert(0, symbol["index"][0] - 1)
            symbol["index"].append(symbol["index"][-1] + 1)


def check_neighbours():
    """Main function used to check the above and below members of each
    line. Figures out which numbers are in the footprint of the symbols
    of the above and below line and just summs them up
    """
    summ = 0
    for index, row in enumerate(lines_list):
        # print("index:", index)
        # pprint(lines_list)

        symbol_fields = []
        numbers_index = []
        if index == 0:
            for symbol in lines_list[index]["symbols"]:
                symbol_fields.extend(symbol["index"])
            for symbol in lines_list[index + 1]["symbols"]:
                symbol_fields.extend(symbol["index"])

        elif index == len(lines_list) - 1:
            for symbol in lines_list[index - 1]["symbols"]:
                symbol_fields.extend(symbol["index"])
            for symbol in lines_list[index]["symbols"]:
                symbol_fields.extend(symbol["index"])

        else:
            for symbol in lines_list[index - 1]["symbols"]:
                symbol_fields.extend(symbol["index"])
            for symbol in lines_list[index]["symbols"]:
                symbol_fields.extend(symbol["index"])
            for symbol in lines_list[index + 1]["symbols"]:
                symbol_fields.extend(symbol["index"])

        for numbers in lines_list[index]["numbers"]:
            numbers_index.extend(numbers["index"])
            # print(numbers["index"])
        # print(row["symbols"])
        # print("symbols", symbol_fields)
        # print("numbers", numbers_index)

        inter_indexes = list(set(symbol_fields) & set(numbers_index))
        # print(inter_indexes)
        if len(inter_indexes) >= 1:
            for numbers in row["numbers"]:
                # print(numbers["index"])
                if len(list(set(numbers["index"]) & set(inter_indexes))) > 0:
                    summ += numbers["number"]
                # print(numbers)

        # print("\n")
    print(summ)
    # print(lines_list[index + 1])


# Need to create symbol index checker between adjascent lines
#

if __name__ == "__main__":
    # test_row = line_parser(
    #     "........................#....374...382....250...*..........737*....*896.395...........*....................$.........................#......\n"
    # )
    lines_list = []

    with open("puzzle_inputs/day3.txt", "r") as file:
        for line in file:
            current_line = line_parser(line)
            lines_list.append(current_line)
    # print(current_line)
    symbol_appender()
    check_neighbours()
    # print(lines_list)
