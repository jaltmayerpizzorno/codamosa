# Automatically generated by Pynguin.
import flutils.pathutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '~/tmp/*'
    generator_0 = module_0.find_paths(str_0)
    struct_passwd_0 = module_0.get_os_user()
    var_0 = set(generator_0)
    int_0 = 1938
    module_0.chmod(str_0, int_0, int_0)

def test_case_2():
    str_0 = '/4U2[=_jDiK@<1F/62'
    module_0.chown(str_0)
    module_0.chmod(str_0)

def test_case_3():
    str_0 = '/4U2[=_jDiK@<1F/62'
    path_0 = module_0.directory_present(str_0)

def test_case_4():
    str_0 = '~/tmp/flutils.tests.osutils.txt'
    module_0.chown(str_0)
    str_1 = '~/tmp/**'
    module_0.chown(str_1)

def test_case_5():
    str_0 = '/4U2[=_jDiK@<1F/62'
    path_0 = module_0.directory_present(str_0)

def test_case_6():
    str_0 = '/mp'
    str_1 = module_0.exists_as(str_0)

def test_case_7():
    struct_group_0 = module_0.get_os_group()

def test_case_8():
    str_0 = "/4E2[/e=_lDiK'YF/62"
    module_0.path_absent(str_0)

def test_case_9():
    str_0 = '~/tmp/*'
    generator_0 = module_0.find_paths(str_0)
    var_0 = set(generator_0)

def test_case_10():
    str_0 = '/dev/null'
    str_1 = module_0.exists_as(str_0)
    str_2 = '/dev/ttys000'
    str_3 = module_0.exists_as(str_2)
    str_4 = '/dev/disk0s1'
    str_5 = module_0.exists_as(str_4)
    str_6 = '/dev/disk2s2'
    str_7 = module_0.exists_as(str_6)
    str_8 = '/dev/fd/0'
    str_9 = module_0.exists_as(str_8)
    str_10 = '/dev/fd/1'
    str_11 = module_0.exists_as(str_10)