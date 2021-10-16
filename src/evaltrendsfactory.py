import logging

from responses import ResponseFactory, ResponseEnum
from trends import Trends

res_enum = ResponseEnum()
res_factory = ResponseFactory()
trend_enum = Trends()

class EvalTrendsFactory():
    def __init__(self):
        print('Eval Trends Interface created')

    def eval_trends_before(self, case_level, trend):
        print('created before eval trends with case level', case_level)
        res_dict = res_factory.get_reponsedict('before')
        if case_level == 0:
            return res_dict[res_enum.RESPONSE_0]

        elif case_level == 1:
            if trend == trend_enum.UP or \
                    trend == trend_enum.GOING_UP:
                return res_dict[res_enum.RESPONSE_1]

            elif trend == trend_enum.STABLE:
                return res_dict[res_enum.RESPONSE_2]

            elif trend == trend_enum.GOING_DOWN or \
                    trend == trend_enum.DOWN:
                return res_dict[res_enum.RESPONSE_3]

        elif case_level == 2:
            if trend == trend_enum.UP or \
                    trend == trend_enum.GOING_UP:
                return res_dict[res_enum.RESPONSE_4]

            elif trend == trend_enum.STABLE:
                return res_dict[res_enum.RESPONSE_5]

            elif trend == trend_enum.GOING_DOWN or \
                    trend == trend_enum.DOWN:
                return res_dict[res_enum.RESPONSE_6]

        elif case_level == 3:
            if trend == trend_enum.UP or \
                    trend == trend_enum.GOING_UP or \
                    trend == trend_enum.STABLE:
                return res_dict[res_enum.RESPONSE_7]

            elif trend == trend_enum.GOING_DOWN or \
                    trend == trend_enum.DOWN:
                return res_dict[res_enum.RESPONSE_8]

        elif case_level == 4:
            if trend == trend_enum.UP or \
                    trend == trend_enum.GOING_UP:
                return res_dict[res_enum.RESPONSE_9]

            elif trend == trend_enum.STABLE:
                return res_dict[res_enum.RESPONSE_10]

            elif trend == trend_enum.GOING_DOWN:
                return res_dict[res_enum.RESPONSE_11]

            elif trend == trend_enum.DOWN:
                return res_dict[res_enum.RESPONSE_12]

        elif case_level == 5:
            if trend == trend_enum.UP:
                return res_dict[res_enum.RESPONSE_13]

            elif trend == trend_enum.GOING_UP:
                return res_dict[res_enum.RESPONSE_14]

            elif trend == trend_enum.STABLE:
                return res_dict[res_enum.RESPONSE_15]

            elif trend == trend_enum.GOING_DOWN:
                return res_dict[res_enum.RESPONSE_16]

            elif trend == trend_enum.DOWN:
                return res_dict[res_enum.RESPONSE_17]

            elif case_level == 6:
                return res_dict[res_enum.RESPONSE_18]
            elif case_level == -1:
                raise AssertionError

    def eval_trends_during(self, case_level, trend):
        res_dict = res_factory.get_reponsedict('during')
        if case_level == 0:
            pass
        elif case_level == 1:
            pass
        elif case_level == 2:
            pass
        elif case_level == 3:
            pass
        elif case_level == 4:
            pass
        elif case_level == 5:
            pass
        elif case_level == 6:
            pass
        else:
            raise AssertionError

    def eval_trends_after(self, case_level, trend):
        res_dict = res_factory.get_reponsedict('after')
        if case_level == 0:
            pass
        elif case_level == 1:
            pass
        elif case_level == 2:
            pass
        elif case_level == 3:
            pass
        elif case_level == 4:
            pass
        elif case_level == 5:
            pass
        elif case_level == 6:
            pass
        else:
            raise AssertionError

    def get_eval_func(self, state):
        if state == 'before':
            print('not in get eval func')
            return self.eval_trends_before
        elif state == 'during':
            pass
        elif state == 'after':
            pass

