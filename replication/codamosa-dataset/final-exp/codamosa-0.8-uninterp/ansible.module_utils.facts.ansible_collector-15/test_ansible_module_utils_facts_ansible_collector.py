# Automatically generated by Pynguin.
import ansible.module_utils.facts.ansible_collector as module_0
import ansible.module_utils.facts.collector as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'L[_P\x0cec\nt'
    list_0 = None
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_0, list_0)

def test_case_2():
    str_0 = 'w'
    bool_0 = False
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_0, bool_0, str_0)
    int_0 = 2117
    var_0 = ansible_fact_collector_0.collect(int_0)

def test_case_3():
    bytes_0 = b'\'I\x17\xea\xd7\xa1e\xc5\xe6\x97T\xdd"\xd3\xdb'
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(bytes_0)
    var_0 = ansible_fact_collector_0.collect()

def test_case_4():
    str_0 = ' o2(OY'
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_0)
    list_0 = [ansible_fact_collector_0]
    bool_0 = True
    set_0 = {ansible_fact_collector_0}
    ansible_fact_collector_1 = module_0.AnsibleFactCollector(list_0, bool_0, set_0)
    tuple_0 = (ansible_fact_collector_1,)
    ansible_fact_collector_2 = module_0.AnsibleFactCollector(tuple_0)
    var_0 = ansible_fact_collector_2.collect()
    ansible_fact_collector_3 = module_0.AnsibleFactCollector()

def test_case_5():
    collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
    int_0 = 4267
    var_0 = collector_meta_data_collector_0.collect(int_0)

def test_case_6():
    bool_0 = None
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
    var_0 = module_0.get_ansible_collector(bool_0, dict_0, collector_meta_data_collector_0)

def test_case_7():
    str_0 = 'q@qaL$'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    int_0 = 2628
    list_0 = [dict_0, dict_0, str_0, dict_0]
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(dict_0, int_0, list_0)
    var_0 = ansible_fact_collector_0.collect(str_0)

def test_case_8():
    collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
    tuple_0 = ()
    str_0 = '*'
    bool_0 = False
    ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_0, bool_0, str_0)
    base_fact_collector_0 = module_1.BaseFactCollector()
    int_0 = 2131
    var_0 = ansible_fact_collector_0.collect(int_0)
    collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector()
    var_1 = collector_meta_data_collector_1.collect()
    base_fact_collector_1 = module_1.BaseFactCollector()
    list_0 = [base_fact_collector_0, int_0, bool_0, tuple_0]
    var_2 = base_fact_collector_0.collect(list_0, base_fact_collector_0)
    ansible_fact_collector_1 = module_0.AnsibleFactCollector()
    int_1 = -305
    base_fact_collector_2 = module_1.BaseFactCollector()
    collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(int_1, base_fact_collector_2)
    var_3 = collector_meta_data_collector_2.collect()
    complex_0 = None
    float_0 = 2.0
    bool_1 = True
    var_4 = module_0.get_ansible_collector(complex_0, float_0, bool_1)