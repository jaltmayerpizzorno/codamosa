# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hurd as module_0

def test_case_0():
    try:
        float_0 = -1998.50518
        set_0 = {float_0, float_0}
        str_0 = '&vBvz_e_zq/bO'
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(str_0)
        var_0 = hurd_pfinet_network_0.assign_network_facts(float_0, float_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        hurd_network_collector_0 = module_0.HurdNetworkCollector()
        str_0 = '*[tFgg2V'
        bytes_0 = b'\x1e>\xa8'
        float_0 = -630.0122
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(bytes_0, float_0)
        var_0 = hurd_pfinet_network_0.populate(str_0)
    except BaseException:
        pass