# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    aggregate_stats_0 = module_0.AggregateStats()

def test_case_1():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'ok'
    str_1 = 'test'
    var_0 = aggregate_stats_0.increment(str_0, str_1)
    var_1 = aggregate_stats_0.decrement(str_0, str_1)

def test_case_2():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'skipped'
    str_1 = 'all'
    var_0 = aggregate_stats_0.decrement(str_0, str_1)

def test_case_3():
    str_0 = 'jDF\rT+jYjK'
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.summarize(str_0)

def test_case_4():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'what'
    var_0 = aggregate_stats_0.update_custom_stats(str_0, str_0)
    var_1 = aggregate_stats_0.update_custom_stats(str_0, str_0)
    str_1 = {str_0: str_0}
    var_2 = aggregate_stats_0.update_custom_stats(str_0, str_1)
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    var_3 = aggregate_stats_0.update_custom_stats(str_0, int_3)

def test_case_5():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'foo'
    str_1 = 'c'
    int_0 = 1
    int_1 = 2
    int_2 = {str_0: int_0, str_1: int_1}
    str_2 = 'host'
    var_0 = aggregate_stats_0.set_custom_stats(str_0, int_2, str_2)
    str_3 = 'b'
    int_3 = {str_0: int_1, str_3: int_0}
    var_1 = aggregate_stats_0.update_custom_stats(str_0, int_3, str_2)

def test_case_6():
    aggregate_stats_0 = module_0.AggregateStats()
    set_0 = None
    str_0 = 'failed to retrieve selinux context'
    var_0 = aggregate_stats_0.update_custom_stats(set_0, str_0)
    var_1 = aggregate_stats_0.summarize(str_0)
    aggregate_stats_1 = module_0.AggregateStats()
    bytes_0 = b'\xdcOL\xd3}4\x05S\xa4"\xdc\xed\xdf'
    tuple_0 = ()
    tuple_1 = (bytes_0, tuple_0)
    var_2 = aggregate_stats_0.update_custom_stats(str_0, tuple_1)

def test_case_7():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'ok'
    str_1 = 'host1'
    var_0 = aggregate_stats_0.decrement(str_0, str_1)
    var_1 = aggregate_stats_0.decrement(str_0, str_1)