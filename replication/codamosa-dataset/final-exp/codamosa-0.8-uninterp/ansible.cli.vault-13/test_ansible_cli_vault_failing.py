# Automatically generated by Pynguin.
import ansible.cli.vault as module_0

def test_case_0():
    try:
        str_0 = ''
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xdd\x8b\x94\xf8%\x10\xe5AMbz\xcfx'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        var_0 = vault_c_l_i_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xc0\n\xa9\x83\xee'
        set_0 = {bytes_0, bytes_0, bytes_0}
        int_0 = 1001
        str_0 = '%\\'
        str_1 = '@D'
        list_0 = [set_0, str_1, bytes_0]
        tuple_0 = (bytes_0, int_0, str_0, list_0)
        vault_c_l_i_0 = module_0.VaultCLI(tuple_0)
        var_0 = vault_c_l_i_0.init_parser()
        vault_c_l_i_1 = module_0.VaultCLI(set_0)
        var_1 = vault_c_l_i_1.execute_view()
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x13\xf1\x9f\x07.Y'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        var_0 = vault_c_l_i_0.post_process_args(vault_c_l_i_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'rC\x0civK&eaHBusn`Yn><C'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_encrypt()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -1969.015
        vault_c_l_i_0 = module_0.VaultCLI(float_0)
        var_0 = vault_c_l_i_0.execute_encrypt_string()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'a'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        var_0 = vault_c_l_i_0.execute_decrypt()
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        vault_c_l_i_0 = module_0.VaultCLI(bool_0)
        var_0 = vault_c_l_i_0.execute_create()
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = None
        list_0 = [float_0, float_0]
        vault_c_l_i_0 = module_0.VaultCLI(list_0)
        var_0 = vault_c_l_i_0.execute_edit()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '?-S(A\t'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_view()
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -1190.100962
        vault_c_l_i_0 = module_0.VaultCLI(float_0)
        var_0 = vault_c_l_i_0.execute_rekey()
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'?\x91n))Ka\xb9\x9d\x1a\xc3\x19'
        bytes_1 = b'\x03('
        vault_c_l_i_0 = module_0.VaultCLI(bytes_1)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = False
        set_0 = {bool_0}
        dict_0 = {bool_0: set_0, bool_0: set_0}
        vault_c_l_i_0 = module_0.VaultCLI(dict_0)
        vault_c_l_i_1 = module_0.VaultCLI(vault_c_l_i_0)
        str_0 = '\n                # fcinfo hba-port  | grep "Port WWN"\n                HBA Port WWN: 10000090fa1658de\n                '
        vault_c_l_i_2 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_2.format_ciphertext_yaml(bool_0, set_0, vault_c_l_i_1)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'\xc0\n\xa9\x83\xee'
        set_0 = {bytes_0, bytes_0, bytes_0}
        int_0 = 1001
        str_0 = '%\\'
        str_1 = '@D'
        list_0 = [set_0, str_1, bytes_0]
        set_1 = set()
        str_2 = 'n'
        vault_c_l_i_0 = module_0.VaultCLI(str_2)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(bytes_0, set_1)
        tuple_0 = (bytes_0, int_0, str_0, list_0)
        vault_c_l_i_1 = module_0.VaultCLI(tuple_0)
        var_1 = vault_c_l_i_1.init_parser()
        dict_0 = {str_0: var_0, var_1: vault_c_l_i_1, str_0: bytes_0}
        var_2 = vault_c_l_i_1.post_process_args(dict_0)
    except BaseException:
        pass