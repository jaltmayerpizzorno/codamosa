# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.distribution as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'*\xa1\xb6E\xd3\xf7\xb2\xe6\xf7\x9c\x8d\xa06l\xa6'
    distribution_files_0 = module_0.DistributionFiles(bytes_0)
    var_0 = distribution_files_0.process_dist_files()

def test_case_2():
    str_0 = 'Jrc'
    tuple_0 = (str_0,)
    tuple_1 = (tuple_0,)
    set_0 = None
    float_0 = None
    bool_0 = False
    distribution_files_0 = module_0.DistributionFiles(bool_0)
    var_0 = distribution_files_0.parse_distribution_file_OpenWrt(tuple_1, str_0, set_0, float_0)

def test_case_3():
    float_0 = -1853.9
    distribution_fact_collector_0 = module_0.DistributionFactCollector(float_0)
    str_0 = "P_vUYyJB-I?LT[}2']"
    tuple_0 = None
    var_0 = distribution_fact_collector_0.collect()
    int_0 = 1820
    distribution_files_0 = module_0.DistributionFiles(int_0)
    var_1 = distribution_files_0.parse_distribution_file_NA(float_0, str_0, tuple_0, tuple_0)
    var_2 = distribution_files_0.process_dist_files()

def test_case_4():
    bytes_0 = b'*\xa1\xb6E\xd3\xf7\xb2\xe6\xf7\x9c\x8d\xa06l\xa6'
    distribution_files_0 = module_0.DistributionFiles(bytes_0)
    tuple_0 = ()
    str_0 = '3W_Jx}&eSwtu'
    list_0 = [bytes_0, tuple_0, bytes_0]
    var_0 = distribution_files_0.parse_distribution_file_Coreos(str_0, tuple_0, str_0, list_0)

def test_case_5():
    int_0 = -698
    bool_0 = False
    str_0 = ''
    str_1 = '\\xT_'
    distribution_files_0 = module_0.DistributionFiles(str_1)
    var_0 = distribution_files_0.parse_distribution_file_Flatcar(int_0, bool_0, str_0, str_1)

def test_case_6():
    str_0 = "U8_`YG'vG*0"
    dict_0 = None
    str_1 = 'V-&h74wF,`J&\x0byBT'
    set_0 = None
    str_2 = 'Duqla'
    distribution_files_0 = module_0.DistributionFiles(str_2)
    var_0 = distribution_files_0.parse_distribution_file_ClearLinux(str_0, dict_0, str_1, set_0)

def test_case_7():
    set_0 = set()
    str_0 = '--gid-owner'
    str_1 = 'P\t""BhAKBM.E=I'
    bool_0 = False
    set_1 = {bool_0, bool_0, bool_0, bool_0}
    distribution_files_0 = module_0.DistributionFiles(set_1)
    var_0 = distribution_files_0.parse_distribution_file_CentOS(set_0, str_0, str_1, set_0)

def test_case_8():
    int_0 = -563
    distribution_0 = module_0.Distribution(int_0)
    var_0 = distribution_0.get_distribution_FreeBSD()

def test_case_9():
    str_0 = 'r>*Nm8'
    distribution_0 = module_0.Distribution(str_0)
    var_0 = distribution_0.get_distribution_facts()

def test_case_10():
    str_0 = '[uHYQfdG/'
    distribution_0 = module_0.Distribution(str_0)
    distribution_1 = module_0.Distribution(distribution_0)
    distribution_2 = module_0.Distribution(distribution_1)
    var_0 = distribution_2.get_distribution_SMGL()

def test_case_11():
    bytes_0 = b'*\xa1\xb6E\xd3\xf7\xb2\xe6\xf7\x9c\x8d\xa06l\xa6'
    distribution_files_0 = module_0.DistributionFiles(bytes_0)
    float_0 = -2610.0
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    var_0 = distribution_fact_collector_0.collect(float_0, float_0)
    set_0 = {distribution_files_0, distribution_fact_collector_0, bytes_0}
    var_1 = distribution_fact_collector_0.collect(set_0, distribution_files_0)

def test_case_12():
    bool_0 = False
    str_0 = "'name' is a required field for %s."
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    str_1 = '`b`1e\x0cAlb@@9"'
    var_0 = distribution_fact_collector_0.collect()
    var_1 = distribution_fact_collector_0.collect(str_1)
    distribution_fact_collector_1 = module_0.DistributionFactCollector(bool_0)
    distribution_files_0 = module_0.DistributionFiles(str_0)
    distribution_files_1 = module_0.DistributionFiles(distribution_files_0)

def test_case_13():
    str_0 = "NSpP]k'kE^u/L4"
    set_0 = {str_0}
    list_0 = [str_0, str_0, set_0, set_0]
    float_0 = 0.2
    distribution_files_0 = module_0.DistributionFiles(float_0)
    var_0 = distribution_files_0.parse_distribution_file_Mandriva(str_0, str_0, set_0, list_0)
    bool_0 = True
    distribution_fact_collector_0 = module_0.DistributionFactCollector(bool_0)

def test_case_14():
    str_0 = "U8_`YG'vG*0"
    set_0 = {str_0, str_0, str_0, str_0}
    bool_0 = False
    dict_0 = {bool_0: str_0}
    list_0 = [str_0, str_0, str_0, str_0]
    distribution_files_0 = module_0.DistributionFiles(list_0)
    var_0 = distribution_files_0.parse_distribution_file_Alpine(set_0, bool_0, dict_0, str_0)
    dict_1 = None
    str_1 = 'V-&h74wF,`J&\x0byBT'
    set_1 = None
    str_2 = 'Duqla'
    list_1 = [set_1, str_1, str_2]
    distribution_0 = module_0.Distribution(list_1)
    var_1 = distribution_0.get_distribution_facts()
    distribution_files_1 = module_0.DistributionFiles(str_2)
    var_2 = distribution_files_1.parse_distribution_file_ClearLinux(str_0, dict_1, str_1, set_1)