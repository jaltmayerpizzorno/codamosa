# Automatically generated by Pynguin.
import ansible.modules.dnf as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 22
    var_0 = module_0.main()
    bool_0 = False
    var_1 = module_0.main()
    var_2 = module_0.main()
    dnf_module_0 = module_0.DnfModule(bool_0)
    var_3 = dnf_module_0.list_items(int_0)
    var_4 = dnf_module_0.is_lockfile_pid_valid()
    int_1 = 36
    str_0 = '-{1P\x0c'
    var_5 = dnf_module_0.list_items(str_0)
    var_6 = dnf_module_0.run()
    var_7 = module_0.main()
    dnf_module_1 = module_0.DnfModule(int_1)
    var_8 = dnf_module_1.run()
    var_9 = dnf_module_1.is_lockfile_pid_valid()
    var_10 = dnf_module_1.list_items(dnf_module_1)
    str_1 = '}Kk+)'
    var_11 = dnf_module_0.list_items(str_1)
    var_12 = dnf_module_1.ensure()