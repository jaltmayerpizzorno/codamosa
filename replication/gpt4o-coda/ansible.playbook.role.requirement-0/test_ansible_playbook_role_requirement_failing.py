# Automatically generated by Pynguin.
import ansible.playbook.role.requirement as module_0

def test_case_0():
    try:
        bool_0 = False
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.repo_url_to_role_name(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        int_0 = -2303
        var_0 = role_requirement_0.role_yaml_parse(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 30
        dict_0 = {int_0: int_0, int_0: int_0}
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(dict_0)
        role_requirement_1 = module_0.RoleRequirement()
        var_1 = role_requirement_1.scm_archive_role(dict_0, int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        int_0 = 544
        var_0 = role_requirement_0.scm_archive_role(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        str_0 = ')C|PFb@,dE3|'
        var_0 = role_requirement_0.repo_url_to_role_name(str_0)
        role_requirement_1 = module_0.RoleRequirement()
        bytes_0 = b'1\x0e\xa1\x99\xccc\x1a %\x12\x1aw'
        var_1 = role_requirement_0.repo_url_to_role_name(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'The source inventory contains a non-string key (%s) which cannot be represented in TOML. The specified key will need to be converted to a string. Be aware that if your playbooks expect this key to be non-string, your playbooks will need to be modified to support this change.'
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(str_0)
        str_1 = 'kwr&BbgzzI@jnJO\x0c'
        role_requirement_1 = module_0.RoleRequirement()
        var_1 = role_requirement_1.role_yaml_parse(str_1)
        role_requirement_2 = module_0.RoleRequirement()
        str_2 = "\nThe ``distro`` package (``distro`` stands for Linux Distribution) provides\ninformation about the Linux distribution it runs on, such as a reliable\nmachine-readable distro ID, or version information.\n\nIt is the recommended replacement for Python's original\n:py:func:`platform.linux_distribution` function, but it provides much more\nfunctionality. An alternative implementation became necessary because Python\n3.5 deprecated this function, and Python 3.8 removed it altogether. Its\npredecessor function :py:func:`platform.dist` was already deprecated since\nPython 2.6 and removed in Python 3.8. Still, there are many cases in which\naccess to OS distribution information is needed. See `Python issue 1322\n<https://bugs.python.org/issue1322>`_ for more information.\n"
        var_2 = role_requirement_1.role_yaml_parse(str_2)
    except BaseException:
        pass