# Automatically generated by Pynguin.
import ansible.module_utils.facts.ansible_collector as module_0

def test_case_0():
    try:
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        var_0 = module_0.get_ansible_collector(ansible_fact_collector_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1696.38352
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        ansible_fact_collector_1 = module_0.AnsibleFactCollector()
        bytes_0 = b'U\xf6\x0e\xc28\xd5\rqW\xbf<@\xcac'
        var_0 = module_0.get_ansible_collector(float_0, ansible_fact_collector_0, ansible_fact_collector_1, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 25
        dict_0 = None
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        tuple_0 = (ansible_fact_collector_0,)
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(int_0, tuple_0)
        set_0 = set()
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(tuple_0)
        var_0 = ansible_fact_collector_2.collect(set_0)
        ansible_fact_collector_3 = module_0.AnsibleFactCollector(dict_0)
        list_0 = [ansible_fact_collector_0, collector_meta_data_collector_0, ansible_fact_collector_2]
        ansible_fact_collector_4 = module_0.AnsibleFactCollector(list_0, dict_0)
        int_1 = 92
        str_0 = "~bnuh}'q[*;"
        bytes_0 = b'\x13\x9b\xa7}rn\xc2\xab\xaa\xbb\x1bR'
        var_1 = module_0.get_ansible_collector(int_1, str_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b"\xbe'\xa8^\xe0\\\xd7\xf2\xf4:a4\x93\x07"
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        int_0 = -1027
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(list_0, int_0)
        var_0 = collector_meta_data_collector_0.collect()
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(bytes_0)
        var_1 = ansible_fact_collector_0.collect()
        complex_0 = None
        var_2 = module_0.get_ansible_collector(complex_0, complex_0)
        var_3 = ansible_fact_collector_0.collect()
        int_1 = 331
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(int_1)
        ansible_fact_collector_2 = module_0.AnsibleFactCollector()
        dict_0 = {}
        str_0 = 'lI2jCo T'
        float_0 = -1087.947
        var_4 = module_0.get_ansible_collector(bytes_0, dict_0, str_0, str_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\x19\x84I2\xc5\x19\xc7\xba\x89j)\xe3'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        int_0 = -1027
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(list_0, int_0)
        var_0 = collector_meta_data_collector_0.collect()
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(bytes_0)
        var_1 = ansible_fact_collector_1.collect()
        complex_0 = None
        var_2 = module_0.get_ansible_collector(complex_0, complex_0)
        var_3 = ansible_fact_collector_1.collect()
        int_1 = 331
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(int_1)
        var_4 = ansible_fact_collector_0.collect()
        tuple_0 = (ansible_fact_collector_2,)
        var_5 = module_0.get_ansible_collector(tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 4117
        str_0 = '*'
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(int_0, str_0)
        bytes_0 = b"\xbe'\xa8^\xe0\\\xd7\xf2\xf4:a4\x93\x07"
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        int_1 = -1027
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(list_0, int_1)
        var_0 = collector_meta_data_collector_1.collect()
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(bytes_0)
        var_1 = ansible_fact_collector_1.collect()
        complex_0 = None
        var_2 = module_0.get_ansible_collector(complex_0, complex_0)
        var_3 = ansible_fact_collector_1.collect()
        dict_0 = {int_1: ansible_fact_collector_1}
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(complex_0, dict_0)
        str_1 = '*'
        ansible_fact_collector_3 = module_0.AnsibleFactCollector(str_1, collector_meta_data_collector_1, str_1)
        var_4 = ansible_fact_collector_3.collect()
        var_5 = module_0.get_ansible_collector(str_1, ansible_fact_collector_3, ansible_fact_collector_3)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b"\xbe'\xa8^\xe0\\\xd7\xf2\xf4:a4\x93\x07"
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        int_0 = -1027
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(list_0, int_0)
        var_0 = collector_meta_data_collector_0.collect()
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        ansible_fact_collector_1 = module_0.AnsibleFactCollector()
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(bytes_0)
        var_1 = collector_meta_data_collector_0.collect()
        var_2 = ansible_fact_collector_2.collect()
        complex_0 = None
        var_3 = ansible_fact_collector_1.collect()
        var_4 = module_0.get_ansible_collector(complex_0, complex_0)
        var_5 = ansible_fact_collector_2.collect()
        dict_0 = {int_0: ansible_fact_collector_2}
        ansible_fact_collector_3 = module_0.AnsibleFactCollector(complex_0, dict_0)
        str_0 = 'k8'
        str_1 = 'GG7'
        ansible_fact_collector_4 = module_0.AnsibleFactCollector(str_0, collector_meta_data_collector_0, str_1)
        ansible_fact_collector_5 = module_0.AnsibleFactCollector()
        var_6 = ansible_fact_collector_4.collect()
        var_7 = collector_meta_data_collector_0.collect(ansible_fact_collector_0)
        float_0 = -102.650957
        bool_0 = False
        tuple_0 = (bool_0,)
        var_8 = module_0.get_ansible_collector(tuple_0, bool_0, tuple_0, list_0, collector_meta_data_collector_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 4117
        str_0 = 'k'
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(int_0, str_0)
        bytes_0 = b"\xbe'\xa8^\xe0\\\xd7\xf2\xf4:a4\x93\x07"
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        int_1 = -1027
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(list_0, int_1)
        var_0 = collector_meta_data_collector_1.collect()
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        ansible_fact_collector_1 = module_0.AnsibleFactCollector()
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(bytes_0)
        var_1 = ansible_fact_collector_2.collect()
        complex_0 = None
        var_2 = module_0.get_ansible_collector(complex_0, complex_0)
        var_3 = ansible_fact_collector_2.collect()
        dict_0 = {int_1: ansible_fact_collector_2}
        ansible_fact_collector_3 = module_0.AnsibleFactCollector(complex_0, dict_0)
        str_1 = 'k8'
        ansible_fact_collector_4 = module_0.AnsibleFactCollector(str_1, collector_meta_data_collector_1, int_1)
        var_4 = ansible_fact_collector_4.collect()
    except BaseException:
        pass