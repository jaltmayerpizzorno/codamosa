# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.local as module_0

def test_case_0():
    try:
        int_0 = 480
        local_fact_collector_0 = module_0.LocalFactCollector()
        var_0 = local_fact_collector_0.collect(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        local_fact_collector_0 = module_0.LocalFactCollector()
        var_0 = local_fact_collector_0.collect()
        var_1 = local_fact_collector_0.collect(local_fact_collector_0)
    except BaseException:
        pass