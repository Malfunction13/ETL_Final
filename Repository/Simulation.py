from Models.Entry import Entry
import datetime
from random import randint, randrange, choice, uniform

class Simulation:

    def generate_random_ts(self):
        start_date = datetime.datetime(1969, 1, 1, 00, 00, 00, 000000)
        tz = randint(0, 12)
        east_west = choice(["+", "-"])
        random_ts = start_date + datetime.timedelta(days=randint(0, 99999),
                                                    hours=randint(0, 24),
                                                    seconds=randint(0, 999999),
                                                    microseconds=randint(1, 999999))

        if tz < 10:
            random_ts = str(random_ts) + east_west + f"0{tz}:00"
        else:
            random_ts = str(random_ts) + east_west + f"{tz}:00"

        return random_ts

    def generate_random_data(self):
        key = chr(randrange(97, 97 + 26)).upper() + str(randint(100, 999))
        value = f"{uniform(10.0, 29.9):.1f}"
        ts = self.generate_random_ts()

        return [Entry(key, value, ts)]

