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
        str_0 = 'o2ni69|Q(nOt'
        list_0 = [str_0, str_0, str_0, str_0]
        facter_fact_collector_0 = module_0.FacterFactCollector()
        var_0 = facter_fact_collector_0.run_facter(str_0, list_0)
    except BaseException:
        pass