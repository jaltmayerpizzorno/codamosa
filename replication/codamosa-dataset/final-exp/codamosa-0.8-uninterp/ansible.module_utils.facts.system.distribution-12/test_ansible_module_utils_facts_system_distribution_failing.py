# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.distribution as module_0

def test_case_0():
    try:
        str_0 = "9!'p["
        var_0 = module_0.get_uname(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        bytes_0 = b'\xd1\xb6\x0e\t\xe5\xccI\xab\x81\xcf7\xbdh)\xec'
        str_0 = '^'
        dict_0 = {bool_0: bool_0, bytes_0: str_0, str_0: bool_0, bool_0: bool_0}
        bytes_1 = b'\x16\xe5\xa4\x10.\xa3'
        distribution_files_0 = module_0.DistributionFiles(bytes_1)
        var_0 = distribution_files_0.parse_distribution_file_Slackware(bytes_0, str_0, dict_0, str_0)
        distribution_0 = module_0.Distribution(bool_0)
        var_1 = distribution_0.get_distribution_HPUX()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        str_0 = 'wX2P'
        int_0 = 0
        tuple_0 = (dict_0, str_0, int_0)
        str_1 = 'coreos'
        bool_1 = True
        float_0 = 1.5
        distribution_files_0 = module_0.DistributionFiles(float_0)
        var_0 = distribution_files_0.parse_distribution_file_Debian(tuple_0, dict_0, str_1, bool_1)
        distribution_0 = module_0.Distribution(bool_0)
        var_1 = distribution_0.get_distribution_NetBSD()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'eT0x=kr\\'
        bool_0 = True
        float_0 = -36.599
        distribution_0 = module_0.Distribution(float_0)
        int_0 = -1898
        var_0 = distribution_0.get_distribution_facts()
        str_1 = 'AdvancedTCA'
        distribution_1 = module_0.Distribution(str_1)
        distribution_files_0 = module_0.DistributionFiles(distribution_1)
        var_1 = distribution_files_0.parse_distribution_file_NA(str_0, bool_0, distribution_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        distribution_files_0 = module_0.DistributionFiles(list_0)
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        str_0 = 'The python "toml" library is required when using the TOML output format'
        distribution_0 = module_0.Distribution(str_0)
        var_0 = distribution_0.get_distribution_AIX()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "&/)CJ1OK<n@=%'Q'(t=\x0b"
        float_0 = -44.5
        dict_0 = {}
        int_0 = -4156
        bytes_0 = b'\xd7\x03\xe3\xb1B;O\x14Z\xf3;s\xb6\x93\xc5\x08'
        distribution_files_0 = module_0.DistributionFiles(bytes_0)
        distribution_files_1 = module_0.DistributionFiles(distribution_files_0)
        var_0 = distribution_files_1.parse_distribution_file_CentOS(float_0, str_0, dict_0, int_0)
        distribution_0 = module_0.Distribution(str_0)
        var_1 = distribution_0.get_distribution_Darwin()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ',hw:{WZp.Yv`Ete'
        float_0 = 0.0
        distribution_0 = module_0.Distribution(float_0)
        var_0 = distribution_0.get_distribution_facts()
        distribution_1 = module_0.Distribution(str_0)
        var_1 = distribution_1.get_distribution_OpenBSD()
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        str_0 = "'name' is a required field for %s."
        distribution_0 = module_0.Distribution(str_0)
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        str_1 = '5h`r$~!eLpslvc'
        var_0 = distribution_fact_collector_0.collect()
        var_1 = distribution_fact_collector_0.collect(str_1)
        var_2 = distribution_fact_collector_0.collect(distribution_0)
        distribution_fact_collector_1 = module_0.DistributionFactCollector(bool_0)
        bool_1 = False
        distribution_1 = module_0.Distribution(bool_1)
        var_3 = distribution_1.get_distribution_SMGL()
        var_4 = distribution_1.get_distribution_DragonFly()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '*0Z8UQ<'
        tuple_0 = (str_0,)
        str_1 = '`q>-*>y#FFn\r'
        list_0 = [str_0]
        distribution_files_0 = module_0.DistributionFiles(list_0)
        list_1 = [tuple_0, str_1, distribution_files_0]
        distribution_files_1 = module_0.DistributionFiles(list_1)
        distribution_0 = module_0.Distribution(distribution_files_1)
        var_0 = distribution_0.get_distribution_SunOS()
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = -36.599
        distribution_0 = module_0.Distribution(float_0)
        int_0 = -1898
        var_0 = distribution_0.get_distribution_facts()
        str_0 = 'AdvancedTCA'
        distribution_1 = module_0.Distribution(str_0)
        distribution_files_0 = module_0.DistributionFiles(distribution_1)
        bool_0 = False
        list_0 = [bool_0]
        var_1 = module_0.get_uname(int_0, list_0)
    except BaseException:
        pass