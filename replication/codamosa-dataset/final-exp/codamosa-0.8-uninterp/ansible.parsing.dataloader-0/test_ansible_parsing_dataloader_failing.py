# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0

def test_case_0():
    try:
        dict_0 = {}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load_from_file(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load_from_file(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 715.0
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_exists(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = None
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.list_directory(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '{0} [core {1}]'
        var_0 = data_loader_0.list_directory(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = ()
        data_loader_0 = module_0.DataLoader()
        bytes_0 = b'G\xf3\x07\xb5\x97\xf7%\x18W\x8f\x80g\x12'
        list_0 = [tuple_0, data_loader_0, bytes_0, data_loader_0]
        var_0 = data_loader_0.set_basedir(list_0)
        var_1 = data_loader_0.is_executable(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'IQ~JS'
        int_0 = 1371
        list_0 = []
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, int_0, list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'DqT;,y[vZO'
        int_0 = None
        bool_0 = True
        var_0 = data_loader_0.path_dwim_relative_stack(int_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = ()
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\xbaIU\xb4$\n\xa3a\xbb\xed'
        list_0 = []
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load_from_file(bytes_0, list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '/etc/passwd'
        data_loader_0 = module_0.DataLoader()
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_1.get_real_file(str_0)
        bytes_0 = b'\x07\x8d\xe3'
        var_1 = data_loader_0.set_basedir(str_0)
        var_2 = data_loader_1.is_directory(bytes_0)
        var_3 = data_loader_0.load_from_file(str_0, data_loader_0)
        bytes_1 = None
        tuple_0 = (bytes_1, bytes_1)
        var_4 = data_loader_1.path_dwim_relative_stack(tuple_0, str_0, str_0)
        dict_0 = None
        var_5 = data_loader_1.set_basedir(dict_0)
        str_1 = 'r'
        var_6 = data_loader_0.load_from_file(str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = -1195.55
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '_G@\r'
        complex_0 = None
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, complex_0, complex_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'h&/[SzL9\tnH`SKAQH7b'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '/etc/passwd'
        float_0 = 2293.7765008696238
        str_1 = "G&\x0b{*>sCr\\1}*'F@'C(v"
        tuple_0 = ()
        tuple_1 = (float_0, str_1, tuple_0)
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_tmp_file(float_0)
        var_1 = data_loader_0.get_real_file(str_0)
        var_2 = data_loader_0.set_basedir(str_0)
        var_3 = data_loader_0.load_from_file(str_0, data_loader_0)
        var_4 = data_loader_0.cleanup_all_tmp_files()
        var_5 = data_loader_0.path_dwim_relative_stack(tuple_1, str_0, str_0)
        str_2 = '~XAJn&]E#'
        bool_0 = False
        var_6 = data_loader_0.path_dwim_relative(str_2, str_2, bool_0)
        str_3 = '>ogku'
        var_7 = data_loader_0.load_from_file(str_3)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'files'
        str_1 = 'var.yml'
        data_loader_0 = module_0.DataLoader()
        str_2 = [str_0]
        bool_0 = True
        var_0 = data_loader_0.path_dwim_relative_stack(str_2, str_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '/etc/passwd'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(str_0)
        bytes_0 = None
        tuple_0 = (bytes_0, bytes_0)
        str_1 = '+RSS%+j'
        var_1 = data_loader_0.path_dwim_relative_stack(tuple_0, str_1, str_0)
        var_2 = data_loader_0.get_real_file(data_loader_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = './roles/role1/tasks/main.yml'
        str_1 = 'files'
        str_2 = 'var.yml'
        data_loader_0 = module_0.DataLoader()
        str_3 = [str_0]
        bool_0 = True
        var_0 = data_loader_0.path_dwim_relative_stack(str_3, str_1, str_2, bool_0)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b''
        list_0 = []
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.load_from_file(bytes_0, list_0)
    except BaseException:
        pass

def test_case_19():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'DqT;,y[vZO'
        var_0 = data_loader_0.cleanup_all_tmp_files()
        tuple_0 = ()
        var_1 = data_loader_0.cleanup_tmp_file(tuple_0)
        var_2 = data_loader_0.cleanup_all_tmp_files()
        var_3 = data_loader_0.path_dwim_relative(str_0, str_0, data_loader_0)
        list_0 = []
        bytes_0 = b'~\xbf\xd9'
        var_4 = data_loader_0.path_dwim_relative(tuple_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_20():
    try:
        float_0 = 2293.7765008696238
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_tmp_file(float_0)
        var_1 = data_loader_0.cleanup_all_tmp_files()
        str_0 = '~F<H'
        dict_0 = {var_1: str_0}
        var_2 = data_loader_0.path_dwim_relative(str_0, dict_0, str_0)
        bytes_0 = None
        tuple_0 = (bytes_0, bytes_0)
        str_1 = ',kh*z}:2krE\x0b_5'
        var_3 = data_loader_0.path_dwim_relative_stack(tuple_0, str_1, str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = ''
        var_0 = data_loader_0.find_vars_files(str_0, str_0)
        data_loader_1 = module_0.DataLoader()
        str_1 = '/etc/passwd'
        float_0 = 2296.0908201700686
        var_1 = data_loader_0.cleanup_tmp_file(float_0)
        var_2 = data_loader_0.get_real_file(str_1)
        bytes_0 = b'\x13'
        var_3 = data_loader_0.is_directory(bytes_0)
        var_4 = data_loader_1.get_basedir()
        var_5 = data_loader_0.load_from_file(str_1, var_1, bytes_0)
        str_2 = 'xir/luBR'
        str_3 = "bDYE|'+"
        bool_0 = False
        var_6 = data_loader_1.path_dwim_relative(str_2, str_3, bool_0)
        var_7 = data_loader_1.cleanup_all_tmp_files()
        str_4 = 'D'
        var_8 = data_loader_0.cleanup_all_tmp_files()
        var_9 = data_loader_0.path_dwim_relative_stack(str_2, bytes_0, str_4)
    except BaseException:
        pass