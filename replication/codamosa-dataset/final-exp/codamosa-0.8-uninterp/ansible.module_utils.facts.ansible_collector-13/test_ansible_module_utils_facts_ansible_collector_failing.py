# Automatically generated by Pynguin.
import ansible.module_utils.facts.ansible_collector as module_0

def test_case_0():
    try:
        str_0 = '*'
        var_0 = module_0.get_ansible_collector(str_0, str_0, str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'i\x88\xf5\xb0sT\x019nq\xf2\xbazNHg\xd5\xc8'
        str_0 = '*'
        set_0 = {str_0}
        str_1 = 'cI) \x0c"o'
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(set_0, str_1)
        list_0 = [str_0, str_1, str_1, str_0]
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(str_1, ansible_fact_collector_0, list_0)
        var_0 = ansible_fact_collector_1.collect(bytes_0)
        ansible_fact_collector_2 = module_0.AnsibleFactCollector()
        list_1 = [ansible_fact_collector_2, ansible_fact_collector_2, ansible_fact_collector_2]
        ansible_fact_collector_3 = module_0.AnsibleFactCollector(ansible_fact_collector_2, list_1)
        var_1 = ansible_fact_collector_0.collect(ansible_fact_collector_3)
        int_0 = 131072
        var_2 = ansible_fact_collector_2.collect(int_0)
        var_3 = ansible_fact_collector_2.collect()
        str_2 = 'YDI\rd$'
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_0, str_2)
        dict_0 = {ansible_fact_collector_3: ansible_fact_collector_3, ansible_fact_collector_2: ansible_fact_collector_2, ansible_fact_collector_2: list_1, ansible_fact_collector_2: list_1}
        var_4 = module_0.get_ansible_collector(dict_0, ansible_fact_collector_3)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 161
        int_1 = -1979
        list_0 = [int_1]
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(list_0, list_0)
        var_0 = ansible_fact_collector_0.collect(int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        str_0 = 'Publish a collection artifact to Ansible Galaxy.'
        collector_meta_data_collector_0 = None
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(str_0, collector_meta_data_collector_0)
        bytes_0 = b'i\x88\xf5\xb0sT\x019nq\xf2\xbazNHg\xd5\xc8'
        str_1 = 'bUU[:xU'
        str_2 = '~|'
        bool_0 = True
        tuple_0 = (str_2, bool_0)
        var_0 = ansible_fact_collector_0.collect()
        collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(tuple_0)
        var_1 = ansible_fact_collector_0.collect(str_1)
        tuple_1 = ()
        var_2 = module_0.get_ansible_collector(tuple_1)
        var_3 = ansible_fact_collector_0.collect()
        str_3 = 'x.,a1R\\Bp'
        set_0 = {collector_meta_data_collector_1, str_0, str_0, var_2}
        str_4 = 'r6o#6|+\n_'
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(set_0, str_4)
        list_0 = [str_3, str_4, str_4, str_3]
        collector_meta_data_collector_3 = module_0.CollectorMetaDataCollector()
        var_4 = collector_meta_data_collector_3.collect(set_0)
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(str_3, ansible_fact_collector_1, list_0)
        var_5 = ansible_fact_collector_2.collect(bytes_0)
        ansible_fact_collector_3 = module_0.AnsibleFactCollector()
        list_1 = [ansible_fact_collector_3, ansible_fact_collector_0, collector_meta_data_collector_0]
        var_6 = ansible_fact_collector_0.collect()
        ansible_fact_collector_4 = module_0.AnsibleFactCollector(ansible_fact_collector_3, list_1)
        var_7 = ansible_fact_collector_1.collect(ansible_fact_collector_4)
        int_0 = 131095
        var_8 = ansible_fact_collector_3.collect(int_0)
        var_9 = collector_meta_data_collector_3.collect()
        var_10 = ansible_fact_collector_3.collect()
        collector_meta_data_collector_4 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_3, str_1)
        bool_1 = True
        float_0 = 992.228
        var_11 = module_0.get_ansible_collector(set_0, bool_1, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'i\x88\xf5\xb0sT\x019nq\xf2\xbazNHg\xd5\xc8'
        str_0 = '*'
        bool_0 = True
        set_0 = {str_0}
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(set_0, str_0)
        list_0 = [str_0, str_0, str_0, str_0]
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        dict_0 = {str_0: bool_0, collector_meta_data_collector_0: bool_0}
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(dict_0, ansible_fact_collector_0, str_0)
        var_0 = ansible_fact_collector_1.collect()
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector()
        var_1 = collector_meta_data_collector_1.collect(set_0)
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(str_0, ansible_fact_collector_0, list_0)
        var_2 = ansible_fact_collector_2.collect(bytes_0)
        ansible_fact_collector_3 = module_0.AnsibleFactCollector()
        list_1 = [set_0, set_0, ansible_fact_collector_3, ansible_fact_collector_3, ansible_fact_collector_3]
        ansible_fact_collector_4 = module_0.AnsibleFactCollector(ansible_fact_collector_3, list_1)
        var_3 = ansible_fact_collector_0.collect(ansible_fact_collector_4)
        var_4 = ansible_fact_collector_3.collect()
        str_1 = 'YDI\rd$'
        collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_1, str_1)
        dict_1 = {ansible_fact_collector_4: ansible_fact_collector_4, ansible_fact_collector_3: ansible_fact_collector_3, ansible_fact_collector_3: list_1, ansible_fact_collector_3: list_1}
        ansible_fact_collector_5 = module_0.AnsibleFactCollector()
        var_5 = module_0.get_ansible_collector(dict_1, ansible_fact_collector_4)
    except BaseException:
        pass