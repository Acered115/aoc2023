from pprint import pprint
import numpy as np
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
    # print(maps_obj)

    for map_ in maps_obj.keys():
        print(map_)
        if map_ == "seeds":
            continue
        for row in maps_obj[map_]:
            print(row)
            mapped_sources = np.arange(row[1], row[1] + row[2])
            # print("The Range", mapped_sources)
            if seed in mapped_sources:
                print(f"The seed is mapped: {seed}")
                displacement = seed - row[1]
                dest = row[0] + displacement
                print(f"This corresponds to a dest of {dest}")
                seed = dest

                break
            else:
                continue

    return dest


if __name__ == "__main__":
    with open("puzzle_inputs/test5.txt", "r") as file:
        obj = ParseMaps(file)
    locations = []
    t0 = time.time()
    for seed in obj.maps_obj["seeds"]:
        locations.append(reverse_parse_map(obj.maps_obj, seed))

    print("\n")
    print(f"It took {round(time.time()-t0, 4)} seconds to run this program")
    print(f"The list of locations is: {locations}")
    print(f"The lowest location number is: {min(locations)}")
