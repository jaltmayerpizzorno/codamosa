# Automatically generated by Pynguin.
import flutils.pathutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '=$Yz;H\x0b!\\.v/'
    bool_0 = True
    module_0.chmod(str_0, bool_0)
    path_0 = module_0.normalize_path(str_0)

def test_case_2():
    str_0 = 'z9N;'
    path_0 = module_0.directory_present(str_0)
    generator_0 = module_0.find_paths(str_0)

def test_case_3():
    str_0 = '/root/tmp/flutils.tests.pathttils'
    module_0.chown(str_0)

def test_case_4():
    str_0 = '~/tmp/flutils.tests.pathutils/direct~ry_present.txt'
    path_0 = module_0.directory_present(str_0)
    path_1 = module_0.normalize_path(str_0)

def test_case_5():
    str_0 = '~/tmp'
    str_1 = module_0.exists_as(str_0)

def test_case_6():
    struct_passwd_0 = module_0.get_os_user()

def test_case_7():
    str_0 = 'Oc\trQ'
    module_0.path_absent(str_0)

def test_case_8():
    str_0 = '/tmp'
    module_0.path_absent(str_0)

def test_case_9():
    str_0 = '/tmp/test_chown'
    str_1 = '-1'
    module_0.chown(str_0, str_1)

def test_case_10():
    bytes_0 = b''
    str_0 = '_P\ns[7o'
    module_0.chmod(str_0)
    str_1 = module_0.exists_as(bytes_0)
    generator_0 = module_0.find_paths(bytes_0)
    struct_group_0 = module_0.get_os_group()
    bool_0 = True
    module_0.chmod(str_1, bool_0)

def test_case_11():
    str_0 = '/tmp'
    module_0.path_absent(str_0)

def test_case_12():
    str_0 = '/dev/stdin'
    str_1 = module_0.exists_as(str_0)
    str_2 = '/dev/stdout'
    str_3 = module_0.exists_as(str_2)
    str_4 = '/dev/stderr'
    str_5 = module_0.exists_as(str_4)
    str_6 = '/dev/null'
    str_7 = module_0.exists_as(str_6)
    str_8 = '/dev/full'
    str_9 = module_0.exists_as(str_8)

def test_case_13():
    str_0 = '~/tmp/**'
    path_0 = module_0.normalize_path(str_0)
    generator_0 = module_0.find_paths(path_0)
    var_0 = list(generator_0)

def test_case_14():
    str_0 = '/etc'
    str_1 = module_0.exists_as(str_0)
    str_2 = '/etc/hosts'
    str_3 = module_0.exists_as(str_2)
    str_4 = '/etc/hosts.t_does_not_exist'
    str_5 = module_0.exists_as(str_4)