# Automatically generated by Pynguin.
import ansible.cli.vault as module_0
import ansible.utils.display as module_1

def test_case_0():
    try:
        str_0 = 'RBbOu@ZS*<RZ!mfb'
        list_0 = [str_0, str_0, str_0]
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(list_0)
        var_1 = vault_c_l_i_0.init_parser()
        var_2 = vault_c_l_i_0.execute_edit()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '|i%'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.init_parser()
        str_1 = "Expecting requirements file to be a dict with the key 'collections' that contains a list of collections to install"
        vault_c_l_i_1 = module_0.VaultCLI(str_1)
        display_0 = module_1.Display(vault_c_l_i_1)
        var_1 = vault_c_l_i_0.post_process_args(display_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1839
        vault_c_l_i_0 = module_0.VaultCLI(int_0)
        var_0 = vault_c_l_i_0.run()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'seealso'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_encrypt()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "\n?06oQ'Y`o|6W\\Kc-|;I"
        float_0 = -1250.126
        set_0 = {str_0, str_0, float_0, float_0}
        str_1 = '0y28'
        vault_c_l_i_0 = module_0.VaultCLI(str_1)
        var_0 = vault_c_l_i_0.format_ciphertext_yaml(str_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        vault_c_l_i_0 = module_0.VaultCLI(bool_0)
        var_0 = vault_c_l_i_0.execute_encrypt_string()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'RBbOu@ZS*<RZ!mfb'
        list_0 = [str_0, str_0, str_0]
        vault_c_l_i_0 = module_0.VaultCLI(list_0)
        var_0 = vault_c_l_i_0.execute_decrypt()
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = -2207.647
        vault_c_l_i_0 = module_0.VaultCLI(float_0)
        var_0 = vault_c_l_i_0.execute_create()
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 5
        vault_c_l_i_0 = module_0.VaultCLI(int_0)
        var_0 = vault_c_l_i_0.execute_edit()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'DA5`]o'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_view()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = ',n=+}:Qs@!~pX>rO)hM'
        vault_c_l_i_0 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_0.execute_rekey()
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'RBbOuZS*<R!mf'
        list_0 = [str_0, str_0, str_0]
        vault_c_l_i_0 = module_0.VaultCLI(list_0)
        str_1 = '|0M!w*QuZ6tJv'
        float_0 = 100.0
        str_2 = 'obj must be a list ofdicts or a nested dict'
        vault_c_l_i_1 = module_0.VaultCLI(str_0)
        var_0 = vault_c_l_i_1.format_ciphertext_yaml(str_1, float_0, str_2)
    except BaseException:
        pass