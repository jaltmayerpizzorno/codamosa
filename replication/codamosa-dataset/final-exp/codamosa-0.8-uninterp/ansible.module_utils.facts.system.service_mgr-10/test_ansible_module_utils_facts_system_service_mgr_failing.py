# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.service_mgr as module_0

def test_case_0():
    try:
        bytes_0 = b'N\x10\r\x8c8'
        bytes_1 = b''
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(bytes_1)
        var_0 = service_mgr_fact_collector_0.is_systemd_managed(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'b^1 (PmE'
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(str_0)
        str_1 = 'Dr<(-'
        tuple_0 = ()
        service_mgr_fact_collector_1 = module_0.ServiceMgrFactCollector(tuple_0)
        var_0 = service_mgr_fact_collector_1.is_systemd_managed_offline(str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        str_0 = 'RETURN'
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(str_0)
        service_mgr_fact_collector_1 = module_0.ServiceMgrFactCollector(bool_0, service_mgr_fact_collector_0)
        bytes_0 = b'{\xf0\xc0:A\xda\x9a\x1d\xc9}\x94<'
        dict_0 = {str_0: bytes_0, bytes_0: str_0}
        service_mgr_fact_collector_2 = module_0.ServiceMgrFactCollector(bytes_0)
        var_0 = service_mgr_fact_collector_2.collect(dict_0, str_0)
    except BaseException:
        pass