# Automatically generated by Pynguin.
import ansible.module_utils.common.arg_spec as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = "`Pc wjW=e'"
    dict_0 = {str_0: str_0}
    dict_1 = {}
    list_0 = [dict_1]
    module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)
    var_0 = module_argument_spec_validator_0.validate(dict_0)
    validation_result_0 = module_0.ValidationResult(str_0)

def test_case_2():
    str_0 = 'name'
    str_1 = {str_0: str_0}
    str_2 = {str_0: str_0, str_0: str_1}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_2)

def test_case_3():
    var_0 = {}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_0)
    var_1 = {}
    var_2 = argument_spec_validator_0.validate(var_1)

def test_case_4():
    str_0 = 'name'
    str_1 = 'age'
    str_2 = 'type'
    str_3 = {str_2: str_1}
    str_4 = {str_2: str_0}
    str_5 = {str_0: str_3, str_1: str_4}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_5)
    var_0 = argument_spec_validator_0.validate(str_3)
    var_1 = var_0.validated_parameters
    var_2 = len(str_2)

def test_case_5():
    str_0 = 'name'
    str_1 = 'age'
    str_2 = 'type'
    str_3 = 'str'
    str_4 = {str_2: str_3}
    str_5 = 'int'
    str_6 = {str_2: str_5}
    str_7 = {str_0: str_4, str_1: str_6}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_7)
    var_0 = argument_spec_validator_0.validate(str_4)
    var_1 = var_0.validated_parameters
    var_2 = var_0.error_messages
    var_3 = len(var_2)