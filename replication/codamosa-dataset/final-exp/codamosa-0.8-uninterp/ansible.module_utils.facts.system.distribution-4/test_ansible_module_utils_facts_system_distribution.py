# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.distribution as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = -1124.0
    distribution_files_0 = module_0.DistributionFiles(float_0)
    var_0 = distribution_files_0.process_dist_files()

def test_case_2():
    str_0 = 'b\x0bBcUxK&q\r%u@K/H2'
    distribution_files_0 = module_0.DistributionFiles(str_0)

def test_case_3():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
    str_0 = '`\\A}`%CVPL\t>%a\\1J]Gj'
    list_0 = [str_0, str_0, tuple_0]
    str_1 = 'UT9O"`9.&ZxNCHsj8}n'
    distribution_files_0 = module_0.DistributionFiles(str_1)
    var_0 = distribution_files_0.parse_distribution_file_Slackware(dict_0, str_0, list_0, list_0)

def test_case_4():
    float_0 = 2205.661
    distribution_0 = module_0.Distribution(float_0)
    set_0 = {distribution_0}
    str_0 = "%:.Bs~'8?54\\d"
    list_0 = [set_0]
    bytes_0 = b'$\x1c\xe3O\x8e\x0f\xcd\x0b8\x1b\xbf\x98xZ\x97\xf5'
    distribution_files_0 = module_0.DistributionFiles(float_0)
    var_0 = distribution_files_0.parse_distribution_file_OpenWrt(set_0, str_0, list_0, bytes_0)
    var_1 = distribution_0.get_distribution_SMGL()

def test_case_5():
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    list_0 = None
    bytes_0 = b'\xe3)\x18\x8bl\xe0\xfbm\xc0\x1e\xf5g\x0cp\x8d\xef\xe9\xae\x04\x8b'
    float_0 = 1576.255432
    set_0 = set()
    distribution_files_0 = module_0.DistributionFiles(set_0)
    var_0 = distribution_files_0.parse_distribution_file_Alpine(distribution_fact_collector_0, list_0, bytes_0, float_0)

def test_case_6():
    str_0 = ''
    str_1 = '~C`SM, ,V-*\\7%*u=J'
    bool_0 = True
    bool_1 = True
    distribution_files_0 = module_0.DistributionFiles(bool_1)
    var_0 = distribution_files_0.parse_distribution_file_Mandriva(str_0, str_1, bool_0, str_1)

def test_case_7():
    bool_0 = False
    float_0 = 725.2
    int_0 = 4171
    distribution_0 = module_0.Distribution(int_0)
    var_0 = distribution_0.get_distribution_facts()
    var_1 = distribution_0.get_distribution_FreeBSD()
    str_0 = '3Dwjw_5ih[K'
    distribution_files_0 = module_0.DistributionFiles(str_0)
    var_2 = distribution_files_0.parse_distribution_file_NA(float_0, str_0, bool_0, distribution_files_0)

def test_case_8():
    list_0 = []
    distribution_0 = None
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    str_0 = 'PsmPf'
    int_0 = -1610
    list_1 = [int_0, int_0, int_0, int_0]
    distribution_files_0 = module_0.DistributionFiles(list_1)
    var_0 = distribution_files_0.parse_distribution_file_Coreos(list_0, distribution_0, distribution_fact_collector_0, str_0)

def test_case_9():
    float_0 = 0.2
    dict_0 = None
    distribution_files_0 = None
    bytes_0 = b',\x95.\xdd\xc8\xa3\x7f5\xba\x072\x167\xe7\x06\x91O7u'
    distribution_files_1 = module_0.DistributionFiles(float_0)
    var_0 = distribution_files_1.parse_distribution_file_Flatcar(float_0, dict_0, distribution_files_0, bytes_0)

def test_case_10():
    float_0 = -1141.0471813746242
    distribution_files_0 = module_0.DistributionFiles(float_0)
    str_0 = "EZQA'Htj;Q\x0cpkidw"
    str_1 = 'fVB9<-'
    bool_0 = False
    var_0 = distribution_files_0.parse_distribution_file_ClearLinux(str_0, str_1, bool_0, bool_0)

def test_case_11():
    bytes_0 = b'\xd6\xc1\xefx\x8c\x124'
    str_0 = 's\x0c>mh#*'
    tuple_0 = None
    int_0 = 1944
    bool_0 = True
    distribution_files_0 = module_0.DistributionFiles(bool_0)
    distribution_files_1 = module_0.DistributionFiles(distribution_files_0)
    var_0 = distribution_files_1.parse_distribution_file_CentOS(bytes_0, str_0, tuple_0, int_0)

def test_case_12():
    var_0 = None
    distribution_0 = module_0.Distribution(var_0)

def test_case_13():
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    str_0 = 'line is required with state=present'
    var_0 = distribution_fact_collector_0.collect(str_0)

def test_case_14():
    var_0 = None
    distribution_0 = module_0.Distribution(var_0)
    var_1 = distribution_0.get_distribution_FreeBSD()

def test_case_15():
    bool_0 = True
    str_0 = 'bulleye'
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    distribution_files_0 = module_0.DistributionFiles(dict_0)
    bool_1 = False
    var_0 = distribution_files_0.parse_distribution_file_Debian(bool_0, str_0, distribution_files_0, bool_1)

def test_case_16():
    str_0 = 'DISTRIB_RELEASE="14.07"\nDISTRIB_CODENAME="barrier_breaker"\nDISTRIB_TARGET="ramips/mt7621"\nDISTRIB_DESCRIPTION="OpenWrt Barrier Breaker 14.07"'
    str_1 = 'path'
    str_2 = 'distribution'
    str_3 = 'distribution_release'
    str_4 = 'distribution_version'
    str_5 = [str_2, str_3, str_4]
    distribution_files_0 = module_0.DistributionFiles(str_3)
    str_6 = 'OpenWrt'
    var_0 = distribution_files_0.parse_distribution_file_OpenWrt(str_6, str_0, str_1, str_5)