# Automatically generated by Pynguin.
import ansible.module_utils.common.arg_spec as module_0

def test_case_0():
    try:
        int_0 = None
        validation_result_0 = None
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(int_0, validation_result_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '9,\t4gGg`<RMe0'
        dict_0 = {str_0: str_0}
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator()
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        float_0 = 1000.0
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0)
        var_0 = argument_spec_validator_0.validate(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'argument_spec'
        str_1 = 'name'
        str_2 = 'type'
        str_3 = {str_2: str_1}
        str_4 = {str_1: str_3}
        str_5 = {str_0: str_4}
        var_0 = {str_1: str_4}
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(**str_5)
        var_1 = module_argument_spec_validator_0.validate(var_0)
        str_6 = 'Errors: '
        var_2 = var_1.errors
        var_3 = str_6 + str_3
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '`>jN:6qP!'
        list_0 = [str_0, str_0, str_0]
        dict_0 = {}
        list_1 = [dict_0, str_0, list_0, str_0, list_0]
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_1)
        var_0 = module_argument_spec_validator_0.validate(dict_0)
    except BaseException:
        pass