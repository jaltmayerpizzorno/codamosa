# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.distribution as module_0

def test_case_0():
    try:
        distribution_files_0 = module_0.DistributionFiles()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1887
        distribution_0 = module_0.Distribution(int_0)
        var_0 = distribution_0.get_distribution_FreeBSD()
        int_1 = -574
        var_1 = module_0.get_uname(int_1)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = None
        float_0 = 156.0
        bytes_0 = b'\xdd\x12\x13\xda\xe3l\xb4\xda.\x98fq\x8eF\xe5~\xd8\x8d'
        distribution_fact_collector_0 = module_0.DistributionFactCollector(bytes_0)
        str_0 = ''
        bool_0 = False
        distribution_files_0 = module_0.DistributionFiles(bool_0)
        var_0 = distribution_files_0.parse_distribution_file_OpenWrt(set_0, float_0, distribution_fact_collector_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Package already installed: {0}'
        set_0 = {str_0}
        distribution_files_0 = module_0.DistributionFiles(set_0)
        distribution_0 = module_0.Distribution(distribution_files_0)
        int_0 = 40
        float_0 = -774.6528
        int_1 = -568
        distribution_fact_collector_0 = module_0.DistributionFactCollector(int_1)
        var_0 = distribution_fact_collector_0.collect(float_0)
        distribution_fact_collector_1 = module_0.DistributionFactCollector()
        var_1 = distribution_0.get_distribution_facts()
        list_0 = [distribution_fact_collector_1, distribution_0, int_0, set_0]
        bytes_0 = b'\xdc\n\x84\xfc'
        var_2 = distribution_files_0.parse_distribution_file_Alpine(int_0, distribution_fact_collector_1, list_0, bytes_0)
        bytes_1 = b'\xd2[\x9e\xd4\x05\xa2\xb0\x9f\xd1\x7f\x0b\xb9\x19K\xee#V'
        bool_0 = False
        dict_0 = None
        var_3 = distribution_files_0.parse_distribution_file_Amazon(bytes_1, bool_0, dict_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'NA'
        distribution_fact_collector_0 = module_0.DistributionFactCollector(str_0)
        int_0 = 415
        str_1 = 'flatcar'
        bytes_0 = b'$%b\x12}H\xdeR\x8e\xbd\x06+\t|\x8f\x98\xc1\xf6'
        distribution_files_0 = module_0.DistributionFiles(bytes_0)
        var_0 = distribution_files_0.parse_distribution_file_Mandriva(distribution_fact_collector_0, str_0, int_0, str_1)
        distribution_files_1 = module_0.DistributionFiles()
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        distribution_0 = module_0.Distribution(dict_0)
        var_0 = distribution_0.get_distribution_NetBSD()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\xa8U0\x8b,\x05\xf5g\xa2Q\xc0\x9f\xa7i\xe5\x02\x81+'
        distribution_0 = module_0.Distribution(bytes_0)
        var_0 = distribution_0.get_distribution_HPUX()
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -1766
        distribution_0 = module_0.Distribution(int_0)
        var_0 = distribution_0.get_distribution_Darwin()
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = 3465.46656
        distribution_files_0 = module_0.DistributionFiles(float_0)
        distribution_0 = module_0.Distribution(distribution_files_0)
        var_0 = distribution_0.get_distribution_OpenBSD()
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = -532.777569
        distribution_files_0 = module_0.DistributionFiles(float_0)
        distribution_0 = module_0.Distribution(distribution_files_0)
        var_0 = distribution_0.get_distribution_DragonFly()
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = 2.0
        distribution_0 = module_0.Distribution(float_0)
        bytes_0 = b'\x147'
        distribution_files_0 = module_0.DistributionFiles(bytes_0)
        set_0 = set()
        bool_0 = False
        tuple_0 = (distribution_0, distribution_files_0, set_0, bool_0)
        distribution_1 = module_0.Distribution(tuple_0)
        int_0 = -837
        distribution_fact_collector_0 = module_0.DistributionFactCollector(set_0, int_0)
        str_0 = 'r,#.y+=1+&{\x0cr[>6R-?'
        bool_1 = False
        var_0 = distribution_1.get_distribution_SMGL()
        distribution_2 = module_0.Distribution(bool_1)
        var_1 = distribution_files_0.process_dist_files()
        distribution_files_1 = module_0.DistributionFiles(distribution_2)
        var_2 = distribution_files_1.parse_distribution_file_NA(distribution_1, distribution_fact_collector_0, str_0, distribution_files_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'F?'
        distribution_fact_collector_0 = module_0.DistributionFactCollector(str_0)
        set_0 = {str_0}
        distribution_files_0 = module_0.DistributionFiles(set_0)
        var_0 = distribution_fact_collector_0.collect(distribution_files_0)
        tuple_0 = (distribution_fact_collector_0,)
        str_1 = '}KrNlfL('
        str_2 = 'Y5vxkfS/'
        var_1 = distribution_files_0.parse_distribution_file_Flatcar(tuple_0, str_1, str_2, distribution_fact_collector_0)
        distribution_0 = module_0.Distribution(tuple_0)
        var_2 = distribution_0.get_distribution_SunOS()
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = False
        distribution_files_0 = module_0.DistributionFiles(bool_0)
        distribution_files_1 = module_0.DistributionFiles(distribution_files_0)
        var_0 = distribution_files_1.process_dist_files()
        str_0 = 'W8FLLB&qf6'
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        bytes_0 = b'\x03\xaa\xef\x18\xc8\xf7$\x81\x88.(D\x84'
        distribution_files_2 = module_0.DistributionFiles(bytes_0)
        dict_0 = {str_0: bytes_0}
        var_1 = distribution_files_2.parse_distribution_file_CentOS(bytes_0, dict_0, str_0, distribution_files_2)
        distribution_0 = module_0.Distribution(distribution_files_2)
        var_2 = distribution_0.get_distribution_SMGL()
        distribution_files_3 = module_0.DistributionFiles(distribution_fact_collector_0)
        distribution_1 = module_0.Distribution(distribution_files_3)
        var_3 = distribution_1.get_distribution_SMGL()
        dict_1 = {}
        float_0 = 2414.4
        var_4 = module_0.get_uname(dict_1, float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 4576
        str_0 = 'NA'
        str_1 = 'advisory_type__eq'
        dict_0 = {int_0: int_0, int_0: int_0, str_0: str_0, str_1: str_0}
        distribution_0 = module_0.Distribution(dict_0)
        distribution_fact_collector_0 = module_0.DistributionFactCollector(distribution_0, dict_0)
        float_0 = -1270.0
        set_0 = {int_0}
        distribution_files_0 = module_0.DistributionFiles(set_0)
        var_0 = distribution_files_0.parse_distribution_file_ClearLinux(str_0, distribution_fact_collector_0, distribution_0, float_0)
        distribution_fact_collector_1 = module_0.DistributionFactCollector(int_0)
        tuple_0 = ()
        distribution_1 = module_0.Distribution(tuple_0)
        var_1 = distribution_fact_collector_1.collect(int_0, distribution_1)
        float_1 = -2311.806
        var_2 = distribution_fact_collector_1.collect(float_1)
        bytes_0 = b'\xde\xa7\x8f'
        str_2 = '6b24!%E^W;yY2'
        distribution_files_1 = module_0.DistributionFiles(str_2)
        float_2 = 1423.094
        distribution_files_2 = module_0.DistributionFiles(float_2)
        float_3 = 512.0
        distribution_2 = module_0.Distribution(float_3)
        str_3 = '1\n:2SJ)'
        var_3 = distribution_fact_collector_1.collect(str_3)
        var_4 = distribution_files_1.parse_distribution_file_Amazon(str_3, distribution_files_2, str_3, bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        dict_0 = None
        str_0 = '+Uw\t;I%%Dig7F2g6$Gk'
        bool_0 = True
        tuple_0 = (dict_0, str_0, bool_0)
        set_0 = {tuple_0}
        list_0 = [set_0, tuple_0]
        distribution_0 = module_0.Distribution(list_0)
        var_0 = distribution_0.get_distribution_AIX()
    except BaseException:
        pass