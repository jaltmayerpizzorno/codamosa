# Automatically generated by Pynguin.
import ansible.cli.vault as module_0

def test_case_0():
    try:
        str_0 = '\\'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_encrypt()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'w\xf2R\x12\x15\xd7G\x95'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        var_0 = vault_c_l_i_0.init_parser()
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = None
        bool_0 = True
        vault_c_l_i_0 = module_0.VaultCLI(bool_0)
        var_0 = vault_c_l_i_0.post_process_args(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'xRCp#?V]G1s[O@!*|x'
        tuple_0 = ()
        bool_0 = False
        dict_0 = {bool_0: str_0, bool_0: str_0, bool_0: bool_0, bool_0: str_0}
        tuple_1 = (bool_0, dict_0)
        vault_c_l_i_0 = module_0.VaultCLI(tuple_1)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(tuple_0)
        var_1 = vault_c_l_i_0.run()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'w:'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_encrypt_string()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$vt'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_decrypt()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'R('
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_create()
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = -3256.0
        vault_c_l_i_0 = module_0.VaultCLI(float_0)
        var_0 = vault_c_l_i_0.execute_edit()
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = 42.7775
        vault_c_l_i_0 = module_0.VaultCLI(float_0)
        var_0 = vault_c_l_i_0.execute_view()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'j1'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_rekey()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'N1'
        bytes_0 = b'j\xea$\x15'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        list_0 = [bytes_0]
        set_0 = {vault_c_l_i_0, vault_c_l_i_0, str_0, vault_c_l_i_0}
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(list_0, set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'xRCp#?V]G1s[O@!*|x'
        tuple_0 = ()
        bool_0 = False
        dict_0 = {bool_0: str_0, bool_0: str_0, bool_0: bool_0, bool_0: str_0}
        tuple_1 = (bool_0, dict_0)
        vault_c_l_i_0 = module_0.VaultCLI(tuple_1)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(tuple_0)
        list_0 = [tuple_0, vault_c_l_i_0, bool_0]
        var_1 = vault_c_l_i_0.format_ciphertext_yaml(list_0, vault_c_l_i_0, tuple_1)
    except BaseException:
        pass