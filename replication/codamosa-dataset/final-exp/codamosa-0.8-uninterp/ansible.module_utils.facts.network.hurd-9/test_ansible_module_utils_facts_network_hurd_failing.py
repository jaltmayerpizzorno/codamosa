# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hurd as module_0

def test_case_0():
    try:
        float_0 = 1331.222032
        int_0 = 5780
        int_1 = 497
        bool_0 = False
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(bool_0)
        var_0 = hurd_pfinet_network_0.assign_network_facts(float_0, int_0, int_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n[6"/K|d>LnbFIl'
        str_1 = '"$wHYa!+\x0bHU\x0cN+$;['
        hurd_pfinet_network_0 = module_0.HurdPfinetNetwork(str_0, str_1)
        var_0 = hurd_pfinet_network_0.populate()
    except BaseException:
        pass