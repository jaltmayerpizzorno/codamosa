# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hurd as module_0

def test_case_0():
    try:
        str_0 = 'Zxw'
        bytes_0 = None
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(bytes_0)
        hurd_network_collector_0 = module_0.HurdNetworkCollector()
        hurd_network_collector_1 = module_0.HurdNetworkCollector(hurd_network_collector_0)
        str_1 = 'D(wJ@RFnq rWb'
        hurd_pfinet_network_1 = module_0.HurdPfinetNetwork(str_1)
        var_0 = hurd_pfinet_network_1.assign_network_facts(str_0, hurd_pfinet_network_0, hurd_network_collector_1)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(tuple_0)
        var_0 = hurd_pfinet_network_0.populate()
    except BaseException:
        pass