# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    aggregate_stats_0 = module_0.AggregateStats()

def test_case_1():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'ok'
    str_1 = 'test_host'
    var_0 = aggregate_stats_0.increment(str_0, str_1)
    var_1 = aggregate_stats_0.decrement(str_0, str_1)
    var_2 = aggregate_stats_0.decrement(str_0, str_1)

def test_case_2():
    bool_0 = True
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.summarize(bool_0)

def test_case_3():
    float_0 = 5093.1
    aggregate_stats_0 = module_0.AggregateStats()
    aggregate_stats_1 = module_0.AggregateStats()
    var_0 = aggregate_stats_1.set_custom_stats(float_0, aggregate_stats_0)

def test_case_4():
    str_0 = ''
    str_1 = {str_0: str_0}
    aggregate_stats_0 = module_0.AggregateStats()
    str_2 = 'first'
    str_3 = 'second'
    var_0 = aggregate_stats_0.set_custom_stats(str_2, str_3)
    str_4 = 'one'
    var_1 = aggregate_stats_0.set_custom_stats(str_4, str_1)
    var_2 = aggregate_stats_0.update_custom_stats(str_2, str_3)
    var_3 = aggregate_stats_0.update_custom_stats(str_4, str_1)
    var_4 = aggregate_stats_0.update_custom_stats(str_4, str_1)

def test_case_5():
    aggregate_stats_0 = module_0.AggregateStats()
    aggregate_stats_1 = module_0.AggregateStats()
    aggregate_stats_2 = module_0.AggregateStats()
    bool_0 = False
    int_0 = 829
    var_0 = aggregate_stats_0.update_custom_stats(bool_0, int_0)

def test_case_6():
    str_0 = 'host1'
    str_1 = 'custom_stat'
    aggregate_stats_0 = module_0.AggregateStats()
    int_0 = 1
    var_0 = aggregate_stats_0.update_custom_stats(str_1, int_0, str_0)
    var_1 = aggregate_stats_0.update_custom_stats(str_1, int_0, str_0)
    str_2 = 'string1'
    var_2 = aggregate_stats_0.update_custom_stats(str_1, str_2, str_0)

def test_case_7():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = "F'3Ms\x0cXnQ*^/<'u|"
    float_0 = 865.14
    var_0 = aggregate_stats_0.set_custom_stats(str_0, float_0)
    str_1 = 'done checking to see if all hosts have failed'
    var_1 = aggregate_stats_0.update_custom_stats(str_0, str_1)

def test_case_8():
    bool_0 = True
    aggregate_stats_0 = module_0.AggregateStats()
    var_0 = aggregate_stats_0.summarize(bool_0)
    str_0 = "F'3Ms\x0cXnQ*^/<'u|"
    float_0 = 865.14
    var_1 = aggregate_stats_0.set_custom_stats(str_0, float_0)
    tuple_0 = ()
    str_1 = 'done checking to see if all hosts have failed'
    var_2 = aggregate_stats_0.update_custom_stats(aggregate_stats_0, tuple_0, str_1)
    aggregate_stats_1 = module_0.AggregateStats()
    int_0 = None
    set_0 = set()
    var_3 = aggregate_stats_0.update_custom_stats(int_0, set_0)

def test_case_9():
    aggregate_stats_0 = module_0.AggregateStats()
    str_0 = 'ok'
    var_0 = aggregate_stats_0.decrement(str_0, str_0)
    var_1 = aggregate_stats_0.decrement(str_0, str_0)