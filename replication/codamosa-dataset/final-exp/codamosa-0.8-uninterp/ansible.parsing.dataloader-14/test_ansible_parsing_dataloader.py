# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0
import ansible.parsing.vault as module_1

def test_case_0():
    pass

def test_case_1():
    data_loader_0 = module_0.DataLoader()

def test_case_2():
    bytes_0 = b'\xf9\x14(3,\xcc\xf0a5\xdf'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.is_file(bytes_0)

def test_case_3():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.get_basedir()

def test_case_4():
    str_0 = 'ooa=r'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)

def test_case_5():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_tmp_file(data_loader_0)

def test_case_6():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_all_tmp_files()

def test_case_7():
    str_0 = "role '%s' vars"
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.find_vars_files(str_0, str_0)

def test_case_8():
    str_0 = '/home/localadmin/backup/my.yml'
    str_1 = 'my.yml'
    bool_0 = True
    data_loader_0 = module_0.DataLoader()
    str_2 = 'other.yml'
    var_0 = data_loader_0.path_dwim_relative(str_0, str_2, str_2, bool_0)
    data_loader_1 = module_0.DataLoader()
    var_1 = data_loader_1.path_dwim_relative(str_0, str_1, str_2, bool_0)

def test_case_9():
    bool_0 = True
    str_0 = 'other.yml'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0, bool_0)

def test_case_10():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.get_basedir()
    str_0 = ''
    var_1 = data_loader_0.find_vars_files(str_0, str_0)
    str_1 = '$|0{@dvX8W1LZ'
    tuple_0 = (data_loader_0, str_1)
    int_0 = -1793
    var_2 = data_loader_0.set_vault_secrets(int_0)
    var_3 = data_loader_0.is_file(tuple_0)
    var_4 = data_loader_0.path_dwim(str_1)
    data_loader_1 = module_0.DataLoader()

def test_case_11():
    data_loader_0 = module_0.DataLoader()
    int_0 = None
    tuple_0 = ()
    var_0 = data_loader_0.cleanup_tmp_file(tuple_0)
    str_0 = ''
    var_1 = data_loader_0.find_vars_files(str_0, str_0)
    var_2 = data_loader_0.cleanup_all_tmp_files()
    float_0 = 2019.5596
    var_3 = data_loader_0.set_basedir(tuple_0)
    dict_0 = {int_0: str_0, int_0: tuple_0}
    var_4 = data_loader_0.get_basedir()
    var_5 = data_loader_0.path_dwim(dict_0)
    str_1 = 'my.yml'
    tuple_1 = (data_loader_0, str_0)
    int_1 = -1793
    var_6 = data_loader_0.set_vault_secrets(int_1)
    var_7 = data_loader_0.is_file(tuple_1)
    str_2 = ';/'
    var_8 = data_loader_0.cleanup_tmp_file(str_2)
    var_9 = data_loader_0.set_basedir(data_loader_0)
    var_10 = data_loader_0.path_dwim(str_0)
    bool_0 = False
    var_11 = data_loader_0.path_dwim_relative(str_0, str_0, str_1, bool_0)
    data_loader_1 = module_0.DataLoader()
    bytes_0 = b'\xe9+b}\xc2\xdc\xb52k\xf3\xe5\xf5XF\xda\xc8\x86'
    str_3 = 'gNN1IRJ7'
    float_1 = 1057.0
    vault_lib_0 = module_1.VaultLib()
    str_4 = '~o'
    data_loader_2 = module_0.DataLoader()
    var_12 = data_loader_2.path_dwim_relative(float_1, vault_lib_0, str_4)
    data_loader_3 = module_0.DataLoader()
    list_0 = [data_loader_0, bytes_0]
    var_13 = data_loader_1.path_dwim_relative_stack(str_3, float_0, str_0, list_0)
    str_5 = '>4|B]K,CLp\x0b6)l!:4?'
    var_14 = data_loader_0.set_vault_secrets(str_5)
    var_15 = data_loader_0.cleanup_all_tmp_files()

def test_case_12():
    data_loader_0 = module_0.DataLoader()
    int_0 = None
    tuple_0 = ()
    var_0 = data_loader_0.get_basedir()
    var_1 = data_loader_0.cleanup_tmp_file(tuple_0)
    str_0 = ''
    var_2 = data_loader_0.find_vars_files(str_0, str_0)
    var_3 = data_loader_0.cleanup_all_tmp_files()
    float_0 = 2019.5596
    dict_0 = {int_0: str_0, int_0: tuple_0}
    var_4 = data_loader_0.path_dwim(dict_0)
    str_1 = 'my.yml'
    tuple_1 = (data_loader_0, str_0)
    var_5 = data_loader_0.is_file(tuple_1)
    str_2 = ';/'
    var_6 = data_loader_0.cleanup_tmp_file(str_2)
    var_7 = data_loader_0.set_basedir(data_loader_0)
    bool_0 = False
    var_8 = data_loader_0.path_dwim_relative(str_0, str_0, str_1, bool_0)
    var_9 = data_loader_0.get_basedir()
    set_0 = {var_8}
    data_loader_1 = module_0.DataLoader()
    bytes_0 = b'\xe9+b}\xc2\xdc\xb52k\xf3\xe5\xf5XF\xda\xc8\x86'
    str_3 = 'gNN1IRJ7'
    data_loader_2 = module_0.DataLoader()
    list_0 = [data_loader_0, bytes_0]
    var_10 = data_loader_1.path_dwim_relative_stack(str_3, float_0, str_0, var_3)
    data_loader_3 = module_0.DataLoader()
    var_11 = data_loader_0.set_vault_secrets(str_0)
    str_4 = '/'
    var_12 = data_loader_0.path_dwim_relative_stack(list_0, set_0, str_4)

def test_case_13():
    data_loader_0 = module_0.DataLoader()
    int_0 = None
    tuple_0 = ()
    data_loader_1 = module_0.DataLoader()
    var_0 = data_loader_0.get_basedir()
    var_1 = data_loader_0.cleanup_tmp_file(tuple_0)
    str_0 = '/'
    var_2 = data_loader_0.find_vars_files(str_0, str_0)
    var_3 = data_loader_0.cleanup_all_tmp_files()
    var_4 = data_loader_0.get_basedir()
    float_0 = -382.66
    var_5 = data_loader_0.set_basedir(tuple_0)
    dict_0 = {int_0: str_0, int_0: tuple_0}
    var_6 = data_loader_0.path_dwim(dict_0)
    str_1 = 'my.yml'
    tuple_1 = (data_loader_0, str_0)
    int_1 = -1793
    var_7 = data_loader_0.set_vault_secrets(int_1)
    var_8 = data_loader_0.is_file(tuple_1)
    var_9 = data_loader_0.set_basedir(data_loader_0)
    var_10 = data_loader_0.path_dwim(str_0)
    var_11 = data_loader_1.path_dwim_relative(str_0, str_0, str_1, var_7)
    set_0 = {var_11}
    bytes_0 = b'28J\xa1\xabtj\xa9p\x8c\xda\x97\xe5\x13'
    str_2 = 'gNN1IRJ7'
    data_loader_2 = module_0.DataLoader()
    list_0 = [data_loader_0, bytes_0]
    var_12 = data_loader_2.path_dwim_relative_stack(str_2, float_0, str_0, list_0)
    vault_lib_0 = module_1.VaultLib()
    var_13 = data_loader_2.cleanup_tmp_file(vault_lib_0)
    bytes_1 = b'@\x80'
    str_3 = '@E1'
    var_14 = data_loader_0.path_dwim_relative_stack(set_0, bytes_1, str_3)