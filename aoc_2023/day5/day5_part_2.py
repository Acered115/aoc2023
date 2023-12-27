from pprint import pprint
import time


class ParseMaps:
    def __init__(self, file):
        self.file = file
        self.maps_obj = {}
        self.parse_into_maps()

    def parse_into_maps(self):
        line_buffer = ""
        current_map = ""
        for line in self.file:
            line_buffer += line
            if "seeds:" in line:
                current_map = line.replace("\n", "")
                seeds = current_map[6:].split(" ")
                seeds.remove("")
                seeds = list(map(int, seeds))

                self.maps_obj[current_map[:5]] = seeds
                line_buffer = ""
                continue

            if ":" in line:
                current_map = line.replace(" map:\n", "")
                self.maps_obj[current_map] = []
                line_buffer = ""
                continue

            if len(line) != 1:
                current_line = line.replace("\n", "")
                line_maps = current_line.split(" ")
                line_maps = list(map(int, line_maps))

                self.maps_obj[current_map].append(line_maps)

            if line == "\n":
                line_buffer = ""
                continue


def reverse_parse_map(maps_obj, seed: int):
    dest = 0
    for map_ in maps_obj.keys():
        print(map_)
        if map_ == "seeds":
            continue
        for row in maps_obj[map_]:
            print(row)
            source = row[1]
            range_ = row[2]
            if seed <= source + range_ and seed > source:
                # print(row[1], row[2], source + range_)
                print(f"The seed is mapped: {seed}")
                displacement = seed - row[1]
                dest = row[0] + displacement
                print(f"This corresponds to a dest of {dest}")
                seed = dest

                break
            else:
                continue

    return dest


def check_seed_to_soil(maps_obj, seed, range_):
    print(maps_obj["seed-to_soil"])

    return


if __name__ == "__main__":
    with open("puzzle_inputs/test5.txt", "r") as file:
        obj = ParseMaps(file)
    list_of_ranges = []
    seeds = []
    numbers = []
    for index, seed in enumerate(obj.maps_obj["seeds"]):
        if index % 2:
            list_of_ranges.append((index, seed))

        else:
            seeds.append((index, seed))
            print(seed, obj.maps_obj["seeds"][index + 1])
            numbers.append(seed + obj.maps_obj["seeds"][index + 1])
            pass
        # seeds.pop(index)
    print(seeds)
    print(list_of_ranges)
    print(numbers)
    locations = []
    t0 = time.time()

    # for seed in obj.maps_obj["seeds"]:
    #     locations.append(reverse_parse_map(obj.maps_obj, seed))
    # for x in len()

    # check_seed_to_soil()

    print("\n")
    print(f"It took {round(time.time()-t0, 4)} seconds to run this program")
    print(f"The list of locations is: {locations}")
    print(f"The lowest location number is: {min(locations)}")
