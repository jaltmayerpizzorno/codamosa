# Automatically generated by Pynguin.
import ansible.module_utils.facts.ansible_collector as module_0
import ansible.module_utils.facts.collector as module_1

def test_case_0():
    try:
        str_0 = ''
        set_0 = {str_0}
        bytes_0 = b'\xe2\xcdQ\x85\x7f>\xb7\x06\xa1p\x94\x85\x07eaP`\xb5\xdc\xa7'
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        str_1 = '9'
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(set_0, str_0, str_1)
        bool_0 = None
        var_0 = collector_meta_data_collector_0.collect(bool_0)
        ansible_fact_collector_1 = module_0.AnsibleFactCollector()
        list_0 = [ansible_fact_collector_1, bytes_0, str_0]
        var_1 = ansible_fact_collector_1.collect(list_0, list_0)
        var_2 = ansible_fact_collector_0.collect()
        base_fact_collector_0 = module_1.BaseFactCollector()
        ansible_fact_collector_2 = None
        var_3 = module_0.get_ansible_collector(base_fact_collector_0, ansible_fact_collector_2)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 657.45929
        list_0 = [float_0, float_0, float_0]
        int_0 = 329
        var_0 = module_0.get_ansible_collector(float_0, list_0, list_0, float_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        set_0 = {str_0}
        bytes_0 = b'\xe2\xcdQ\x85\x7f>\xb7\x06\xa1p\x94\x85\x07eaP`\xb5\xdc'
        list_0 = [bytes_0]
        int_0 = -2139
        str_1 = '^('
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(set_0, int_0, str_1)
        bool_0 = True
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(list_0, collector_meta_data_collector_0, bool_0)
        var_0 = ansible_fact_collector_0.collect()
    except BaseException:
        pass

def test_case_3():
    try:
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        str_0 = ''
        str_1 = "\n    Used to insert chunks of code into modules before transfer rather than\n    doing regular python imports.  This allows for more efficient transfer in\n    a non-bootstrapping scenario by not moving extra files over the wire and\n    also takes care of embedding arguments in the transferred modules.\n\n    This version is done in such a way that local imports can still be\n    used in the module code, so IDEs don't have to be aware of what is going on.\n\n    Example:\n\n    from ansible.module_utils.basic import *\n\n       ... will result in the insertion of basic.py into the module\n       from the module_utils/ directory in the source tree.\n\n    For powershell, this code effectively no-ops, as the exec wrapper requires access to a number of\n    properties not available here.\n\n    "
        var_0 = module_0.get_ansible_collector(str_0, str_1)
        str_2 = 'p7QjHOIKq>7T1N\nbb(|}'
        dict_0 = {str_2: str_2, str_2: str_2}
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(dict_0)
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector()
        list_0 = [collector_meta_data_collector_1]
        float_0 = None
        var_1 = module_0.get_ansible_collector(list_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        set_0 = {str_0}
        bytes_0 = b'\xe2\xcdQ\x85\x7f>\xb7\x06\xa1p\x94\x85\x07eaP`\xb5\xdc'
        int_0 = 126
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        var_0 = collector_meta_data_collector_0.collect(collector_meta_data_collector_0)
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(int_0)
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(bytes_0)
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(set_0)
        bool_0 = None
        var_1 = collector_meta_data_collector_1.collect(bool_0)
        ansible_fact_collector_2 = module_0.AnsibleFactCollector()
        list_0 = [ansible_fact_collector_1, bytes_0, str_0]
        var_2 = collector_meta_data_collector_0.collect()
        var_3 = ansible_fact_collector_2.collect(list_0, list_0)
        var_4 = ansible_fact_collector_1.collect()
        var_5 = ansible_fact_collector_2.collect()
        var_6 = module_0.get_ansible_collector(str_0)
        var_7 = ansible_fact_collector_1.collect()
        ansible_fact_collector_3 = module_0.AnsibleFactCollector()
        bytes_1 = b'\xcc\xd1\xcc_; \x15\xd1\x82\x8b\x0b\xc3\xa4U"f&'
        float_0 = 3129.907571
        base_fact_collector_0 = module_1.BaseFactCollector()
        var_8 = module_0.get_ansible_collector(bool_0, float_0, base_fact_collector_0, bytes_1, list_0, collector_meta_data_collector_1)
    except BaseException:
        pass