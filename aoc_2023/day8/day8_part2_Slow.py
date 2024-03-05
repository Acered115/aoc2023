import time


dict_list = {}


class Line:
    def __init__(self, line):
        self.line = line
        self.this = ""
        self.left = ""
        self.right = ""
        self._parse_line()

    def _parse_line(self):
        # print(self.line)
        self.this = self.line[:3]
        self.left = self.line[7:10]
        self.right = self.line[12:15]


def parse_file(file):
    directions = ""
    line_list = []
    for line in list(file):
        line = line.replace("\n", "")
        if len(line) != 16 and len(line) != 0:
            directions = line
            continue
        elif len(line) == 0:
            continue
        else:
            line_list.append(Line(line))
            dict_list[line[:3]] = Line(line)

    return directions, line_list


def traverse_directions(directions, line_list):
    steps = 0
    loop = True
    directions = list(directions)
    # line = line_list[index]
    nodes = []
    for line in line_list:
        if line.this[-1] == "A":
            nodes.append(line.this)
    nodes = sorted(nodes)
    original = nodes
    # nodes = sorted(["XRH", "XFQ", "SNC", "PLH", "VVH", "VLK"])
    while loop == True:
        for direct in directions:
            if loop == False:
                break
            truth_array = []
            # true_only = []

            for node_ in nodes:
                if node_[-1] != "Z":
                    truth_array.append(False)
                else:
                    truth_array.append(True)
                    # true_only.append(True)
            # for index, og_node in enumerate(original):
            # if og_node == nodes[index]:
            # print(original, nodes)
            # print()

            if False in truth_array:
                steps += 1

                for index, item in enumerate(nodes):
                    nodes[index] = find_in_list(item, direct)

                # print(nodes)
                # move_element(directions)
                # print("moved_Directions")

                if steps % 1000000 == 0:
                    print(steps)
                    print(truth_array)
                    print(nodes)

            else:
                print(f"The amount of steps taken for this {steps}")
                print(nodes)
                print(truth_array)

                loop = False
    return steps


def move_element(my_list):
    element = my_list.pop(0)
    my_list.append(element)
    return element


def find_in_list(this, direction):
    new_this = ""
    line = dict_list[this]
    if direction == "R":
        new_this = line.right
    else:
        new_this = line.left
    return new_this


if __name__ == "__main__":
    with open("puzzle_inputs/day8.txt", "r") as file:
        parsed_file = parse_file(file)
        # print(parsed_file)
    steps = traverse_directions(directions=parsed_file[0], line_list=parsed_file[1])
    print(steps)


35680000
[False, False, False, False, False, False]
["XRH", "XFQ", "SNC", "PLH", "VVH", "VLK"]
15299095336639
334000000
