# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.service_mgr as module_0

def test_case_0():
    try:
        bytes_0 = b'\\\x1d?\x84\r"h\xe3t\xe5_\xe2\xe4\x1de\xe9\x91'
        list_0 = [bytes_0, bytes_0, bytes_0]
        int_0 = -1092
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(int_0)
        var_0 = service_mgr_fact_collector_0.is_systemd_managed(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'mIG*M'
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.is_systemd_managed_offline(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        service_mgr_fact_collector_1 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_1.collect()
        float_0 = 100.0
        service_mgr_fact_collector_2 = module_0.ServiceMgrFactCollector(service_mgr_fact_collector_0)
        var_1 = service_mgr_fact_collector_2.collect(float_0, service_mgr_fact_collector_1)
    except BaseException:
        pass