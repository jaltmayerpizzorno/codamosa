# Automatically generated by Pynguin.
import ansible.modules.command as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b't\xf6W\x16\x1e\x87\xf5\xae\xc9\x1c\xb8W`M'
    set_0 = {bytes_0}
    str_0 = 'n'
    var_0 = module_0.check_command(set_0, str_0)

def test_case_2():
    var_0 = module_0.main()