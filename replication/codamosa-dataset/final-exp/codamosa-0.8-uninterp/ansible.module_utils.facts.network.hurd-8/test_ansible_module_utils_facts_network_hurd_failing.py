# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hurd as module_0

def test_case_0():
    try:
        hurd_network_collector_0 = module_0.HurdNetworkCollector()
        str_0 = ';3.A\\'
        bytes_0 = b'\xfe\xb5T\x95\xa5\x88'
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(bytes_0)
        var_0 = hurd_pfinet_network_0.assign_network_facts(hurd_network_collector_0, str_0, hurd_network_collector_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"\x88:>~'"
        float_0 = -1278.0
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(float_0)
        var_0 = hurd_pfinet_network_0.populate(bytes_0)
    except BaseException:
        pass