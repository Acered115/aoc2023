the_race = {"time": 54946592, "record": 302147610291404}
import time


def find_record_breakers(race):
    record_breakers = []
    length = race["time"]
    range_of_times = range(0, length)

    for duration in range_of_times:
        time_left = length - duration
        distance_travelled = time_left * duration

        if distance_travelled > race["record"]:
            record_breakers.append(distance_travelled)

    return record_breakers


if __name__ == "__main__":
    """I'm aware of the symmetric nature of this puzzle,
    but im a bit lazy to implement it.It runs in about 5
    seconds on my hardware so I'm happy to sacrifice those 5 seconds of my life :)

    But its something like len(range(duration, length - duration))
    """

    t0 = time.time()
    print(f"Running...")
    num_record_breakers = len(find_record_breakers(the_race))
    print(f"Complete.")
    print(f"It took {round(time.time() - t0,3)} seconds to run this function")
    print(f"The number of winning charge times is {num_record_breakers}")
