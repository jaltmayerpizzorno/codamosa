# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0
import ansible.parsing.vault as module_1

def test_case_0():
    pass

def test_case_1():
    data_loader_0 = module_0.DataLoader()

def test_case_2():
    data_loader_0 = module_0.DataLoader()
    str_0 = ''
    var_0 = data_loader_0.find_vars_files(str_0, str_0)

def test_case_3():
    bytes_0 = b''
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.is_executable(bytes_0)

def test_case_4():
    dict_0 = {}
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.set_basedir(dict_0)

def test_case_5():
    str_0 = '/path/to/tasks'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)

def test_case_6():
    str_0 = 'zIc^dIg2Y+\x0b+`w?d6'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)

def test_case_7():
    str_0 = 'V0\nxk~[vt)KMp^_V'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_tmp_file(str_0)

def test_case_8():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_all_tmp_files()

def test_case_9():
    tuple_0 = ()
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.is_file(tuple_0)

def test_case_10():
    data_loader_0 = module_0.DataLoader()

def test_case_11():
    str_0 = '/path/to/tasks'
    str_1 = 'role_dirname'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_dwim_relative(str_0, str_1, str_1)

def test_case_12():
    data_loader_0 = module_0.DataLoader()
    str_0 = "'&X9\x0c={ll"
    var_0 = data_loader_0.find_vars_files(str_0, str_0)

def test_case_13():
    str_0 = 'Hand Held'
    str_1 = "pa^z7_\x0cT>TL']"
    int_0 = 3518
    bytes_0 = b'\x14A6\x8c\xf0\x84\xe1\t\x19\x81hX'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_dwim_relative(str_0, str_1, int_0, bytes_0)

def test_case_14():
    data_loader_0 = module_0.DataLoader()
    data_loader_1 = module_0.DataLoader()
    str_0 = ''
    float_0 = -1191.3385
    var_0 = data_loader_1.cleanup_tmp_file(float_0)
    int_0 = -4589
    vault_lib_0 = module_1.VaultLib()
    bool_0 = False
    set_0 = {data_loader_1, bool_0, vault_lib_0, var_0}
    var_1 = data_loader_0.path_dwim_relative(str_0, str_0, set_0, int_0)

def test_case_15():
    str_0 = ''
    str_1 = '~Lr&\x0b1'
    list_0 = [str_1, str_0]
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.find_vars_files(str_0, str_1, list_0)

def test_case_16():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_all_tmp_files()
    data_loader_1 = module_0.DataLoader()
    str_0 = '/'
    var_1 = data_loader_1.find_vars_files(str_0, str_0)
    float_0 = -1191.3385
    var_2 = data_loader_1.cleanup_tmp_file(float_0)
    str_1 = "wkS\r:*y~ER'MW"
    vault_lib_0 = module_1.VaultLib()
    list_0 = [var_0, float_0, str_1]
    vault_lib_1 = module_1.VaultLib(str_1)
    var_3 = data_loader_1.load_from_file(list_0, vault_lib_1)
    bool_0 = False
    set_0 = {data_loader_1, bool_0, var_0}
    str_2 = 'X3t >1\x0bP'
    var_4 = data_loader_0.path_dwim_relative(set_0, vault_lib_1, str_2)

def test_case_17():
    str_0 = ''
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)