# Automatically generated by Pynguin.
import ansible.playbook.role.requirement as module_0

def test_case_0():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        list_0 = []
        bool_0 = None
        list_1 = [role_requirement_0, role_requirement_0, list_0, bool_0]
        var_0 = role_requirement_0.role_yaml_parse(list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x9a'
        role_requirement_0 = module_0.RoleRequirement()
        role_requirement_1 = module_0.RoleRequirement()
        var_0 = role_requirement_1.role_yaml_parse(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b''
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.scm_archive_role(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(dict_0)
        dict_1 = {}
        str_0 = 'li.mv,/!=>vojJ& A"nj'
        role_requirement_1 = module_0.RoleRequirement()
        var_1 = role_requirement_1.role_yaml_parse(str_0)
        role_requirement_2 = module_0.RoleRequirement()
        var_2 = role_requirement_2.repo_url_to_role_name(dict_1)
        role_requirement_3 = module_0.RoleRequirement()
        role_requirement_4 = module_0.RoleRequirement()
        role_requirement_5 = module_0.RoleRequirement()
        var_3 = role_requirement_1.role_yaml_parse(var_1)
        str_1 = '[5B(|Zp$P/;l.'
        var_4 = role_requirement_3.repo_url_to_role_name(str_1)
        role_requirement_6 = module_0.RoleRequirement()
        int_0 = 2385
        var_5 = role_requirement_2.scm_archive_role(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        str_0 = 'foo,bar,baz'
        var_0 = role_requirement_0.role_yaml_parse(str_0)
        int_0 = 4096
        var_1 = role_requirement_0.role_yaml_parse(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Remove strings in ``no_log_strings`` from value.\n\n    If value is a container type, then remove a lot more.\n\n    Use of ``deferred_removals`` exists, rather than a pure recursive solution,\n    because of the potential to hit the maximum recursion depth when dealing with\n    large amounts of data (see `issue #24560 <https://github.com/ansible/ansible/issues/24560>`_).\n    '
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(str_0)
    except BaseException:
        pass