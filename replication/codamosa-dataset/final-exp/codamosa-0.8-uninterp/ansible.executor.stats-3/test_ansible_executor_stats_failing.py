# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    try:
        dict_0 = None
        list_0 = []
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.increment(dict_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xa6\x8c\x90Kh\xb5'
        str_0 = '/.dockerinit'
        float_0 = -136.6
        bytes_1 = None
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.update_custom_stats(str_0, bytes_1, float_0)
        dict_0 = {bytes_0: bytes_1, bytes_1: aggregate_stats_0, str_0: str_0, var_0: bytes_1}
        complex_0 = None
        var_1 = aggregate_stats_0.set_custom_stats(dict_0, complex_0)
    except BaseException:
        pass

def test_case_2():
    try:
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'ok'
        str_1 = 'host'
        var_0 = aggregate_stats_0.decrement(str_0, str_1)
        str_2 = 'host1'
        bytes_0 = b'w\x95s\xbc'
        list_0 = [str_0, bytes_0, str_2]
        aggregate_stats_1 = module_0.AggregateStats()
        var_1 = aggregate_stats_1.decrement(str_0, list_0)
    except BaseException:
        pass