# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    try:
        list_0 = []
        bool_0 = False
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.decrement(list_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = None
        dict_0 = {set_0: set_0}
        list_0 = [dict_0, set_0, dict_0, dict_0]
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.summarize(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        aggregate_stats_0 = module_0.AggregateStats()
        float_0 = 1000.0
        var_0 = aggregate_stats_0.summarize(float_0)
        set_0 = {aggregate_stats_0, aggregate_stats_0, aggregate_stats_0}
        bool_0 = None
        int_0 = 3222
        aggregate_stats_1 = module_0.AggregateStats()
        aggregate_stats_2 = module_0.AggregateStats()
        var_1 = aggregate_stats_0.set_custom_stats(set_0, bool_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 73
        dict_0 = {int_0: int_0, int_0: int_0}
        int_1 = 301
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.summarize(int_1)
        aggregate_stats_1 = module_0.AggregateStats()
        str_0 = "h|'7cZSc\r1"
        aggregate_stats_2 = module_0.AggregateStats()
        var_1 = aggregate_stats_2.update_custom_stats(dict_0, aggregate_stats_1, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'failures'
        set_0 = {aggregate_stats_0, aggregate_stats_0, str_0, aggregate_stats_0}
        var_0 = aggregate_stats_0.decrement(str_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'gO4`hSIgn^tC=6q9o'
        list_0 = [str_0, str_0]
        aggregate_stats_0 = module_0.AggregateStats()
        aggregate_stats_1 = module_0.AggregateStats()
        var_0 = aggregate_stats_1.set_custom_stats(str_0, list_0, aggregate_stats_0)
        aggregate_stats_2 = module_0.AggregateStats()
        str_1 = 'a'
        var_1 = aggregate_stats_2.update_custom_stats(str_1, str_0)
        var_2 = dict()
        var_3 = dict()
        var_4 = aggregate_stats_2.update_custom_stats(str_1, var_3)
        var_5 = dict()
        int_0 = 1
        var_6 = dict(b=int_0)
        var_7 = aggregate_stats_2.update_custom_stats(str_1, var_6)
        var_8 = dict(b=int_0)
        float_0 = 0.5
        var_9 = aggregate_stats_2.update_custom_stats(str_1, str_1)
        var_10 = dict(b=int_0, c=float_0)
        var_11 = dict(c=int_0)
        var_12 = aggregate_stats_2.update_custom_stats(str_1, var_11)
        var_13 = dict(b=int_0, c=int_0)
        var_14 = aggregate_stats_2.update_custom_stats(list_0, float_0)
    except BaseException:
        pass