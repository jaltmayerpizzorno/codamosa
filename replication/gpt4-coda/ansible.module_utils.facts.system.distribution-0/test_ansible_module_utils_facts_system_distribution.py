# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.distribution as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    distribution_files_0 = module_0.DistributionFiles(list_0)
    var_0 = distribution_files_0.process_dist_files()

def test_case_2():
    str_0 = 'NA'
    set_0 = {str_0, str_0, str_0}
    int_0 = 649
    list_0 = []
    float_0 = 3436.66905
    distribution_files_0 = module_0.DistributionFiles(float_0)
    var_0 = distribution_files_0.parse_distribution_file_Slackware(set_0, set_0, int_0, list_0)

def test_case_3():
    bool_0 = True
    list_0 = []
    dict_0 = {bool_0: list_0}
    int_0 = 3042
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    distribution_files_0 = module_0.DistributionFiles(distribution_fact_collector_0)
    var_0 = distribution_files_0.parse_distribution_file_OpenWrt(list_0, dict_0, int_0, dict_0)
    distribution_fact_collector_1 = module_0.DistributionFactCollector(bool_0)

def test_case_4():
    distribution_fact_collector_0 = None
    distribution_fact_collector_1 = module_0.DistributionFactCollector()
    set_0 = {distribution_fact_collector_1, distribution_fact_collector_0, distribution_fact_collector_0, distribution_fact_collector_1}
    bytes_0 = b'q\x85)9)\x98\x89'
    str_0 = 'rmdir'
    distribution_files_0 = module_0.DistributionFiles(str_0)
    var_0 = distribution_files_0.parse_distribution_file_Debian(distribution_fact_collector_0, set_0, bytes_0, bytes_0)

def test_case_5():
    list_0 = None
    distribution_files_0 = module_0.DistributionFiles(list_0)
    str_0 = '\x0c8R'
    int_0 = -3343
    bytes_0 = b"G\xea\x08\x9e\xc9\x08t'\x8b"
    str_1 = 'D`JJ'
    distribution_files_1 = module_0.DistributionFiles(str_1)
    var_0 = distribution_files_1.parse_distribution_file_Mandriva(distribution_files_0, str_0, int_0, bytes_0)

def test_case_6():
    float_0 = 1273.11
    complex_0 = None
    distribution_0 = module_0.Distribution(complex_0)
    set_0 = set()
    str_0 = 'v6&MNq,u#HTw?~+>t>'
    bool_0 = True
    distribution_files_0 = module_0.DistributionFiles(bool_0)
    var_0 = distribution_files_0.parse_distribution_file_Coreos(float_0, distribution_0, set_0, str_0)

def test_case_7():
    float_0 = 1.0
    distribution_0 = module_0.Distribution(float_0)
    distribution_files_0 = module_0.DistributionFiles(distribution_0)
    str_0 = '\\7I\n~f$O\n[8mqO['
    distribution_files_1 = module_0.DistributionFiles(str_0)
    var_0 = distribution_files_1.parse_distribution_file_CentOS(distribution_files_0, str_0, float_0, distribution_0)
    distribution_fact_collector_0 = module_0.DistributionFactCollector()

def test_case_8():
    bool_0 = True
    distribution_0 = module_0.Distribution(bool_0)
    var_0 = distribution_0.get_distribution_facts()

def test_case_9():
    float_0 = -3365.05139
    distribution_0 = module_0.Distribution(float_0)
    distribution_1 = module_0.Distribution(distribution_0)
    var_0 = distribution_1.get_distribution_SMGL()

def test_case_10():
    float_0 = None
    str_0 = 'GDHM_ldoI>'
    distribution_fact_collector_0 = module_0.DistributionFactCollector(str_0)
    var_0 = distribution_fact_collector_0.collect(float_0)

def test_case_11():
    list_0 = []
    distribution_0 = module_0.Distribution(list_0)
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    bytes_0 = b'b+\xf2&\xafM\xbc\xf4\xac\x95\x00\x1d\xcb\xe0'
    var_0 = distribution_fact_collector_0.collect(bytes_0)
    var_1 = distribution_0.get_distribution_facts()

def test_case_12():
    int_0 = 353
    distribution_0 = module_0.Distribution(int_0)
    var_0 = distribution_0.get_distribution_FreeBSD()

def test_case_13():
    str_0 = 'A:J-GTs\x0c<n&x@Id1wp@v'
    dict_0 = None
    distribution_0 = None
    float_0 = 952.60834
    distribution_files_0 = module_0.DistributionFiles(float_0)
    var_0 = distribution_files_0.parse_distribution_file_Flatcar(str_0, dict_0, distribution_0, dict_0)

def test_case_14():
    str_0 = '~%5U+<\nsn'
    distribution_files_0 = module_0.DistributionFiles(str_0)
    set_0 = {str_0, distribution_files_0, str_0}
    tuple_0 = ()
    tuple_1 = (set_0, tuple_0, tuple_0)
    bytes_0 = b"Csh\xa4a\xf2\xfdf\xff\xac'\xcd\xe4lw7\xab&\xd2"
    distribution_0 = module_0.Distribution(tuple_1)
    tuple_2 = (bytes_0, distribution_0, bytes_0)
    var_0 = distribution_files_0.parse_distribution_file_NA(tuple_1, str_0, str_0, tuple_2)
    var_1 = distribution_0.get_distribution_facts()