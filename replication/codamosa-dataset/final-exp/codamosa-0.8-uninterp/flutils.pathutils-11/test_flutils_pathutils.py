# Automatically generated by Pynguin.
import flutils.pathutils as module_0
import getpass as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '/dev/sda'
    path_0 = module_0.directory_present(str_0)

def test_case_2():
    str_0 = '/dev/sda'
    path_0 = module_0.directory_present(str_0)

def test_case_3():
    struct_group_0 = module_0.get_os_group()

def test_case_4():
    var_0 = module_1.getuser()
    var_1 = module_1.getuser()
    str_0 = '~/tmp/flutils.tests.osutils.txt'
    module_0.chown(str_0, var_0, var_1)

def test_case_5():
    str_0 = '/Q)=ouin/a'
    module_0.path_absent(str_0)

def test_case_6():
    str_0 = '/Q)=ouin/a'
    int_0 = 80
    module_0.chmod(str_0, int_0)
    path_0 = module_0.directory_present(str_0, int_0)
    module_0.path_absent(str_0)
    str_1 = module_0.exists_as(str_0)

def test_case_7():
    str_0 = '/Q)=ouin/a'
    int_0 = 80
    module_0.chmod(str_0, int_0)
    path_0 = module_0.directory_present(str_0, int_0)
    module_0.path_absent(str_0)

def test_case_8():
    str_0 = ',_+k\x0bw&7tD}'
    module_0.path_absent(str_0)
    struct_passwd_0 = module_0.get_os_user()

def test_case_9():
    str_0 = '/8ev/sda'
    path_0 = module_0.directory_present(str_0)

def test_case_10():
    str_0 = '/tmp/flutils.tests.osutils.txt'
    var_0 = module_1.getuser()
    module_0.chown(str_0)

def test_case_11():
    str_0 = '/tmp'
    str_1 = module_0.exists_as(str_0)
    str_2 = '/etc/hosts'
    str_3 = module_0.exists_as(str_2)
    str_4 = '/dev/sda'
    str_5 = module_0.exists_as(str_4)
    str_6 = '/dev/tty'
    str_7 = module_0.exists_as(str_6)
    str_8 = '/dev/stdin'
    str_9 = module_0.exists_as(str_8)

def test_case_12():
    str_0 = '/etc/hosts'
    str_1 = module_0.exists_as(str_0)
    str_2 = '/dev/sda'
    str_3 = '/dev/tty'
    str_4 = module_0.exists_as(str_2)
    str_5 = module_0.exists_as(str_2)
    str_6 = '/not_exists_path'
    str_7 = module_0.exists_as(str_6)
    module_0.path_absent(str_3)
    path_0 = module_0.directory_present(str_2)

def test_case_13():
    str_0 = '/some/path/that/does/not/exist/*'
    generator_0 = module_0.find_paths(str_0)
    var_0 = list(generator_0)
    var_1 = len(var_0)
    var_2 = module_1.getuser()

def test_case_14():
    str_0 = '/tmp/test_chown.txt'
    str_1 = '/tmp/test_chown.txt'
    module_0.chown(str_1)
    str_2 = '-1'
    module_0.chown(str_1, str_2, str_2)
    module_0.path_absent(str_0)