# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.distribution as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -590
    distribution_files_0 = module_0.DistributionFiles(int_0)
    var_0 = distribution_files_0.process_dist_files()

def test_case_2():
    distribution_files_0 = None
    set_0 = {distribution_files_0}
    distribution_files_1 = module_0.DistributionFiles(set_0)
    distribution_fact_collector_0 = module_0.DistributionFactCollector(distribution_files_1)
    str_0 = '"=B]9dh\'aFfid1\x0bz'
    str_1 = 'vL?.Tkg%z23",'
    bytes_0 = b'\xe6\xe5\x91\x06\x1f\x17\x05`u\x08\xceu\xbbt\x81\xcd\xd9\x92\xcf'
    int_0 = 1029
    distribution_files_2 = module_0.DistributionFiles(int_0)
    var_0 = distribution_files_2.parse_distribution_file_Slackware(distribution_fact_collector_0, str_0, str_1, bytes_0)

def test_case_3():
    tuple_0 = ()
    distribution_files_0 = module_0.DistributionFiles(tuple_0)
    dict_0 = {tuple_0: tuple_0, distribution_files_0: distribution_files_0, distribution_files_0: tuple_0}
    bytes_0 = b'\x05\xc0\x0b8*G5'
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    distribution_files_1 = module_0.DistributionFiles(distribution_fact_collector_0)
    var_0 = distribution_files_1.parse_distribution_file_OpenWrt(distribution_files_0, dict_0, distribution_files_0, bytes_0)

def test_case_4():
    var_0 = {}
    distribution_files_0 = module_0.DistributionFiles(var_0)
    str_0 = '\ndistribution="OpenWrt"\ndistribution_codename="barrier_breaker"\ndistribution_release="14.07-rc1"\ndistribution_revision="r48537"\n'
    str_1 = 'OpenWrt'
    var_1 = {}
    var_2 = distribution_files_0.parse_distribution_file_OpenWrt(str_1, str_0, str_0, var_1)

def test_case_5():
    str_0 = 'EeKtA~l!Z'
    bytes_0 = b'\xe9\xb7\x93\x89\x0b\x98T\xa9'
    bool_0 = False
    str_1 = "the type of 'task_ds' should be a dict, but is a %s"
    float_0 = 2585.24
    distribution_files_0 = module_0.DistributionFiles(float_0)
    distribution_files_1 = module_0.DistributionFiles(distribution_files_0)
    var_0 = distribution_files_1.parse_distribution_file_Alpine(str_0, bytes_0, bool_0, str_1)

def test_case_6():
    dict_0 = {}
    tuple_0 = ()
    list_0 = []
    str_0 = ''
    distribution_files_0 = module_0.DistributionFiles(str_0)
    var_0 = distribution_files_0.parse_distribution_file_Debian(dict_0, tuple_0, list_0, tuple_0)

def test_case_7():
    dict_0 = None
    str_0 = 'id|+/Y@zELAZ5\rJHjH'
    bytes_0 = b'\xec\xcd\xdc\xdf'
    distribution_files_0 = module_0.DistributionFiles(bytes_0)
    bytes_1 = b'\xa4\xdf\x8a>\x15&\x89\xb6F\x06\xb1\x90'
    distribution_files_1 = module_0.DistributionFiles(bytes_1)
    var_0 = distribution_files_1.parse_distribution_file_Mandriva(dict_0, str_0, dict_0, distribution_files_0)

def test_case_8():
    int_0 = -1334
    distribution_0 = module_0.Distribution(int_0)
    list_0 = [int_0, distribution_0, int_0]
    bytes_0 = b'GnM%\xd5m\xae\xfa,\xb6\x949\xac\xa9pi\t\x0f'
    distribution_files_0 = module_0.DistributionFiles(bytes_0)
    var_0 = distribution_files_0.parse_distribution_file_Coreos(distribution_0, list_0, list_0, list_0)

def test_case_9():
    int_0 = -590
    distribution_files_0 = module_0.DistributionFiles(int_0)
    dict_0 = {int_0: int_0, distribution_files_0: int_0}
    str_0 = 'w](^nZUUR,G`'
    float_0 = -937.3634
    var_0 = distribution_files_0.parse_distribution_file_Flatcar(dict_0, str_0, float_0, distribution_files_0)
    var_1 = distribution_files_0.process_dist_files()

def test_case_10():
    str_0 = '[6\x0bTf0P?qy!ATv?'
    distribution_0 = module_0.Distribution(str_0)
    bool_0 = False
    set_0 = {str_0}
    list_0 = [distribution_0, distribution_0, distribution_0, str_0]
    distribution_files_0 = module_0.DistributionFiles(list_0)
    var_0 = distribution_files_0.parse_distribution_file_ClearLinux(str_0, bool_0, set_0, str_0)

def test_case_11():
    str_0 = ';e~SI\ty(u'
    set_0 = {str_0, str_0, str_0}
    str_1 = '`='
    int_0 = 1607
    distribution_files_0 = module_0.DistributionFiles(int_0)
    var_0 = distribution_files_0.parse_distribution_file_CentOS(set_0, str_0, str_1, str_0)

def test_case_12():
    str_0 = 'flatcar'
    distribution_0 = module_0.Distribution(str_0)
    var_0 = distribution_0.get_distribution_facts()

def test_case_13():
    dict_0 = {}
    distribution_0 = module_0.Distribution(dict_0)
    var_0 = distribution_0.get_distribution_FreeBSD()

def test_case_14():
    str_0 = '[6\x0bTf0P?qy!ATv?'
    distribution_0 = module_0.Distribution(str_0)
    var_0 = distribution_0.get_distribution_SMGL()
    bool_0 = False
    set_0 = {str_0}
    list_0 = [distribution_0, distribution_0, distribution_0, str_0]
    distribution_files_0 = module_0.DistributionFiles(list_0)
    var_1 = distribution_files_0.parse_distribution_file_ClearLinux(str_0, bool_0, set_0, str_0)

def test_case_15():
    str_0 = '[6\x0bTf0P?y!ATv?'
    distribution_0 = module_0.Distribution(str_0)
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    var_0 = distribution_fact_collector_0.collect(distribution_0)

def test_case_16():
    str_0 = '|2pYNv$p[ae<*'
    distribution_0 = module_0.Distribution(str_0)
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    bool_0 = None
    dict_0 = {str_0: bool_0, str_0: str_0}
    bytes_0 = b"9\x82t\x98\xe6\x91\xd2:{\xa6\xbd\xa6Z\xf8'"
    distribution_files_0 = module_0.DistributionFiles(bytes_0)
    var_0 = distribution_files_0.parse_distribution_file_Debian(distribution_fact_collector_0, str_0, bool_0, dict_0)
    var_1 = distribution_fact_collector_0.collect()

def test_case_17():
    set_0 = set()
    str_0 = 'vG@dk5\\S9g*]y\n='
    bytes_0 = b'7\x00)\xe3O\x9a'
    int_0 = -764
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    distribution_files_0 = module_0.DistributionFiles(int_0)
    distribution_fact_collector_1 = module_0.DistributionFactCollector()
    float_0 = 3274.65686
    var_0 = distribution_files_0.parse_distribution_file_Debian(distribution_fact_collector_1, str_0, float_0, distribution_fact_collector_1)
    var_1 = distribution_files_0.parse_distribution_file_NA(set_0, str_0, bytes_0, str_0)

def test_case_18():
    str_0 = '|2pYNv$p[ae<*'
    distribution_0 = module_0.Distribution(str_0)
    distribution_fact_collector_0 = module_0.DistributionFactCollector()
    str_1 = 'h2!/d>]}xCRjU37X>'
    bool_0 = None
    dict_0 = {str_1: bool_0, str_1: str_0}
    bytes_0 = b"9\x82t\x98\xe6\x91\xd2:{\xa6\xbd\xa6Z\xf8'"
    distribution_files_0 = module_0.DistributionFiles(bytes_0)
    var_0 = distribution_files_0.parse_distribution_file_Debian(distribution_fact_collector_0, str_1, bool_0, dict_0)
    int_0 = -3274
    list_0 = [distribution_fact_collector_0, bool_0, distribution_fact_collector_0]
    var_1 = distribution_fact_collector_0.collect(int_0, list_0)