# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hurd as module_0

def test_case_0():
    try:
        int_0 = -1099
        str_0 = 's2'
        list_0 = None
        float_0 = 0.0
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(float_0)
        var_0 = hurd_pfinet_network_0.assign_network_facts(int_0, str_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        hurd_network_collector_0 = module_0.HurdNetworkCollector(list_0)
        int_0 = -1669
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(hurd_network_collector_0, int_0)
        var_0 = hurd_pfinet_network_0.populate()
    except BaseException:
        pass