# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0

def test_case_0():
    try:
        dict_0 = None
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'cb,!XHKO9J#_oRh|'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load_from_file(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/usr/bin/'
        var_0 = data_loader_0.get_real_file(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_directory(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'(\x90\x9dJO\x99kq\xc7[\x82\xf8\xa9\xfa\x80\x01\xe7\xbe'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.list_directory(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '"'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_tmp_file(str_0)
        data_loader_1 = module_0.DataLoader()
        bytes_0 = b'\x02V\xc3\xafL\xbc\xf8'
        var_1 = data_loader_1.is_executable(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'Qi$Y~@/BL,F4:H8,Cakr'
        dict_0 = {}
        var_0 = data_loader_0.path_dwim_relative_stack(dict_0, data_loader_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim_relative(bool_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '>2-b\n~Tal'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(str_0, data_loader_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = ']E{.$OBG\x0bf'
        float_0 = 912.174
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim_relative(str_0, str_0, float_0)
        dict_0 = {var_0: var_0, var_0: str_0}
        var_1 = data_loader_0.get_real_file(dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'\x85\x9a\x83\x10F\xf2'
        bool_0 = True
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.find_vars_files(bytes_0, bytes_0, bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/a/b/c/d/e'
        str_1 = 'to/file.yml'
        bool_0 = False
        var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_1, bool_0)
        int_0 = None
        var_1 = data_loader_0.get_real_file(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_all_tmp_files()
        bytes_0 = None
        bool_0 = False
        list_0 = None
        var_1 = data_loader_0.path_dwim_relative_stack(bytes_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = ''
        var_0 = data_loader_0.load_from_file(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = None
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.set_basedir(list_0)
        data_loader_1 = module_0.DataLoader()
        var_1 = data_loader_1.cleanup_all_tmp_files()
        data_loader_2 = module_0.DataLoader()
        bytes_0 = b'\xf2\xc5k5\x94\xd2#\xe9\xafv'
        dict_0 = None
        var_2 = data_loader_2.cleanup_tmp_file(dict_0)
        str_0 = '"YK'
        str_1 = '~>O'
        int_0 = -318
        var_3 = data_loader_2.path_dwim_relative_stack(bytes_0, str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = -537.0
        list_0 = [float_0, float_0]
        complex_0 = None
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load_from_file(list_0, complex_0)
    except BaseException:
        pass

def test_case_16():
    try:
        data_loader_0 = module_0.DataLoader()
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_1.get_basedir()
        data_loader_2 = None
        var_1 = data_loader_0.cleanup_tmp_file(data_loader_2)
        str_0 = '~/.ansible'
        var_2 = data_loader_1.is_executable(str_0)
        data_loader_3 = module_0.DataLoader()
        int_0 = 3143
        var_3 = data_loader_0.set_basedir(int_0)
    except BaseException:
        pass

def test_case_17():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/etc/ansible/roles/foo'
        str_1 = 'Z0w)r]F5'
        str_2 = [str_0, str_1]
        str_3 = 'foo.yml'
        bool_0 = True
        var_0 = data_loader_0.path_dwim_relative_stack(str_2, str_0, str_3, bool_0)
    except BaseException:
        pass

def test_case_18():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/Users/user/Projects/ansible-project/playbooks/roles/venv'
        str_1 = '/Users/user/Projects/ansible-project/playbooks/roles/venv/tasks'
        str_2 = [str_0, str_1]
        var_0 = data_loader_0.cleanup_all_tmp_files()
        str_3 = " @I24n'yFd}\t"
        var_1 = data_loader_0.is_file(str_3)
        str_4 = 'vars'
        float_0 = -1071.284755
        var_2 = data_loader_0.set_basedir(float_0)
        str_5 = '/Users/user/Projects/ansible-project/playbooks/roles/venv/vars/main.yaml'
        var_3 = data_loader_0.path_dwim_relative_stack(str_2, str_4, str_5)
    except BaseException:
        pass

def test_case_19():
    try:
        data_loader_0 = module_0.DataLoader()
        bytes_0 = b'\xf2\xc5k5\x94\xd2#\xe9\xafv'
        dict_0 = None
        var_0 = data_loader_0.cleanup_tmp_file(dict_0)
        str_0 = '"YK'
        str_1 = '~>O'
        int_0 = -303
        var_1 = data_loader_0.path_dwim_relative_stack(bytes_0, str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_20():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/Users/user/Projects/ansible-project/playbooks/roles/venv/tasks'
        str_1 = [str_0, str_0]
        str_2 = 'vars'
        var_0 = data_loader_0.path_dwim_relative_stack(str_1, str_2, str_2)
    except BaseException:
        pass

def test_case_21():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/a/b/c/d/e'
        str_1 = 'tofieyml'
        bool_0 = True
        var_0 = data_loader_0.path_dwim_relative(str_0, str_1, str_1, bool_0)
        list_0 = [str_0, str_0]
        dict_0 = {}
        var_1 = data_loader_0.path_dwim_relative_stack(list_0, dict_0, bool_0)
    except BaseException:
        pass

def test_case_22():
    try:
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_all_tmp_files()
        bytes_0 = b'\xe8\x10\xa0\n!\xdb\x9b\xba'
        str_0 = '<1S'
        list_0 = [str_0, bytes_0, str_0]
        bytes_1 = b"\xea\xfd^\x90'\r\xb6\xa9\xeb\xef,\xe4\xabY"
        var_1 = data_loader_0.find_vars_files(bytes_0, bytes_0, list_0, bytes_1)
    except BaseException:
        pass