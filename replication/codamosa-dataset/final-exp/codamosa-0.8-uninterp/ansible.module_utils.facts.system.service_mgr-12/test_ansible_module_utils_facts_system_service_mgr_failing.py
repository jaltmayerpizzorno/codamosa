# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.service_mgr as module_0

def test_case_0():
    try:
        service_mgr_fact_collector_0 = None
        service_mgr_fact_collector_1 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_1.is_systemd_managed(service_mgr_fact_collector_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'i+3I\x98C\x0f,\xfa\xdfa"\x9dsHA\xb3\xb0\xa3'
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.is_systemd_managed_offline(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        list_0 = [service_mgr_fact_collector_0]
        int_0 = -3522
        dict_0 = {service_mgr_fact_collector_0: service_mgr_fact_collector_0, service_mgr_fact_collector_0: list_0}
        var_0 = service_mgr_fact_collector_0.collect(int_0, dict_0)
        var_1 = service_mgr_fact_collector_0.collect(list_0)
        var_2 = service_mgr_fact_collector_0.collect()
        bool_0 = True
        service_mgr_fact_collector_1 = module_0.ServiceMgrFactCollector(bool_0)
        bytes_0 = b'l/A\x0e\xac\xe3'
        var_3 = service_mgr_fact_collector_1.collect(bytes_0)
        var_4 = service_mgr_fact_collector_1.is_systemd_managed_offline(int_0)
    except BaseException:
        pass