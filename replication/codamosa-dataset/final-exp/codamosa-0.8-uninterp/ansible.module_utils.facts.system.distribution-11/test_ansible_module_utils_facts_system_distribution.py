# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.distribution as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Wu 3K%CNt:IRp'
    distribution_files_0 = module_0.DistributionFiles(str_0)
    var_0 = distribution_files_0.process_dist_files()

def test_case_2():
    str_0 = ' validation that is done at parse time, not load time '
    dict_0 = {str_0: str_0}
    distribution_0 = module_0.Distribution(dict_0)
    dict_1 = {}
    distribution_files_0 = module_0.DistributionFiles(dict_1)
    var_0 = distribution_files_0.parse_distribution_file_Slackware(str_0, str_0, distribution_0, distribution_0)

def test_case_3():
    bytes_0 = b'o&C\x8f\xc1\x9b\xe3S\xf9\x0b\xe6'
    str_0 = 'xQf)vv'
    set_0 = {bytes_0}
    distribution_files_0 = module_0.DistributionFiles(set_0)
    bool_0 = True
    tuple_0 = ()
    float_0 = 274.94
    distribution_files_1 = module_0.DistributionFiles(float_0)
    var_0 = distribution_files_1.parse_distribution_file_Coreos(str_0, distribution_files_0, bool_0, tuple_0)
    str_1 = '\tK(='
    bool_1 = True
    bool_2 = True
    distribution_0 = module_0.Distribution(bool_2)
    dict_0 = {distribution_0: bool_2, distribution_0: bool_2}
    distribution_files_2 = module_0.DistributionFiles(dict_0)
    var_1 = distribution_files_2.parse_distribution_file_OpenWrt(bytes_0, str_1, bool_1, bytes_0)

def test_case_4():
    int_0 = None
    distribution_files_0 = module_0.DistributionFiles(int_0)
    list_0 = [int_0, int_0]
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    set_0 = set()
    distribution_0 = module_0.Distribution(set_0)
    distribution_files_1 = module_0.DistributionFiles(distribution_0)
    dict_0 = {distribution_files_1: distribution_files_1, distribution_0: distribution_0, distribution_0: distribution_0}
    distribution_files_2 = module_0.DistributionFiles(dict_0)
    var_0 = distribution_files_2.parse_distribution_file_CentOS(distribution_files_0, list_0, list_0, distribution_fact_collector_0)
    bool_0 = False
    distribution_1 = module_0.Distribution(bool_0)
    distribution_files_3 = module_0.DistributionFiles(distribution_1)
    set_1 = {bool_0, bool_0}
    bool_1 = False
    int_1 = -2177
    list_1 = [int_1, int_1, int_1, int_1]
    tuple_0 = ()
    str_0 = "p@*'^ModvrZ&\x0b_Om}"
    float_0 = 1844.0
    dict_1 = {}
    distribution_fact_collector_1 = module_0.DistributionFactCollector()
    var_1 = distribution_files_3.parse_distribution_file_OpenWrt(float_0, dict_1, str_0, distribution_fact_collector_1)
    float_1 = -7.1
    var_2 = distribution_files_3.parse_distribution_file_Debian(tuple_0, str_0, float_1, set_1)
    distribution_files_4 = module_0.DistributionFiles(list_1)
    var_3 = distribution_files_4.parse_distribution_file_Alpine(distribution_files_3, set_1, bool_1, distribution_files_3)

def test_case_5():
    distribution_0 = None
    distribution_files_0 = module_0.DistributionFiles(distribution_0)
    str_0 = 'coreos'
    set_0 = {distribution_files_0}
    dict_0 = {}
    str_1 = 'mwImQ.I/lUNk_'
    distribution_files_1 = module_0.DistributionFiles(str_1)
    var_0 = distribution_files_1.parse_distribution_file_Mandriva(distribution_files_0, str_0, set_0, dict_0)
    distribution_fact_collector_0 = module_0.DistributionFactCollector()

def test_case_6():
    int_0 = 267
    str_0 = 'ApKLgoQ'
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    list_0 = [int_0]
    bytes_0 = b'\xa2N\xff:\x9d\\b\xf4'
    distribution_files_0 = module_0.DistributionFiles(bytes_0)
    var_0 = distribution_files_0.parse_distribution_file_NA(int_0, str_0, distribution_fact_collector_0, list_0)

def test_case_7():
    bool_0 = False
    str_0 = '(wVpv<BF2'
    float_0 = 2848.0
    distribution_files_0 = module_0.DistributionFiles(float_0)
    int_0 = 3120
    distribution_files_1 = module_0.DistributionFiles(int_0)
    var_0 = distribution_files_1.parse_distribution_file_Coreos(bool_0, str_0, float_0, distribution_files_0)

def test_case_8():
    float_0 = -2448.55933
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    dict_0 = {distribution_fact_collector_0: distribution_fact_collector_0, distribution_fact_collector_0: float_0, distribution_fact_collector_0: float_0, distribution_fact_collector_0: float_0}
    str_0 = None
    float_1 = -13.4222
    set_0 = {float_1, float_1}
    distribution_files_0 = module_0.DistributionFiles(set_0)
    var_0 = distribution_files_0.parse_distribution_file_Flatcar(float_0, distribution_fact_collector_0, dict_0, str_0)

def test_case_9():
    str_0 = 'Linux'
    bool_0 = False
    bool_1 = False
    list_0 = [bool_1]
    float_0 = -213.305009
    distribution_files_0 = module_0.DistributionFiles(float_0)
    var_0 = distribution_files_0.parse_distribution_file_ClearLinux(str_0, bool_0, bool_1, list_0)

def test_case_10():
    bytes_0 = None
    tuple_0 = (bytes_0,)
    distribution_files_0 = module_0.DistributionFiles(tuple_0)
    distribution_files_1 = module_0.DistributionFiles(distribution_files_0)
    str_0 = '<1g.hSKG'
    int_0 = 6564
    list_0 = []
    var_0 = distribution_files_0.parse_distribution_file_CentOS(distribution_files_1, str_0, int_0, list_0)

def test_case_11():
    bytes_0 = b'_'
    distribution_0 = module_0.Distribution(bytes_0)
    var_0 = distribution_0.get_distribution_FreeBSD()

def test_case_12():
    str_0 = 'NE"1s0P>H9T|cJ'
    distribution_0 = module_0.Distribution(str_0)
    var_0 = distribution_0.get_distribution_facts()

def test_case_13():
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    var_0 = distribution_fact_collector_0.collect()

def test_case_14():
    str_0 = '/L|exk7\x0c4F%F9'
    distribution_fact_collector_0 = module_0.DistributionFactCollector(str_0)
    var_0 = distribution_fact_collector_0.collect(distribution_fact_collector_0)
    str_1 = 'u5Ssd<Df.Zf<Y$@'
    distribution_files_0 = module_0.DistributionFiles(str_1)

def test_case_15():
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    int_0 = 821
    list_0 = []
    bytes_0 = b''
    distribution_0 = module_0.Distribution(bytes_0)
    distribution_files_0 = module_0.DistributionFiles(distribution_0)
    bytes_1 = b'\xb0\x0f\xd0\xb4>J\xd0'
    float_0 = 2462.760083
    var_0 = distribution_fact_collector_0.collect(float_0)
    distribution_files_1 = module_0.DistributionFiles(bytes_1)
    set_0 = {distribution_fact_collector_0, distribution_files_1, bytes_1}
    distribution_files_2 = module_0.DistributionFiles(set_0)
    var_1 = distribution_files_2.parse_distribution_file_Flatcar(list_0, distribution_files_0, int_0, distribution_files_0)
    distribution_fact_collector_1 = module_0.DistributionFactCollector(int_0)
    str_0 = 'D+Tg3k?*()\x0c{O--"'
    tuple_0 = (str_0, distribution_0)
    var_2 = distribution_fact_collector_0.collect(tuple_0, float_0)
    var_3 = distribution_fact_collector_1.collect(distribution_fact_collector_0)

def test_case_16():
    str_0 = '::D1Af;lCX\\BNQVgZ&='
    float_0 = None
    bytes_0 = None
    bool_0 = False
    distribution_files_0 = module_0.DistributionFiles(bool_0)
    var_0 = distribution_files_0.parse_distribution_file_Debian(float_0, str_0, bytes_0, bytes_0)