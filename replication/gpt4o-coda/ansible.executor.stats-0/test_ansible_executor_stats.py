# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    aggregate_stats_0 = module_0.AggregateStats()

def test_case_1():
    str_0 = None
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.summarize(str_0)

def test_case_2():
    str_0 = 'chattr'
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.update_custom_stats(str_0, aggregate_stats_0)

def test_case_3():
    int_0 = 1008
    bytes_0 = b'D\xf0H\x942\xe6-\x9b\xa91\xcet\xa58\xb8M'
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.set_custom_stats(int_0, bytes_0)