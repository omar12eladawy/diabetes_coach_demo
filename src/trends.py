from aenum import enum as Enum

class Trends(Enum):
    UP = 'up'
    GOING_UP = 'going up'
    STABLE = 'stable'
    GOING_DOWN = 'going down'
    DOWN = 'down'