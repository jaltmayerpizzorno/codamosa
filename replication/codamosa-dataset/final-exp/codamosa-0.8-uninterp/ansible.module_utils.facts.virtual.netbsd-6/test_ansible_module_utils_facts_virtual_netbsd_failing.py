# Automatically generated by Pynguin.
import ansible.module_utils.facts.virtual.netbsd as module_0

def test_case_0():
    try:
        net_b_s_d_virtual_collector_0 = module_0.NetBSDVirtualCollector()
        net_b_s_d_virtual_0 = module_0.NetBSDVirtual(net_b_s_d_virtual_collector_0)
        var_0 = net_b_s_d_virtual_0.get_virtual_facts()
    except BaseException:
        pass