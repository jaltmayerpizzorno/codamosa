# Automatically generated by Pynguin.
import ansible.cli.vault as module_0

def test_case_0():
    try:
        str_0 = '/'
        set_0 = {str_0, str_0, str_0}
        vault_c_l_i_0 = module_0.VaultCLI(set_0)
        var_0 = vault_c_l_i_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'i*=(#2kw\n5'
        bytes_0 = b'\x8a\x82\xf2\xa3`|\xf8\x19-\xb6pH\xf8\xd5g=5\xbfbk'
        vault_c_l_i_0 = module_0.VaultCLI(bytes_0)
        var_0 = vault_c_l_i_0.post_process_args(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "b0 `'i7J9\x0cc"
        list_0 = [str_0, str_0, str_0]
        vault_c_l_i_0 = module_0.VaultCLI(list_0)
        var_0 = vault_c_l_i_0.execute_encrypt()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 1606.69
        bool_0 = True
        float_1 = 846.196811
        vault_c_l_i_0 = module_0.VaultCLI(float_1)
        vault_c_l_i_1 = module_0.VaultCLI(vault_c_l_i_0)
        var_0 = vault_c_l_i_1.format_ciphertext_yaml(float_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = None
        str_0 = None
        str_1 = 'ansible_ssh_host_key_'
        float_0 = -3966.52
        vault_c_l_i_0 = module_0.VaultCLI(float_0)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(tuple_0, str_0, str_1)
        str_2 = 's'
        bool_0 = False
        vault_c_l_i_1 = module_0.VaultCLI(str_2)
        var_1 = vault_c_l_i_1.format_ciphertext_yaml(bool_0)
        tuple_1 = None
        vault_c_l_i_2 = module_0.VaultCLI(tuple_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Failed to parse bus message'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_encrypt_string()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '2CwLE5BF-h`"$7Z)K'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_decrypt()
    except BaseException:
        pass

def test_case_7():
    try:
        vault_c_l_i_0 = None
        set_0 = {vault_c_l_i_0, vault_c_l_i_0, vault_c_l_i_0, vault_c_l_i_0}
        vault_c_l_i_1 = module_0.VaultCLI(set_0)
        var_0 = vault_c_l_i_1.execute_create()
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = None
        list_0 = [tuple_0]
        vault_c_l_i_0 = module_0.VaultCLI(list_0)
        var_0 = vault_c_l_i_0.execute_edit()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'Z\njQ"%!(Z&kK'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_view()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = "b0 `'i7J9\x0cc"
        set_0 = {str_0}
        vault_c_l_i_0 = module_0.VaultCLI(set_0)
        var_0 = vault_c_l_i_0.execute_rekey()
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = "f9kcS'?w{4k3\tbu\x0c"
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.init_parser()
        var_1 = vault_c_l_i_0.post_process_args(vault_c_l_i_0)
    except BaseException:
        pass