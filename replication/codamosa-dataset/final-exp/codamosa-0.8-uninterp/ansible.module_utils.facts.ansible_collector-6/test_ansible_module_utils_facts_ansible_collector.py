# Automatically generated by Pynguin.
import ansible.module_utils.facts.ansible_collector as module_0

def test_case_0():
    pass

def test_case_1():
    ansible_fact_collector_0 = module_0.AnsibleFactCollector()

def test_case_2():
    bytes_0 = b'\xc1\x186m\xb9B\xc5a\xddo\xcc \xe6\x99\xf3'
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(bytes_0)
    var_0 = ansible_fact_collector_0.collect()

def test_case_3():
    str_0 = 'L(~|X G'
    tuple_0 = None
    collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(tuple_0)
    list_0 = [collector_meta_data_collector_0, collector_meta_data_collector_0, collector_meta_data_collector_0]
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(list_0)
    var_0 = ansible_fact_collector_0.collect(str_0)

def test_case_4():
    collector_meta_data_collector_0 = None
    collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_0)

def test_case_5():
    collector_meta_data_collector_0 = None
    collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_0)
    var_0 = collector_meta_data_collector_1.collect()

def test_case_6():
    str_0 = 'Vq+~o3-mp\rSLs\\]ad._%'
    collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(str_0)
    list_0 = [collector_meta_data_collector_0, collector_meta_data_collector_0, str_0, str_0]
    var_0 = collector_meta_data_collector_0.collect()
    var_1 = collector_meta_data_collector_0.collect()
    ansible_fact_collector_0 = module_0.AnsibleFactCollector()
    set_0 = {collector_meta_data_collector_0, ansible_fact_collector_0, ansible_fact_collector_0, collector_meta_data_collector_0}
    tuple_0 = (collector_meta_data_collector_0,)
    str_1 = '2'
    ansible_fact_collector_1 = module_0.AnsibleFactCollector(set_0, tuple_0, str_1)
    var_2 = ansible_fact_collector_1.collect(list_0)

def test_case_7():
    str_0 = 'Vq+~o3-mp\rSLs\\]ad._%'
    collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(str_0)
    list_0 = [str_0, collector_meta_data_collector_0, collector_meta_data_collector_0, str_0, str_0]
    dict_0 = {str_0: collector_meta_data_collector_0, str_0: list_0}
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(list_0, str_0, dict_0)
    var_0 = ansible_fact_collector_0.collect()

def test_case_8():
    str_0 = 'Vq+~o3-mp\rSLs\\]ad._%'
    collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(str_0)
    list_0 = [collector_meta_data_collector_0, collector_meta_data_collector_0, str_0, str_0]
    var_0 = collector_meta_data_collector_0.collect()
    var_1 = collector_meta_data_collector_0.collect()
    ansible_fact_collector_0 = module_0.AnsibleFactCollector()
    set_0 = {collector_meta_data_collector_0, ansible_fact_collector_0, str_0, ansible_fact_collector_0, collector_meta_data_collector_0}
    tuple_0 = (collector_meta_data_collector_0,)
    str_1 = '2'
    ansible_fact_collector_1 = module_0.AnsibleFactCollector(set_0, tuple_0, str_1)
    var_2 = ansible_fact_collector_1.collect(list_0)

def test_case_9():
    str_0 = '*'
    collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(str_0)
    list_0 = [str_0, collector_meta_data_collector_0, collector_meta_data_collector_0, str_0, str_0]
    dict_0 = {str_0: collector_meta_data_collector_0, str_0: list_0}
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(list_0, str_0, dict_0)
    ansible_fact_collector_1 = module_0.AnsibleFactCollector()
    float_0 = -234.322287
    var_0 = ansible_fact_collector_0.collect(float_0)