# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.service_mgr as module_0

def test_case_0():
    try:
        bool_0 = False
        str_0 = 'Id%"{\x0c* u'
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(str_0)
        var_0 = service_mgr_fact_collector_0.is_systemd_managed(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        str_0 = 'DMH&~]p'
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(str_0)
        var_0 = service_mgr_fact_collector_0.is_systemd_managed_offline(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.collect(service_mgr_fact_collector_0, service_mgr_fact_collector_0)
    except BaseException:
        pass