from aenum import enum as Enum


class ResponseEnum(Enum):
    RESPONSE_0 = 'r_0'
    RESPONSE_1 = 'r_1'
    RESPONSE_2 = 'r_2'
    RESPONSE_3 = 'r_3'
    RESPONSE_4 = 'r_4'
    RESPONSE_5 = 'r_5'
    RESPONSE_6 = 'r_6'
    RESPONSE_7 = 'r_7'
    RESPONSE_8 = 'r_8'
    RESPONSE_9 = 'r_9'
    RESPONSE_10 = 'r_10'
    RESPONSE_11 = 'r_11'
    RESPONSE_12 = 'r_12'
    RESPONSE_13 = 'r_13'
    RESPONSE_14 = 'r_14'
    RESPONSE_15 = 'r_15'
    RESPONSE_16 = 'r_16'
    RESPONSE_17 = 'r_17'
    RESPONSE_18 = 'r_18'

#Todo integrate all the notes from the
class ResponseFactory():
    def __init__(self):
        self.response_dict = {}
        self.response_enum = ResponseEnum()

    def define_responses(self, state):
        if state == 'before':
            #Red Area
            #todo get value of insulin correction from paper
            self.response_dict[self.response_enum.RESPONSE_0] = {
                # 'case_increase': 'No Ex, consider insulin correction ',
                'case_increase': None,
                'case_decrease': {
                    'text_AE': 'Not ready for Exercise.',
                    'text_other': 'Not ready for Exercise.',
                    'insulin_rec_AE': 'Insulin Correction needed!',
                    'insulin_rec_other': 'Insulin Correction needed!',
                    'food_rec': None,
                },
                'color': 'red'
            }

            #Dark Yellow Area
            self.response_dict[self.response_enum.RESPONSE_1] = {
                # 'case_increase': 'Can start AE ',
                'case_decrease': {
                    'text_AE': 'Can start exercise! ',
                    'text_other': 'Can start exercise!',
                    'insulin_rec_AE': 'Consider Insulin Correction with 50% of the regular factor.',
                    'insulin_rec_other': 'Consider Insulin Correction with 50% of the regular factor.',
                    'food_rec': None,
                },
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_2] = {
                # 'case_increase': 'Can start AE ',
                'case_decrease': {
                    'text_AE': 'Can start exercise! ',
                    'text_other': 'Can start exercise!',
                    'insulin_rec_AE': 'Consider Insulin Correction with 50% of the regular factor.',
                    'insulin_rec_other': 'Consider Insulin Correction with 50% of the regular factor.',
                    'food_rec': None,
                },
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_3] = {
                # 'case_increase': 'Can start all Ex',
                'case_decrease': {
                    'text_AE': 'Can start all Ex',
                    'text_other': 'Can start all Ex',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': None
                },
                'color': 'dark_yellow'
            }

            #Yellow Area
            self.response_dict[self.response_enum.RESPONSE_4] = {
                # 'case_increase': 'Can start AE. Consider insulin correction for RT, HIIT',
                # 'case_decrease': 'Can start AE. Consider insulin correction for RT, HIIT',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'yellow'
                'case_decrease': {
                    'text_AE': 'Can start exercise!',
                    'text_other': 'Can start exercise, but consider insulin correction',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': 'Consider Insulin Correction with 50% of the regular factor.',
                    'food_rec': None
                },
                'color': 'yellow'
            }

            #todo: refactor the dict.
            self.response_dict[self.response_enum.RESPONSE_5] = {
                'case_decrease': {
                    'text_AE': 'Can start exercise!',
                    'text_other': 'Can start exercise!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': None
                },
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_6] = {
                # 'case_increase': 'Can start all Ex',
                # 'case_decrease': 'Can start all Ex',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'yellow'
                'case_decrease': {
                    'text_AE': 'Can start exercise!',
                    'text_other': 'Can start exercise!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': None
                },
                'color': 'yellow'
            }

            #Green area
            self.response_dict[self.response_enum.RESPONSE_7] = {
                # 'case_increase': 'Can start all Ex',
                # 'case_decrease': 'Can start all Ex',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'green'
                'case_decrease': {
                    'text_AE': 'Can start exercise!',
                    'text_other': 'Can start exercise!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': None
                },
                'color': 'green'
            }
            self.response_dict[self.response_enum.RESPONSE_8] = {
                # 'case_increase': 'Can start all Ex',
                # 'case_decrease': 'Can start all Ex. 15g CHO',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'green'
                'case_decrease': {
                    'text_AE': 'Can start exercise!',
                    'text_other': 'Can start exercise!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': '15'
                },
                'color': 'green'
            }

            #Yellow Area
            self.response_dict[self.response_enum.RESPONSE_9] = {
                # 'case_increase': 'Can start all Ex',
                # 'case_decrease': 'Can start all Ex. 15 g CHO',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'yellow'
                'case_decrease': {
                    'text_AE': 'Can start exercise!',
                    'text_other': 'Can start exercise!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': '15'
                },
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_10] = {
                # 'case_increase': 'Can start all Ex. 10 g CHO',
                # 'case_decrease': 'Can start all Ex. 20 g CHO',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'yellow'
                'case_decrease': {
                    'text_AE': 'Can start exercise!',
                    'text_other': 'Can start exercise!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': '20'
                },
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_11] = {
                # 'case_increase': 'Delay all Ex. 15 g CHO',
                # 'case_decrease': 'Delay all Ex. 25 g CHO',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'yellow'
                'case_decrease': {
                    'text_AE': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'text_other': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': '25'
                },
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_12] = {
                # 'case_increase': 'Delay all Ex. 20 g CHO',
                # 'case_decrease': 'Delay all Ex. 30 g CHO',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'yellow'
                'case_decrease': {
                    'text_AE': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'text_other': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': '30'
                },
                'color': 'yellow'
            }

            #Dark Yellow Area
            self.response_dict[self.response_enum.RESPONSE_13] = {
                # 'case_increase': 'Can start all Ex. 10 g CHO',
                # 'case_decrease': 'Delay all Ex. 20 g CHO',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'dark_yellow'
                'case_decrease': {
                    'text_AE': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'text_other': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': 'Insulin Correction needed!',
                    'food_rec': '20'
                },
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_14] = {
                # 'case_increase': 'Delay all Ex. 15 g CHO',
                # 'case_decrease': 'Delay all Ex. 25 g CHO',
                # 'color': 'dark_yellow'
                'case_decrease': {
                    'text_AE': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'text_other': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': 'Insulin Correction needed!',
                    'food_rec': '25'
                },
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_15] = {
                # 'case_increase': 'Delay all Ex. 20 g CHO',
                # 'case_decrease': 'Delay all Ex. 30 g CHO',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'dark_yellow'
                'case_decrease': {
                    'text_AE': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'text_other': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': 'Insulin Correction needed!',
                    'food_rec': '30'
                },
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_16] = {
                # 'case_increase': 'Delay all Ex. 25 g CHO',
                # 'case_decrease': 'Delay all Ex. 35 g CHO',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'dark_yellow'
                'case_decrease': {
                    'text_AE': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'text_other': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': 'Insulin Correction needed!',
                    'food_rec': '35'
                },
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_17] = {
                # 'case_increase': 'Individual amount CHO Ingestion. Delay all Ex',
                # 'case_decrease': 'Individual amount CHO Ingestion. Delay all Ex',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'dark_yellow'
                'case_decrease': {

                    'text_AE': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'text_other': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': 'Insulin Correction needed!',
                    'food_rec': 'Individual amount Carbohydrate ingestion'
                },
                'color': 'dark_yellow'
            }

            #Red Area
            self.response_dict[self.response_enum.RESPONSE_18] = {
                # 'case_increase': 'Individual amount CHO Ingestion. Delay all Ex',
                # 'case_decrease': 'Individual amount CHO Ingestion. Delay all Ex',
                # 'insulin_rec': None,
                # 'food_rec': None,
                # 'color': 'red'
                'case_decrease': {
                    'text_AE': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'text_other': 'Delay exercise at least until reaching 90mg/dl and ➡️, ↗️ or ⬆️!',
                    'insulin_rec_AE': None,
                    'insulin_rec_other': None,
                    'food_rec': 'Individual amount Carbohydrate ingestion'
                },
                'color': 'red'
            }

        elif state == 'during':
            self.response_dict[self.response_enum.RESPONSE_0] = ''
            self.response_dict[self.response_enum.RESPONSE_1] = ''
            self.response_dict[self.response_enum.RESPONSE_2] = ''
            self.response_dict[self.response_enum.RESPONSE_3] = ''
            self.response_dict[self.response_enum.RESPONSE_4] = ''
            self.response_dict[self.response_enum.RESPONSE_5] = ''
            self.response_dict[self.response_enum.RESPONSE_6] = ''
            self.response_dict[self.response_enum.RESPONSE_7] = ''
            self.response_dict[self.response_enum.RESPONSE_8] = ''
            self.response_dict[self.response_enum.RESPONSE_9] = ''
            self.response_dict[self.response_enum.RESPONSE_10] = ''
            self.response_dict[self.response_enum.RESPONSE_11] = ''
            self.response_dict[self.response_enum.RESPONSE_12] = ''
            self.response_dict[self.response_enum.RESPONSE_13] = ''
            self.response_dict[self.response_enum.RESPONSE_14] = ''
            self.response_dict[self.response_enum.RESPONSE_15] = ''
            self.response_dict[self.response_enum.RESPONSE_16] = ''
            self.response_dict[self.response_enum.RESPONSE_17] = ''
            self.response_dict[self.response_enum.RESPONSE_18] = ''

        elif state == 'after':
            self.response_dict[self.response_enum.RESPONSE_0] = ''
            self.response_dict[self.response_enum.RESPONSE_1] = ''
            self.response_dict[self.response_enum.RESPONSE_2] = ''
            self.response_dict[self.response_enum.RESPONSE_3] = ''
            self.response_dict[self.response_enum.RESPONSE_4] = ''
            self.response_dict[self.response_enum.RESPONSE_5] = ''
            self.response_dict[self.response_enum.RESPONSE_6] = ''
            self.response_dict[self.response_enum.RESPONSE_7] = ''
            self.response_dict[self.response_enum.RESPONSE_8] = ''
            self.response_dict[self.response_enum.RESPONSE_9] = ''
            self.response_dict[self.response_enum.RESPONSE_10] = ''
            self.response_dict[self.response_enum.RESPONSE_11] = ''
            self.response_dict[self.response_enum.RESPONSE_12] = ''
            self.response_dict[self.response_enum.RESPONSE_13] = ''
            self.response_dict[self.response_enum.RESPONSE_14] = ''
            self.response_dict[self.response_enum.RESPONSE_15] = ''
            self.response_dict[self.response_enum.RESPONSE_16] = ''
            self.response_dict[self.response_enum.RESPONSE_17] = ''
            self.response_dict[self.response_enum.RESPONSE_18] = ''

        else:
            raise Exception

    def get_reponsedict(self, state):
        self.define_responses(state)
        return self.response_dict
