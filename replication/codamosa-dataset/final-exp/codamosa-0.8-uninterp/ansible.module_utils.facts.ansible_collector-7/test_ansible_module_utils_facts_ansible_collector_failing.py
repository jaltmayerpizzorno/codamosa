# Automatically generated by Pynguin.
import ansible.module_utils.facts.ansible_collector as module_0

def test_case_0():
    try:
        float_0 = 1330.2
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(float_0)
        var_0 = module_0.get_ansible_collector(ansible_fact_collector_0, float_0, ansible_fact_collector_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = None
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(bytes_0, bytes_0)
        bool_0 = True
        set_0 = {bool_0, bool_0, bool_0}
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        dict_0 = {collector_meta_data_collector_0: bool_0, ansible_fact_collector_0: set_0}
        var_0 = collector_meta_data_collector_0.collect(dict_0)
        bool_1 = True
        var_1 = module_0.get_ansible_collector(dict_0, dict_0, bool_1)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 705.171898
        str_0 = 'X5}H\tORp'
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        list_0 = [str_0]
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_0, list_0)
        var_0 = collector_meta_data_collector_0.collect()
        bytes_0 = b''
        bool_0 = True
        str_1 = 'u\n(&eQ)'
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(float_0, bytes_0, str_1)
        dict_0 = {bytes_0: float_0}
        var_1 = module_0.get_ansible_collector(collector_meta_data_collector_0, bytes_0, bool_0, list_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -402
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(int_0)
        float_0 = -3895.821
        var_0 = module_0.get_ansible_collector(collector_meta_data_collector_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 360
        set_0 = {int_0}
        bool_0 = True
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(set_0, bool_0)
        set_1 = None
        str_0 = 'vars_cache'
        dict_0 = {int_0: set_1, collector_meta_data_collector_0: set_0, bool_0: collector_meta_data_collector_0}
        float_0 = 1702.0244
        var_0 = module_0.get_ansible_collector(collector_meta_data_collector_0, set_1, str_0, dict_0, collector_meta_data_collector_0, float_0)
    except BaseException:
        pass