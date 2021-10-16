from .trends import Trends
from .responses import ResponseFactory
from .evaltrendsfactory import EvalTrendsFactory
import numpy as np


trends = Trends()
evalTrendsFactory = EvalTrendsFactory()


class DecisionTree():
    def __init__(self, exercise_level: str):
        self.exercise_level = exercise_level
        self.state = 'before'
        self.glu_ranges = [(np.inf, 270),
                           (np.inf, 270),
                           (270, 181),
                           (180, 126),
                           (125, 90),
                           (89, 70),
                           (70, np.ninf)]
    def set_ranges(self):
        if self.exercise_level == 'ex_1':
            self.glu_ranges = [(np.inf, 270),
                               (np.inf, 270),
                               (270, 181),
                               (180, 126),
                               (125, 90),
                               (89, 70),
                               (70, np.ninf)]
            print('exercise level now set to ex_1')

        elif self.exercise_level == 'ex_2':
            self.glu_ranges = [(np.inf, 270),
                               (np.inf, 270),
                               (270, 199),
                               (198, 145),
                               (144, 90),
                               (89, 70),
                               (70, np.ninf)]
            print('exercise level now set to ex_1')

        elif self.exercise_level == 'ex_3':
            self.glu_ranges = [(np.inf, 270),
                               (np.inf, 270),
                               (270, 217),
                               (216, 162),
                               (161, 90),
                               (89, 70),
                               (70, np.ninf)]
            print('exercise level now set to ex_1')

    def set_state(self, new_state):
        self.state = new_state

    def set_exercise_level(self, new_exercise_level):
        self.exercise_level = new_exercise_level
        self.set_ranges()

    def eval_glucose(self, glucose_level, trend):
        eval_func = evalTrendsFactory.get_eval_func(self.state)
        case_level = -1
        for lower_bound, upper_bound, i in enumerate(self.glu_ranges):
            if glucose_level >= lower_bound and glucose_level <= upper_bound:
                case_level = i
        eval_func(case_level, trend)


if __name__ == '__main__':
    print('wtf')
