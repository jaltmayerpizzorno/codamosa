# Automatically generated by Pynguin.
import ansible.module_utils.common.arg_spec as module_0

def test_case_0():
    try:
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator()
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        list_0 = []
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0, list_0)
        list_1 = None
        var_0 = argument_spec_validator_0.validate(list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        str_0 = 'okb'
        list_0 = [dict_0, dict_0]
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)
        var_0 = module_argument_spec_validator_0.validate(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'name'
        str_1 = 'agc'
        str_2 = ',]UXiF<^do}P`R2'
        str_3 = {str_2: str_2}
        str_4 = 'int'
        str_5 = {}
        str_6 = {str_0: str_3, str_1: str_5}
        list_0 = None
        validation_result_0 = module_0.ValidationResult(list_0)
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_6)
        tuple_0 = ()
        str_7 = 'bright green'
        set_0 = {argument_spec_validator_0, str_4, str_7, list_0}
        validation_result_1 = module_0.ValidationResult(set_0)
        bool_0 = True
        dict_0 = {validation_result_1: validation_result_1, tuple_0: list_0, validation_result_0: bool_0, str_2: bool_0}
        var_0 = argument_spec_validator_0.validate(dict_0)
    except BaseException:
        pass