# Automatically generated by Pynguin.
import ansible.module_utils.common.arg_spec as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)

def test_case_2():
    bool_0 = False
    dict_0 = {}
    list_0 = [dict_0, bool_0, bool_0, dict_0]
    module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)
    var_0 = module_argument_spec_validator_0.validate(dict_0)

def test_case_3():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)
    str_0 = 'Netconf'
    str_1 = '^BG8KMmz4oA^}b'
    dict_1 = {str_0: list_0, str_1: dict_0}
    var_0 = module_argument_spec_validator_0.validate(dict_1)

def test_case_4():
    str_0 = 'name'
    str_1 = 'type'
    str_2 = {str_1: str_0}
    str_3 = {str_0: str_2}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_3)
    str_4 = 'bob'
    str_5 = {str_0: str_4}
    var_0 = argument_spec_validator_0.validate(str_5)

def test_case_5():
    str_0 = 'foo'
    str_1 = 'type'
    str_2 = 'Unknown parameter type: %s'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    str_5 = 'bar'
    str_6 = {str_0: str_5}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_4)
    var_0 = argument_spec_validator_0.validate(str_6)
    var_1 = var_0.error_messages
    var_2 = var_0.validated_parameters