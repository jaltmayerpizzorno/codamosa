# Automatically generated by Pynguin.
import ansible.plugins.filter.mathstuff as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xd4\xd7@\x95\x0cy8B'
    list_0 = []
    var_0 = module_0.symmetric_difference(bytes_0, list_0, list_0)

def test_case_2():
    list_0 = None
    bytes_0 = b'n@\x1c\xec'
    var_0 = module_0.min(list_0, bytes_0)

def test_case_3():
    str_0 = '\n    Decorator to retry ssh/scp/sftp in the case of a connection failure\n\n    Will retry if:\n    * an exception is caught\n    * ssh returns 255\n    Will not retry if\n    * sshpass returns 5 (invalid password, to prevent account lockouts)\n    * remaining_tries is < 2\n    * retries limit reached\n    '
    float_0 = -5343.0239
    var_0 = module_0.max(float_0, str_0)

def test_case_4():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_5():
    bytes_0 = b'\xd4\xd7@\x95\x0cy8B'
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.symmetric_difference(bytes_0, list_0, list_0)

def test_case_6():
    filter_module_0 = module_0.FilterModule()
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.union(filter_module_0, list_0, list_1)

def test_case_7():
    bytes_0 = b'\xb5Q\xa4m~O\xff\r\xf8|@\x0bQ\xc9-\xef#\xd7'
    str_0 = 'name cannot be longer than 64 characters on systemd servers, try a shorter name'
    dict_0 = {str_0: str_0, str_0: bytes_0}
    list_0 = [dict_0]
    var_0 = module_0.rekey_on_member(list_0, str_0)

def test_case_8():
    list_0 = None
    list_1 = [list_0, list_0]
    list_2 = [list_1]
    var_0 = module_0.difference(list_0, list_1, list_2)
    var_1 = module_0.unique(list_0, list_2)
    dict_0 = {}
    tuple_0 = ()
    var_2 = module_0.rekey_on_member(dict_0, tuple_0)

def test_case_9():
    float_0 = 38.74375975715523
    list_0 = [float_0, float_0]
    list_1 = [float_0, list_0, list_0, list_0]
    var_0 = module_0.symmetric_difference(float_0, list_0, list_1)