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
        str_0 = "j'y6CgN~!TX"
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        data_loader_0 = module_0.DataLoader()
        data_loader_1 = module_0.DataLoader()
        str_0 = "8=,~z}'[%.\x0bY`k"
        var_0 = data_loader_1.find_vars_files(str_0, str_0)
        data_loader_2 = module_0.DataLoader()
        var_1 = data_loader_2.list_directory(data_loader_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xc3\xaa\xd6\xa9\xd3`\xc4\xe5\x0f*\x1b\xb9\x81]\xa3'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        list_0 = [set_0, set_0]
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim(list_0)
        str_0 = ';*DUSyq:biMoeA\tZQ'
        tuple_0 = (str_0,)
        list_1 = [tuple_0]
        data_loader_1 = module_0.DataLoader()
        var_1 = data_loader_1.list_directory(list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xc1\x08F\xec\xd2F\x139\x8e\x1f\xf1%\xcf\x89\xb6\x9e*\xbf'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_executable(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        data_loader_0 = module_0.DataLoader()
        bytes_0 = b'\xca\xff\x00\x19l\x9a\x02'
        str_0 = 'g.>aDS.7p"'
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/home/vivek/playboo.yml'
        var_0 = data_loader_0.get_real_file(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x18\xc6\xd6\xb3&\xfc'
        data_loader_0 = module_0.DataLoader()
        int_0 = 302
        bytes_1 = None
        var_0 = data_loader_0.path_dwim_relative_stack(bytes_0, int_0, bytes_1)
    except BaseException:
        pass

def test_case_8():
    try:
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.set_vault_secrets(data_loader_0)
        str_0 = 'x$7wMtO'
        var_1 = data_loader_0.get_real_file(data_loader_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        data_loader_0 = module_0.DataLoader()
        data_loader_1 = module_0.DataLoader()
        int_0 = None
        var_0 = data_loader_1.get_real_file(int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = ''
        dict_0 = {}
        var_0 = data_loader_0.load_from_file(str_0, dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        data_loader_0 = module_0.DataLoader()
        dict_0 = {data_loader_0: data_loader_0, data_loader_0: data_loader_0, data_loader_0: data_loader_0}
        list_0 = []
        set_0 = set()
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_1.path_dwim_relative_stack(dict_0, list_0, set_0)
    except BaseException:
        pass

def test_case_12():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = ''
        var_0 = data_loader_0.load_from_file(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        data_loader_0 = module_0.DataLoader()
        bytes_0 = b'\xca\xff\x00\x19\x83l\x9a\x02'
        str_0 = '.aDS.h47p'
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, bytes_0, str_0, data_loader_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '~M'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim(str_0)
        str_1 = 'qR5A{}r#nji3`R'
        set_0 = {str_1, str_1}
        data_loader_1 = module_0.DataLoader()
        var_1 = data_loader_1.path_exists(set_0)
        list_0 = [var_1]
        data_loader_2 = module_0.DataLoader()
        str_2 = 'bG'
        var_2 = data_loader_1.load_from_file(list_0, str_2, str_2)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = ''
        set_0 = {str_0, str_0}
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_basedir()
        list_0 = [str_0, set_0]
        data_loader_1 = module_0.DataLoader()
        var_1 = data_loader_1.path_dwim_relative_stack(set_0, str_0, str_0, list_0)
        data_loader_2 = module_0.DataLoader()
        bytes_0 = b'\x9f\x89\x92S\x14\xd0\x1e%\xfc'
        bool_0 = False
        var_2 = data_loader_1.path_dwim_relative_stack(data_loader_1, bytes_0, bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/dev/null'
        var_0 = data_loader_0.load_from_file(str_0)
        var_1 = data_loader_0.get_real_file(str_0)
        float_0 = None
        ansible_file_not_found_0 = None
        var_2 = data_loader_0.path_dwim_relative_stack(float_0, ansible_file_not_found_0, str_0)
        bool_0 = None
        data_loader_1 = module_0.DataLoader()
        tuple_0 = (str_0,)
        str_1 = 'h\rFTbKzom#PvTv@X'
        var_3 = data_loader_0.load_from_file(tuple_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '~D\x0bP*@EkV*OG9Z'
        data_loader_0 = module_0.DataLoader()
        set_0 = {str_0, str_0}
        list_0 = []
        var_0 = data_loader_0.cleanup_all_tmp_files()
        var_1 = data_loader_0.path_dwim_relative_stack(set_0, str_0, str_0, list_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = ''
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)
        var_1 = data_loader_0.cleanup_all_tmp_files()
        var_2 = data_loader_0.set_basedir(str_0)
        str_1 = 'h\rFT~Kzm#PvTv@X'
        var_3 = data_loader_0.is_file(str_1)
        set_0 = {str_1, str_1, str_1, var_0}
        list_0 = []
        data_loader_1 = module_0.DataLoader()
        var_4 = data_loader_1.path_dwim_relative_stack(set_0, str_1, str_1, list_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '+r9\x0b~-#1cP%)hm'
        str_1 = ''
        str_2 = '}kbyK4'
        tuple_0 = (str_2,)
        float_0 = 3101.751
        data_loader_0 = module_0.DataLoader()
        tuple_1 = (tuple_0, float_0, float_0, data_loader_0)
        bytes_0 = b'\xa6X\x91u\xebp\xe4\x86\x07V\xc8V\xd9\xb7bq9k\x19'
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_1.path_dwim_relative(str_0, str_1, tuple_1, bytes_0)
        int_0 = 91
        var_1 = data_loader_1.list_directory(int_0)
    except BaseException:
        pass

def test_case_20():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/dev/null'
        var_0 = data_loader_0.load_from_file(str_0)
        var_1 = data_loader_0.get_real_file(str_0)
        var_2 = data_loader_0.load_from_file(str_0)
        var_3 = data_loader_0.get_real_file(data_loader_0)
    except BaseException:
        pass

def test_case_21():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/dev/null'
        var_0 = data_loader_0.load_from_file(str_0)
        var_1 = data_loader_0.get_real_file(str_0)
        var_2 = data_loader_0.cleanup_all_tmp_files()
        bytes_0 = b'\xe5V\xde\xb2\x08\x10\r\x0f\xfb\x1d\x8d\xe3\xdc'
        str_1 = 'e9(C'
        var_3 = data_loader_0.load_from_file(str_0, bytes_0, str_1)
        str_2 = '%s.%s from %s'
        dict_0 = {str_2: var_3}
        data_loader_1 = module_0.DataLoader()
        var_4 = data_loader_1.get_real_file(dict_0)
    except BaseException:
        pass