# Automatically generated by Pynguin.
import flutils.pathutils as module_0
import pathlib as module_1

def test_case_0():
    try:
        str_0 = '~/tmp/test_path'
        path_0 = module_0.directory_present(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b''
        module_0.chmod(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        struct_group_0 = module_0.get_os_group()
        str_0 = '/.'
        path_0 = module_0.directory_present(str_0)
        struct_group_1 = module_0.get_os_group(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '~/tmp/test_path'
        bool_0 = True
        path_0 = module_0.directory_present(str_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        posix_path_0 = module_1.PosixPath()
        module_0.path_absent(posix_path_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '/.'
        module_0.path_absent(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        struct_group_0 = module_0.get_os_group()
        str_0 = '/+'
        bool_0 = False
        struct_group_1 = module_0.get_os_group()
        module_0.chown(str_0, bool_0)
        path_0 = module_0.directory_present(str_0)
        path_1 = module_0.normalize_path(str_0)
        module_0.path_absent(str_0)
        struct_group_2 = module_0.get_os_group()
        str_1 = module_0.exists_as(str_0)
        path_2 = module_0.normalize_path(str_0)
        module_0.path_absent(str_0)
        module_0.chmod(str_0)
        bool_1 = True
        module_0.chown(str_0, str_0, bool_1)
    except BaseException:
        pass

def test_case_7():
    try:
        struct_group_0 = module_0.get_os_group()
        int_0 = -2561
        struct_group_1 = module_0.get_os_group(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'D\x8e\xc7M\xb2\xde\xca\xc8\xba\xf7\xf0\xff'
        generator_0 = module_0.find_paths(bytes_0)
        struct_passwd_0 = module_0.get_os_user(generator_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '/N.'
        path_0 = module_0.normalize_path(str_0)
        module_0.path_absent(str_0)
        str_1 = '?A'
        module_0.chown(str_0, str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -1399
        struct_passwd_0 = module_0.get_os_user(int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '/.'
        path_0 = module_0.directory_present(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '~/tmp/test_path'
        path_0 = module_0.directory_present(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '/N.'
        path_0 = module_0.directory_present(str_0)
        path_1 = module_0.normalize_path(str_0)
        module_0.path_absent(str_0)
        struct_passwd_0 = module_0.get_os_user()
        str_1 = 'drP'
        module_0.chown(str_0, str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = []
        posix_path_0 = module_1.PosixPath(*list_0)
        str_0 = "j/otfTwF\x0c_l'Jj94"
        str_1 = 'l_e<'
        str_2 = "'}#\x0b"
        dict_0 = {str_0: str_0, str_1: list_0, str_2: list_0}
        struct_group_0 = module_0.get_os_group(dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'text'
        str_1 = '~/tmp'
        path_0 = module_0.directory_present(str_1, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '~/tmp/*'
        module_0.chmod(str_0)
        path_0 = module_0.directory_present(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '/etc/'
        str_1 = module_0.exists_as(str_0)
        str_2 = '/etc/hosts'
        str_3 = module_0.exists_as(str_2)
        str_4 = '/etc/group'
        str_5 = module_0.exists_as(str_4)
        str_6 = module_0.exists_as(str_1)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '/etc/'
        module_0.path_absent(str_0)
    except BaseException:
        pass