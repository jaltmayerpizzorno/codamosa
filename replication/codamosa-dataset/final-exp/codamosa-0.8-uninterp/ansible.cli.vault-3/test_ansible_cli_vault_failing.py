# Automatically generated by Pynguin.
import ansible.cli.vault as module_0

def test_case_0():
    try:
        str_0 = '.Pk!/'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.init_parser()
        var_1 = vault_c_l_i_0.post_process_args(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -673.565405
        bool_0 = True
        dict_0 = {bool_0: float_0, float_0: float_0, bool_0: float_0, bool_0: float_0}
        bytes_0 = b"L\x05\x93\x9e\x07\x07.\x08\xc6'"
        set_0 = {bytes_0}
        tuple_0 = (bool_0, dict_0, dict_0, set_0)
        vault_c_l_i_0 = module_0.VaultCLI(tuple_0)
        var_0 = vault_c_l_i_0.execute_encrypt()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\n        Adjusts play datastructure to cleanup old/legacy items\n        '
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_encrypt_string()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -4890
        vault_c_l_i_0 = module_0.VaultCLI(int_0)
        var_0 = vault_c_l_i_0.execute_decrypt()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -196
        vault_c_l_i_0 = module_0.VaultCLI(int_0)
        var_0 = vault_c_l_i_0.execute_create()
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x9f\xb6\x90\xb8\xc2RK\x1d\xfd\xf3'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        var_0 = vault_c_l_i_0.execute_edit()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'ts^ zG'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_view()
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        vault_c_l_i_0 = module_0.VaultCLI(bool_0)
        var_0 = vault_c_l_i_0.execute_rekey()
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = 2.0
        str_0 = 'installing from %s'
        bytes_0 = b'j\x84k\xf7\x00nh\x03'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(float_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = None
        list_1 = [list_0, list_0, list_0]
        bool_0 = True
        bytes_0 = b'\x03\xbe\xd7\xaa\x93\xab\x88\xb7\xf3*\x14`\t'
        str_0 = 'Q(OrI<'
        set_0 = {list_0, bool_0}
        vault_c_l_i_0 = module_0.VaultCLI(set_0)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(bytes_0, str_0, list_1)
    except BaseException:
        pass