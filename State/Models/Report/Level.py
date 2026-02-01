
import enum


class Level(enum.Enum):
    Baby = 1
    Easy = 2
    Middle = 3
    Hard = 4
    Insane = 5

    def __str__(self):
        return self.name
