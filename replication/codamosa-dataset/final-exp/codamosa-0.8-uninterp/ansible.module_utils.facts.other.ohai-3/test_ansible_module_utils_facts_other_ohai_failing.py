# Automatically generated by Pynguin.
import ansible.module_utils.facts.other.ohai as module_0

def test_case_0():
    try:
        ohai_fact_collector_0 = module_0.OhaiFactCollector()
        var_0 = ohai_fact_collector_0.collect()
        var_1 = ohai_fact_collector_0.collect(ohai_fact_collector_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ohai_fact_collector_0 = module_0.OhaiFactCollector()
        list_0 = [ohai_fact_collector_0, ohai_fact_collector_0, ohai_fact_collector_0]
        float_0 = 2.0
        var_0 = ohai_fact_collector_0.run_ohai(list_0, float_0)
    except BaseException:
        pass