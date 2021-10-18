from src.trends import Trends
from src.evaltrendsfactory import EvalTrendsFactory
import numpy as np


trends = Trends()
evalTrendsFactory = EvalTrendsFactory()


class DecisionTree():
    def __init__(self,):
        self.exercise_level = 'ex_1'
        self.state = 'before'
        self.glu_ranges = [(np.inf, 270),
                           (np.inf, 270),
                           (270, 181),
                           (180, 126),
                           (125, 90),
                           (89, 70),
                           (69, np.NINF)]
    def set_ranges(self):
        if self.exercise_level == 'ex_1':
            self.glu_ranges = [(np.inf, 270),
                               (np.inf, 270),
                               (270, 181),
                               (180, 126),
                               (125, 90),
                               (89, 70),
                               (70, np.NINF)]
            print('exercise level now set to ex_1')
        elif self.exercise_level == 'ex_2':
            self.glu_ranges = [(np.inf, 270),
                               (np.inf, 270),
                               (270, 199),
                               (198, 145),
                               (144, 90),
                               (89, 70),
                               (70, np.NINF)]
            print('exercise level now set to ex_2')

        elif self.exercise_level == 'ex_3':
            self.glu_ranges = [(np.inf, 270),
                               (np.inf, 270),
                               (270, 217),
                               (216, 162),
                               (161, 90),
                               (89, 70),
                               (70, np.NINF)]
            print('exercise level now set to ex_3')

    def set_state(self, new_state):
        self.state = new_state

    def set_exercise_level(self, new_exercise_level):
        self.exercise_level = new_exercise_level
        self.set_ranges()

    def eval_glucose(self, glucose_level, trend):
        eval_func = evalTrendsFactory.get_eval_func(self.state)
        case_level = -1
        for i, bounds in enumerate(self.glu_ranges):
            if glucose_level >= bounds[1] and glucose_level <= bounds[0]:
                case_level = i
        res = eval_func(case_level, trend)
        return res


if __name__ == '__main__':
    dt = DecisionTree('ex_1')
    res = dt.eval_glucose(270, trends.UP)
    print('#'*1000,'\n')
    print('-'*100)
    print('|' ,'='*10, 'Here are the result of your Evaluation','='*10)

    print('|' , 'Expecting Glucose increase =>', res['case_increase'])
    print('|' ,'Expecting Glucose decrease =>', res['case_decrease'])
    print('-'*100)
