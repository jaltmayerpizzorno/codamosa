# Automatically generated by Pynguin.
import ansible.executor.powershell.module_manifest as module_0

def test_case_0():
    try:
        tuple_0 = ()
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_exec_script(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b''
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        str_0 = 'redhatenterpriseserver'
        tuple_0 = None
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_module(bytes_0, set_0, str_0, tuple_0)
        bytes_1 = b'x\xf1)\xa9\x1d\xc5>b=\xc8Xl\x88\xb5=k'
        p_s_module_dep_finder_1 = module_0.PSModuleDepFinder()
        p_s_module_dep_finder_2 = module_0.PSModuleDepFinder()
        var_1 = p_s_module_dep_finder_2.scan_exec_script(bytes_1)
    except BaseException:
        pass

def test_case_2():
    try:
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        bytes_0 = b'#Requires -Module Ansible.ModuleUtils.Foo'
        var_0 = p_s_module_dep_finder_0.scan_module(bytes_0)
    except BaseException:
        pass