# Automatically generated by Pynguin.
import ansible.module_utils.facts.virtual.netbsd as module_0

def test_case_0():
    try:
        bool_0 = True
        net_b_s_d_virtual_0 = module_0.NetBSDVirtual(bool_0)
        var_0 = net_b_s_d_virtual_0.get_virtual_facts()
    except BaseException:
        pass