# Automatically generated by Pynguin.
import ansible.cli.vault as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -2540
    vault_c_l_i_0 = module_0.VaultCLI(int_0)

def test_case_2():
    str_0 = 'keyword'
    str_1 = 'check mode is currently %s.'
    vault_c_l_i_0 = module_0.VaultCLI(str_1)
    var_0 = vault_c_l_i_0.run()
    list_0 = [str_0, str_0, str_0, str_0]
    dict_0 = {}
    vault_c_l_i_1 = module_0.VaultCLI(dict_0)
    var_1 = vault_c_l_i_1.format_ciphertext_yaml(str_0, list_0)