# Automatically generated by Pynguin.
import ansible.module_utils.facts.utils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '/etc/hosts'
    var_0 = module_0.get_file_content(str_0)

def test_case_2():
    str_0 = '/tmp/test.txt'
    var_0 = module_0.get_file_lines(str_0)

def test_case_3():
    bytes_0 = b'\xd5Q\x0e\x14\xcf\x99\xbc\xc6\xc9\xca'
    var_0 = module_0.get_mount_size(bytes_0)

def test_case_4():
    str_0 = '/t/ots'
    var_0 = module_0.get_file_content(str_0)

def test_case_5():
    str_0 = 'w'
    var_0 = module_0.get_file_content(str_0)

def test_case_6():
    str_0 = '/etc/passwd'
    var_0 = module_0.get_file_lines(str_0)
    str_1 = '\n'
    var_1 = module_0.get_file_lines(str_0, str_1)
    str_2 = '\r'
    var_2 = module_0.get_file_lines(str_0, str_2)

def test_case_7():
    str_0 = '/proc/self/cgroup'
    bool_0 = False
    str_1 = ':'
    var_0 = module_0.get_file_lines(str_0, bool_0, str_1)

def test_case_8():
    str_0 = '/bin/false'
    var_0 = module_0.get_file_content(str_0, str_0)