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
        tuple_0 = ()
        facter_fact_collector_0 = module_0.FacterFactCollector(tuple_0)
        set_0 = {facter_fact_collector_0, facter_fact_collector_0}
        float_0 = -412.261
        var_0 = facter_fact_collector_0.run_facter(set_0, float_0)
    except BaseException:
        pass