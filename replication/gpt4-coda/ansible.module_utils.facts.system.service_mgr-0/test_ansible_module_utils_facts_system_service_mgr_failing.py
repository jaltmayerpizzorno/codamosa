# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.service_mgr as module_0

def test_case_0():
    try:
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.collect(service_mgr_fact_collector_0)
        str_0 = ' kiL#^kM%"'
        var_1 = service_mgr_fact_collector_0.is_systemd_managed(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'W=:cb\t=q[k<'
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        service_mgr_fact_collector_1 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.is_systemd_managed_offline(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.collect(service_mgr_fact_collector_0)
        bytes_0 = b'zx[,:I\xcb@\x012T\xdd\x8c\x16\xe9\x07L86'
        list_0 = []
        tuple_0 = (list_0,)
        var_1 = service_mgr_fact_collector_0.collect(bytes_0, tuple_0)
    except BaseException:
        pass