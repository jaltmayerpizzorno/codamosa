# Automatically generated by Pynguin.
import ansible.executor.powershell.module_manifest as module_0
import ansible.module_utils.common.text.converters as module_1

def test_case_0():
    try:
        str_0 = 'Q\x0cI"'
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_module(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_exec_script(p_s_module_dep_finder_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '#Requires -Module Ansible.ModuleUtils.foo,\n    #Requires -Module Ansible.ModuleUtils.bar\n    #Requires -Module Ansible.ModuleUtils.bar2\n    #AnsibleRequires -PowerShell Ansible.ModuleUtils.foo2\n    #AnsibleRequires -PowerShell Ansible.ModuleUtils.foo3\n    #AnsibleRequires -CSharpUtil Ansible.Foo\n    #AnsibleRequires -CSharpUtil ansible_collections.namespace.coll.plugins.module_utils.foo2\n    #AnsibleRequires -CSharpUtil ..module_utils.foo3\n    '
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = module_1.to_bytes(str_0)
        var_1 = p_s_module_dep_finder_0.scan_module(var_0)
    except BaseException:
        pass