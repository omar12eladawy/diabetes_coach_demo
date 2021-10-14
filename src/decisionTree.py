

state_before = {
    'case_00': {
        'increase in glucsoe expected': 0,
        'decrease in glucose expected': 1,
    },
    'case_01': {
        'increase in glucsoe expected': 0,
        'decrease in glucose expected': 1,
    },
    'case_02': {
        'increase in glucsoe expected': 0,
        'decrease in glucose expected': 1,
    },
    'case_03': {
        'increase in glucsoe expected': 0,
        'decrease in glucose expected': 1,
    },
    'case_04': {
        'increase in glucsoe expected': 0,
        'decrease in glucose expected': 1,
    },
    'case_05': {
        'increase in glucsoe expected': 0,
        'decrease in glucose expected': 1,
    },
    'case_06': {
        'increase in glucsoe expected': 0,
        'decrease in glucose expected': 1,
    }
}

state_during = {}

state_after = {}

all_outcomes = [state_before, state_during, state_after]

class DecisionTree():
    def __init__(self, exercise_level: str, outcomes: dict):
        self.exercise_level = exercise_level
        self.outcomes = outcomes
        self.glu_ranges = 0

    def set_ranges(self):
        if self.exercise_level == 'ex_1':
            # self.glu_ranges = [ddddd]
            print('exercise level now set to ex_1')
            raise NotImplementedError
        elif self.exercise_level == 'ex_2':
            raise NotImplementedError
        elif self.exercise_level == 'ex_3':
            raise NotImplementedError

    def set_exercise_level(self, new_exercise_level):
        self.exercise_level = new_exercise_level
        self.set_ranges()

    def eval(self, current_glucose):
        pass
