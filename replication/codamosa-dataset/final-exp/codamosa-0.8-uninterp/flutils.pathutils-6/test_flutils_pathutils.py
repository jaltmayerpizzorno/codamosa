# Automatically generated by Pynguin.
import flutils.pathutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '~/tmp/*'
    struct_group_0 = module_0.get_os_group()
    module_0.chmod(str_0)

def test_case_2():
    str_0 = '/tmp/tmp_directory_present_test'
    path_0 = module_0.directory_present(str_0)

def test_case_3():
    str_0 = '/home/test_user/tmp/file_one'
    module_0.chmod(str_0)

def test_case_4():
    str_0 = '/tmp/tmp_directory_present_test'
    path_0 = module_0.directory_present(str_0)

def test_case_5():
    struct_group_0 = module_0.get_os_group()

def test_case_6():
    str_0 = '/tmp/tmp_directory_present_test'
    module_0.path_absent(str_0)

def test_case_7():
    str_0 = '/pynNuin'
    module_0.path_absent(str_0)
    path_0 = module_0.directory_present(str_0)
    struct_passwd_0 = module_0.get_os_user()
    module_0.chmod(str_0)
    path_1 = module_0.directory_present(str_0)
    struct_passwd_1 = module_0.get_os_user()
    str_1 = '/home/test_user/tmp/file_one'
    bool_0 = False
    module_0.chmod(str_1, bool_0)

def test_case_8():
    str_0 = '~/tmp/flutils.tests.osutils.txt'
    module_0.chown(str_0)

def test_case_9():
    str_0 = '~/tmp/*'
    generator_0 = module_0.find_paths(str_0)
    var_0 = list(generator_0)

def test_case_10():
    str_0 = '/etc/'
    str_1 = module_0.exists_as(str_0)
    str_2 = '/etc'
    str_3 = module_0.exists_as(str_2)
    str_4 = '/etc/hosts'
    str_5 = module_0.exists_as(str_4)
    str_6 = '/dev/null'
    str_7 = module_0.exists_as(str_6)
    str_8 = '/dev/nulla'
    str_9 = module_0.exists_as(str_8)
    str_10 = '/dev/random'
    str_11 = module_0.exists_as(str_10)
    module_0.chown(str_2)