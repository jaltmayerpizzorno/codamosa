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
        dict_0 = {}
        bytes_0 = b'\xdbd\xd7|\x85\xa4\xe5\xa3\x0b\x11\x97\xf3\x96\x0fc\xcf6\x80'
        bytes_1 = b'K\xd52\xc7\xf24\xe3\xac#'
        ohai_fact_collector_0 = module_0.OhaiFactCollector(bytes_1)
        var_0 = ohai_fact_collector_0.run_ohai(dict_0, bytes_0)
    except BaseException:
        pass