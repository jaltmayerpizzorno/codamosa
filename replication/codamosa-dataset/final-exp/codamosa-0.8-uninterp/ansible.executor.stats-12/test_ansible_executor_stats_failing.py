# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    try:
        float_0 = -1757.155
        int_0 = -215
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.summarize(int_0)
        list_0 = [float_0, float_0, float_0, float_0]
        aggregate_stats_1 = module_0.AggregateStats()
        var_1 = aggregate_stats_1.summarize(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'.\x8al\xbfj\x0b[\xb6\xff#\xaa\nQ\xc0\xe9'
        set_0 = {bytes_0, bytes_0, bytes_0}
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.update_custom_stats(bytes_0, set_0)
        str_0 = 'o8^SR|bM|l0"'
        str_1 = ')k*[wo%'
        var_1 = aggregate_stats_0.update_custom_stats(str_0, str_1)
        var_2 = aggregate_stats_0.update_custom_stats(set_0, aggregate_stats_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'BY'
        aggregate_stats_0 = module_0.AggregateStats()
        set_0 = set()
        var_0 = aggregate_stats_0.update_custom_stats(set_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'my_name'
        str_1 = 'my_value'
        var_0 = aggregate_stats_0.update_custom_stats(str_0, str_1)
        str_2 = 'my_other_value'
        var_1 = aggregate_stats_0.update_custom_stats(str_0, str_2)
        str_3 = 'my_other_name'
        str_4 = 'example.com'
        var_2 = aggregate_stats_0.update_custom_stats(str_3, str_1, str_4)
        var_3 = var_1.update
    except BaseException:
        pass

def test_case_4():
    try:
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'ok'
        str_1 = 'localhost'
        var_0 = aggregate_stats_0.decrement(str_0, str_1)
        set_0 = set()
        var_1 = aggregate_stats_0.decrement(str_0, set_0)
    except BaseException:
        pass