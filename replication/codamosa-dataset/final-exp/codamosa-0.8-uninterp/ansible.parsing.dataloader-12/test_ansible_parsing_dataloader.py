# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0

def test_case_0():
    pass

def test_case_1():
    data_loader_0 = module_0.DataLoader()

def test_case_2():
    data_loader_0 = module_0.DataLoader()
    bytes_0 = b'\xa0=[-\xb2B\xb2\xb5$/'
    var_0 = data_loader_0.is_file(bytes_0)

def test_case_3():
    data_loader_0 = module_0.DataLoader()
    str_0 = ''
    var_0 = data_loader_0.find_vars_files(str_0, str_0)

def test_case_4():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.get_basedir()

def test_case_5():
    data_loader_0 = module_0.DataLoader()
    str_0 = 'c*bVY:'
    bytes_0 = b''
    float_0 = None
    var_0 = data_loader_0.path_dwim_relative_stack(str_0, str_0, bytes_0, float_0)

def test_case_6():
    bool_0 = True
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_tmp_file(bool_0)

def test_case_7():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_all_tmp_files()

def test_case_8():
    data_loader_0 = module_0.DataLoader()
    str_0 = 'H4\x0bFem )/`Q#-q'
    var_0 = data_loader_0.find_vars_files(str_0, str_0)

def test_case_9():
    tuple_0 = ()
    float_0 = -530.5309032125476
    bytes_0 = b'\x01\xf9t\x86IvK\x81'
    data_loader_0 = module_0.DataLoader()
    str_0 = '~/'
    dict_0 = {tuple_0: bytes_0, float_0: float_0, tuple_0: float_0, float_0: str_0}
    var_0 = data_loader_0.path_dwim_relative_stack(str_0, dict_0, str_0)

def test_case_10():
    data_loader_0 = module_0.DataLoader()
    str_0 = 'a.yml'
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)
    str_1 = '/Users/x/a'
    var_1 = data_loader_0.path_dwim_relative(str_1, str_1, str_0, str_1)

def test_case_11():
    data_loader_0 = module_0.DataLoader()
    str_0 = 'vars'
    str_1 = 'a.yml'
    var_0 = data_loader_0.path_dwim_relative(str_1, str_0, str_1)
    str_2 = '/Users/x/a'
    var_1 = data_loader_0.path_dwim_relative(str_2, str_0, str_1)
    var_2 = data_loader_0.path_dwim_relative(str_2, str_0, str_2)
    str_3 = '/Users/b.yml'
    var_3 = data_loader_0.path_dwim_relative(str_2, str_0, str_3)