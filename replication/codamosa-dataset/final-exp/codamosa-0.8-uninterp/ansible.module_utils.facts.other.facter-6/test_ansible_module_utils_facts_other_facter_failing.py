# Automatically generated by Pynguin.
import ansible.module_utils.facts.other.facter as module_0

def test_case_0():
    try:
        facter_fact_collector_0 = module_0.FacterFactCollector()
        var_0 = facter_fact_collector_0.collect()
        var_1 = facter_fact_collector_0.collect(facter_fact_collector_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = None
        facter_fact_collector_0 = module_0.FacterFactCollector()
        bool_0 = False
        facter_fact_collector_1 = module_0.FacterFactCollector()
        var_0 = facter_fact_collector_1.run_facter(set_0, bool_0)
    except BaseException:
        pass