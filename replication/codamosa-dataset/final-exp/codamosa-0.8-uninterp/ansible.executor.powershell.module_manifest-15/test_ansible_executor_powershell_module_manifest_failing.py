# Automatically generated by Pynguin.
import ansible.executor.powershell.module_manifest as module_0

def test_case_0():
    try:
        bool_0 = True
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_module(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        bytes_0 = b'#AnsibleRequires -PowerShell Ansible.ModuleUtils.Legacy.Facts'
        var_0 = p_s_module_dep_finder_0.scan_module(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        bool_0 = True
        var_0 = p_s_module_dep_finder_0.scan_exec_script(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xee\xf4d\xa9\xa8\x14\xfb\xd3\xda\xee\t[\xbaAR!\x0f\x98.'
        bytes_1 = b'\x90\xd0\xc0\xef\xbek\x17c'
        int_0 = 85
        bool_0 = None
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_module(bytes_0, bytes_1, int_0, bool_0)
        str_0 = ' used to print out a deprecation message.'
        float_0 = 100.0
        var_1 = p_s_module_dep_finder_0.scan_module(str_0, float_0)
    except BaseException:
        pass