# Automatically generated by Pynguin.
import ansible.cli.vault as module_0
import ansible.utils.display as module_1

def test_case_0():
    try:
        str_0 = 'extend_group'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.init_parser()
        bool_0 = False
        var_1 = vault_c_l_i_0.post_process_args(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x16!V,,\x96\x97\xbb\xf9\xca'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        var_0 = vault_c_l_i_0.execute_encrypt()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '23Wo'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_encrypt_string()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 0.001
        vault_c_l_i_0 = module_0.VaultCLI(float_0)
        var_0 = vault_c_l_i_0.execute_decrypt()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "X('N!A9~Xq=vmy"
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_create()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "_W)!6vwvE2_p6O$}'tF_"
        tuple_0 = (str_0,)
        vault_c_l_i_0 = module_0.VaultCLI(tuple_0)
        var_0 = vault_c_l_i_0.execute_edit()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = None
        str_1 = '4~cV+X3^c'
        list_0 = [str_0, str_0, str_1]
        vault_c_l_i_0 = module_0.VaultCLI(list_0)
        var_0 = vault_c_l_i_0.execute_view()
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 4791
        vault_c_l_i_0 = module_0.VaultCLI(int_0)
        var_0 = vault_c_l_i_0.execute_rekey()
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -514
        tuple_0 = ()
        bool_0 = None
        str_0 = 'B#<By?!GZt`kt+%U\n\x0cu'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        dict_0 = {tuple_0: int_0, int_0: tuple_0, bool_0: bool_0}
        vault_c_l_i_1 = module_0.VaultCLI(int_0)
        var_0 = vault_c_l_i_1.format_ciphertext_yaml(dict_0, int_0)
        var_1 = vault_c_l_i_0.execute_create()
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\x16\xae\xdf\xf3\xb9\xda\xce5$L\xb5\xf4$\xea\xd1'
        bool_0 = True
        vault_c_l_i_0 = module_0.VaultCLI(bool_0)
        vault_c_l_i_1 = module_0.VaultCLI(vault_c_l_i_0)
        var_0 = vault_c_l_i_1.format_ciphertext_yaml(bytes_0)
        str_0 = "G9gA|n4kFYpQQ~/79L'"
        tuple_0 = (str_0,)
        bytes_1 = b''
        list_0 = [bytes_1]
        var_1 = vault_c_l_i_1.format_ciphertext_yaml(bytes_1, tuple_0, list_0)
        vault_c_l_i_2 = module_0.VaultCLI(tuple_0)
        vault_c_l_i_3 = module_0.VaultCLI(tuple_0)
        var_2 = vault_c_l_i_3.execute_encrypt_string()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '&`G)}2`en8Ga7we'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        display_0 = module_1.Display()
        str_1 = '>ot4LS@\rNQ]1iI:F'
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(str_1)
        var_1 = vault_c_l_i_0.init_parser()
        var_2 = vault_c_l_i_0.post_process_args(display_0)
    except BaseException:
        pass