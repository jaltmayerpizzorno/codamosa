# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.service_mgr as module_0

def test_case_0():
    try:
        str_0 = 'fXe\x0bHCd'
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.is_systemd_managed(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 5975
        set_0 = {int_0}
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.is_systemd_managed_offline(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2477.5
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        bool_0 = True
        set_0 = {bool_0}
        service_mgr_fact_collector_1 = module_0.ServiceMgrFactCollector(bool_0, set_0)
        var_0 = service_mgr_fact_collector_1.collect(float_0, service_mgr_fact_collector_0)
    except BaseException:
        pass