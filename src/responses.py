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
            self.response_dict[self.response_enum.RESPONSE_0] = {
                'case_increase': 'No Ex, consider insulin correction ',
                'case_decrease': 'No Ex, consider insulin correction',
                'color': 'red'
            }

            #Dark Yellow Area
            self.response_dict[self.response_enum.RESPONSE_1] = {
                'case_increase': 'Consider Insulin Correction. Can start AE ',
                'case_decrease': 'Consider Insulin Correction. Can start all Ex',
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_2] = {
                'case_increase': 'Consider Insulin Correction. Can start AE ',
                'case_decrease': 'Consider Insulin Correction. Can start all Ex',
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_3] = {
                'case_increase': 'Can start all Ex',
                'case_decrease': 'Can start all Ex',
                'color': 'dark_yellow'
            }

            #Yellow Area
            self.response_dict[self.response_enum.RESPONSE_4] = {
                'case_increase': 'Can start AE. Consider insulin correction for RT, HIIT',
                'case_decrease': 'Can start AE. Consider insulin correction for RT, HIIT',
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_5] = {
                'case_increase': 'Can start all EX. Consider insulin correction for RT, HIIT',
                'case_decrease': 'Can start all EX',
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_6] = {
                'case_increase': 'Can start all Ex',
                'case_decrease': 'Can start all Ex',
                'color': 'yellow'
            }

            #Green area
            self.response_dict[self.response_enum.RESPONSE_7] = {
                'case_increase': 'Can start all Ex',
                'case_decrease': 'Can start all Ex',
                'color': 'green'
            }
            self.response_dict[self.response_enum.RESPONSE_8] = {
                'case_increase': 'Can start all Ex',
                'case_decrease': 'Can start all Ex. 15g CHO',
                'color': 'green'
            }

            #Yellow Area
            self.response_dict[self.response_enum.RESPONSE_9] = {
                'case_increase': 'Can start all Ex',
                'case_decrease': 'Can start all Ex. 15 g CHO',
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_10] = {
                'case_increase': 'Can start all Ex. 10 g CHO',
                'case_decrease': 'Can start all Ex. 20 g CHO',
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_11] = {
                'case_increase': 'Delay all Ex. 15 g CHO',
                'case_decrease': 'Delay all Ex. 25 g CHO',
                'color': 'yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_12] = {
                'case_increase': 'Delay all Ex. 20 g CHO',
                'case_decrease': 'Delay all Ex. 30 g CHO',
                'color': 'yellow'
            }

            #Dark Yellow Area
            self.response_dict[self.response_enum.RESPONSE_13] = {
                'case_increase': 'Can start all Ex. 10 g CHO',
                'case_decrease': 'Delay all Ex. 20 g CHO',
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_14] = {
                'case_increase': 'Delay all Ex. 15 g CHO',
                'case_decrease': 'Delay all Ex. 25 g CHO',
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_15] = {
                'case_increase': 'Delay all Ex. 20 g CHO',
                'case_decrease': 'Delay all Ex. 30 g CHO',
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_16] = {
                'case_increase': 'Delay all Ex. 25 g CHO',
                'case_decrease': 'Delay all Ex. 35 g CHO',
                'color': 'dark_yellow'
            }
            self.response_dict[self.response_enum.RESPONSE_17] = {
                'case_increase': 'Individual amount CHO Ingestion. Delay all Ex',
                'case_decrease': 'Individual amount CHO Ingestion. Delay all Ex',
                'color': 'dark_yellow'
            }

            #Red Area
            self.response_dict[self.response_enum.RESPONSE_18] = {
                'case_increase': 'Individual amount CHO Ingestion. Delay all Ex',
                'case_decrease': 'Individual amount CHO Ingestion. Delay all Ex',
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
