# Automatically generated by Pynguin.
import ansible.module_utils.facts.ansible_collector as module_0

def test_case_0():
    try:
        bytes_0 = b'S[\xbf\x16\x88^\xd6\x17\xad\x07pgG\t\xbe\xce\x88'
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(bytes_0)
        str_0 = 'ActionModule'
        dict_0 = {bytes_0: str_0, bytes_0: bytes_0, ansible_fact_collector_0: ansible_fact_collector_0}
        int_0 = 2619
        tuple_0 = (dict_0, int_0, ansible_fact_collector_0)
        var_0 = ansible_fact_collector_0.collect(str_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        set_0 = {collector_meta_data_collector_0, collector_meta_data_collector_0, collector_meta_data_collector_0}
        var_0 = collector_meta_data_collector_0.collect(set_0)
        var_1 = collector_meta_data_collector_0.collect()
        tuple_0 = ()
        str_0 = ']\\Zw}.t_e`'
        str_1 = 'j9% 94:nWzs,SV?a>R_'
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_0)
        str_2 = 'Iiw)?Xs3\'Lnse"lUR\''
        var_2 = module_0.get_ansible_collector(str_0, str_1, str_0, ansible_fact_collector_0, tuple_0, str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'I\x8d\xa7MJ\xcd\xa4\x8fP\r\n>'
        bool_0 = False
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(bool_0)
        dict_0 = {}
        var_0 = module_0.get_ansible_collector(bytes_0, collector_meta_data_collector_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_0)
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(bool_0, dict_0, collector_meta_data_collector_1)
        bytes_0 = b'\x9fC\xf3\x1d\x9a\x89'
        dict_1 = {bool_0: bool_0, bool_0: bytes_0, bool_0: bytes_0, bool_0: bytes_0}
        int_0 = 10240
        float_0 = -1101.079652
        set_0 = None
        collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(set_0)
        collector_meta_data_collector_3 = module_0.CollectorMetaDataCollector(dict_1, int_0, float_0, collector_meta_data_collector_2)
        str_0 = ',!ph5nBag!U{(,pX'
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(str_0)
        var_0 = collector_meta_data_collector_3.collect(ansible_fact_collector_1)
        bytes_1 = b'\xe1'
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(bytes_1)
        var_1 = ansible_fact_collector_2.collect(bool_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        bool_1 = True
        dict_0 = {bool_1: bool_1, bool_1: bool_0}
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(dict_0)
        str_0 = 'DyRfmC'
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(str_0)
        str_1 = '#bkxT#A;es\x0b0XzJvD4'
        tuple_0 = (str_0, str_1)
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(tuple_0)
        float_0 = 2509.429
        bytes_0 = b':\xa1\x94<C}\x90\x801=\x9eE=\xe2 '
        var_0 = module_0.get_ansible_collector(dict_0, float_0, bytes_0, bytes_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
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
        ansible_fact_collector_4 = module_0.AnsibleFactCollector()
        var_1 = module_0.get_ansible_collector(set_0, bool_0)
    except BaseException:
        pass