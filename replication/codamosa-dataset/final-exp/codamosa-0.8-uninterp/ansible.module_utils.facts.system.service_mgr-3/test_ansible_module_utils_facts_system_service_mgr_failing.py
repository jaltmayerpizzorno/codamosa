# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.service_mgr as module_0

def test_case_0():
    try:
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        str_0 = '8P? pLoJ= oroU#'
        bool_0 = None
        tuple_0 = (str_0, bool_0)
        var_0 = service_mgr_fact_collector_0.is_systemd_managed(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        float_0 = 898.30556
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(float_0)
        var_0 = service_mgr_fact_collector_0.is_systemd_managed_offline(bool_0)
    except BaseException:
        pass