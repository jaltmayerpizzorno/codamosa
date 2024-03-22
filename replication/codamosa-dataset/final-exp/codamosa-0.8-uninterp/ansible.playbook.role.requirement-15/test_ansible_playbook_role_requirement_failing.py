# Automatically generated by Pynguin.
import ansible.playbook.role.requirement as module_0

def test_case_0():
    try:
        str_0 = "Check parameters that are conditionally required\n\n    Raises :class:`TypeError` if the check fails\n\n    :arg requirements: List of lists specifying a parameter, value, parameters\n        required when the given parameter is the specified value, and optionally\n        a boolean indicating any or all parameters are required.\n\n    :Example:\n\n    .. code-block:: python\n\n        required_if=[\n            ['state', 'present', ('path',), True],\n            ['someint', 99, ('bool_param', 'string_param')],\n        ]\n\n    :arg parameters: Dictionary of parameters\n\n    :returns: Empty list or raises :class:`TypeError` if the check fails.\n        The results attribute of the exception contains a list of dictionaries.\n        Each dictionary is the result of evaluating each item in requirements.\n        Each return dictionary contains the following keys:\n\n            :key missing: List of parameters that are required but missing\n            :key requires: 'any' or 'all'\n            :key parameter: Parameter name that has the requirement\n            :key value: Original value of the parameter\n            :key requirements: Original required parameters\n\n        :Example:\n\n        .. code-block:: python\n\n            [\n                {\n                    'parameter': 'someint',\n                    'value': 99\n                    'requirements': ('bool_param', 'string_param'),\n                    'missing': ['string_param'],\n                    'requires': 'all',\n                }\n            ]\n\n    :kwarg options_context: List of strings of parent key names if ``requirements`` are\n        in a sub spec.\n    "
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        list_0 = [role_requirement_0, role_requirement_0, role_requirement_0, role_requirement_0]
        role_requirement_1 = module_0.RoleRequirement()
        var_0 = role_requirement_1.role_yaml_parse(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x89\xcb\xfb\xbc\xfe-\xed\xdeK\xe0\x8cVo'
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_requirement_0 = module_0.RoleRequirement()
        list_0 = [role_requirement_0]
        bool_0 = True
        var_0 = role_requirement_0.scm_archive_role(list_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xef\t\xd9c\x8c\xa2\x9a'
        tuple_0 = (bytes_0,)
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.repo_url_to_role_name(tuple_0)
        str_0 = 'E'
        role_requirement_1 = module_0.RoleRequirement()
        tuple_1 = ()
        dict_0 = {tuple_1: str_0}
        role_requirement_2 = module_0.RoleRequirement()
        str_1 = '\rd3T#azZ-^C!+gN'
        var_1 = role_requirement_2.role_yaml_parse(str_1)
        role_requirement_3 = module_0.RoleRequirement()
        var_2 = role_requirement_3.repo_url_to_role_name(str_1)
        var_3 = role_requirement_2.scm_archive_role(tuple_1, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Failed to get permanent hostname rc=%d, out=%s, err=%s'
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dg\x0brnd\\u2,\'#c-"'
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.repo_url_to_role_name(str_0)
        str_1 = 'c~yBD@iK/:DZ'
        role_requirement_1 = module_0.RoleRequirement()
        var_1 = role_requirement_1.repo_url_to_role_name(str_1)
        str_2 = 'D_Bum(<FV}^3;nG'
        var_2 = role_requirement_1.role_yaml_parse(str_2)
        str_3 = 'ys,0e.z'
        var_3 = role_requirement_0.repo_url_to_role_name(str_3)
        var_4 = role_requirement_1.role_yaml_parse(str_0)
        str_4 = '@%eV,0\x0bL*mL.\x0bUi@]js'
        var_5 = role_requirement_1.repo_url_to_role_name(str_4)
        var_6 = role_requirement_1.role_yaml_parse(var_4)
        list_0 = []
        var_7 = role_requirement_0.repo_url_to_role_name(list_0)
        var_8 = role_requirement_0.scm_archive_role(role_requirement_1, str_0, str_0)
    except BaseException:
        pass