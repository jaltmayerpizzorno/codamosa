# Automatically generated by Pynguin.
import ansible.module_utils.facts.collector as module_0
import ansible.module_utils.facts.other.ohai as module_1

def test_case_0():
    try:
        base_fact_collector_0 = module_0.BaseFactCollector()
        ohai_fact_collector_0 = module_1.OhaiFactCollector()
        var_0 = ohai_fact_collector_0.collect(base_fact_collector_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ohai_fact_collector_0 = module_1.OhaiFactCollector()
        float_0 = -2290.786
        var_0 = ohai_fact_collector_0.run_ohai(float_0, ohai_fact_collector_0)
    except BaseException:
        pass