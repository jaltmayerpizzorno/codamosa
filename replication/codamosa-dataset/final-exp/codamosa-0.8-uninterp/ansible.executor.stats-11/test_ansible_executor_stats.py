# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    aggregate_stats_0 = module_0.AggregateStats()

def test_case_1():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'ok'
    str_1 = 'host1'
    var_0 = aggregate_stats_0.increment(str_0, str_1)
    var_1 = aggregate_stats_0.decrement(str_0, str_1)

def test_case_2():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'ok'
    str_1 = 'localhost'
    var_0 = aggregate_stats_0.decrement(str_0, str_1)

def test_case_3():
    float_0 = -715.0
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.summarize(float_0)

def test_case_4():
    bytes_0 = b':6\x95*\x8c\xd1\xa6G7j\x8e7\xad\x80\xf7`\xc8=b\xea'
    bool_0 = True
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.update_custom_stats(bytes_0, bool_0)

def test_case_5():
    str_0 = '!^`3y!'
    str_1 = ''
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.set_custom_stats(str_0, str_1)
    aggregate_stats_1 = module_0.AggregateStats()
    str_2 = "$CGV4'"
    var_1 = aggregate_stats_0.update_custom_stats(str_2, str_2)

def test_case_6():
    float_0 = None
    bytes_0 = None
    str_0 = 'dO4E('
    aggregate_stats_0 = module_0.AggregateStats()
    tuple_0 = (bytes_0, str_0, aggregate_stats_0)
    aggregate_stats_1 = module_0.AggregateStats()
    var_0 = aggregate_stats_1.set_custom_stats(float_0, tuple_0)
    aggregate_stats_2 = module_0.AggregateStats()

def test_case_7():
    str_0 = 'rg{>'
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.set_custom_stats(str_0, str_0)
    float_0 = 1752.2717157320214
    var_1 = aggregate_stats_0.summarize(float_0)
    aggregate_stats_1 = module_0.AggregateStats()
    str_1 = "$CGV4'"
    var_2 = aggregate_stats_0.update_custom_stats(str_0, str_1)

def test_case_8():
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.processed
    var_1 = len(var_0)
    var_2 = aggregate_stats_0.ok
    var_3 = len(var_2)
    str_0 = 'ok'
    str_1 = 'hostname'
    var_4 = aggregate_stats_0.increment(str_0, str_1)
    var_5 = aggregate_stats_0.processed
    var_6 = len(var_5)
    var_7 = aggregate_stats_0.ok
    var_8 = len(var_7)
    bytes_0 = b'c\x15\xd7\x0c\x18P\x96\x0cXZX=\xc1\xa7Kz\xd6\xe2\xb7\xd7'
    list_0 = [var_7]
    bool_0 = False
    var_9 = aggregate_stats_0.update_custom_stats(bytes_0, list_0, bool_0)

def test_case_9():
    str_0 = 'bGB~YA@UK 9`AxB'
    str_1 = '|.3;+qu$NY%F!'
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.set_custom_stats(str_0, str_1)
    bool_0 = False
    str_2 = '/usr/local/etc/openssl'
    dict_0 = {str_2: str_0}
    var_1 = aggregate_stats_0.update_custom_stats(bool_0, dict_0)
    float_0 = 1751.3284
    var_2 = aggregate_stats_0.summarize(float_0)
    aggregate_stats_1 = module_0.AggregateStats()
    list_0 = [var_0, var_0, str_2]
    var_3 = aggregate_stats_0.update_custom_stats(bool_0, list_0)

def test_case_10():
    str_0 = 'bGB~YA@U? G`AxB'
    str_1 = '|.3;+qu$NY%F!'
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.set_custom_stats(str_0, str_1)
    bool_0 = False
    str_2 = '/usr/local/etc/openssl'
    dict_0 = {str_2: str_0}
    var_1 = aggregate_stats_0.update_custom_stats(bool_0, dict_0)
    float_0 = 1750.895052487788
    var_2 = aggregate_stats_0.summarize(float_0)
    aggregate_stats_1 = module_0.AggregateStats()
    var_3 = aggregate_stats_0.update_custom_stats(bool_0, dict_0)

def test_case_11():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'host'
    str_1 = 'ok'
    var_0 = aggregate_stats_0.decrement(str_1, str_0)
    var_1 = aggregate_stats_0.decrement(str_1, str_0)