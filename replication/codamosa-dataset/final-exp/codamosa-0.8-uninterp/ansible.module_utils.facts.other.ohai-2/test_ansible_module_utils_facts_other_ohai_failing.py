# Automatically generated by Pynguin.
import ansible.module_utils.facts.other.ohai as module_0

def test_case_0():
    try:
        str_0 = 'zE;=!/g41'
        ohai_fact_collector_0 = module_0.OhaiFactCollector()
        var_0 = ohai_fact_collector_0.find_ohai(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -779
        ohai_fact_collector_0 = module_0.OhaiFactCollector()
        ohai_fact_collector_1 = module_0.OhaiFactCollector()
        ohai_fact_collector_2 = module_0.OhaiFactCollector()
        var_0 = ohai_fact_collector_2.run_ohai(int_0, ohai_fact_collector_0)
    except BaseException:
        pass

def test_case_2():
    try:
        ohai_fact_collector_0 = module_0.OhaiFactCollector()
        var_0 = ohai_fact_collector_0.collect()
        var_1 = ohai_fact_collector_0.collect(ohai_fact_collector_0)
    except BaseException:
        pass