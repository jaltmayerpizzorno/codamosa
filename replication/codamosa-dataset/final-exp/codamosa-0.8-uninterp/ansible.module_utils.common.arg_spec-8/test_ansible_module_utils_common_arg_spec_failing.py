# Automatically generated by Pynguin.
import ansible.module_utils.common.arg_spec as module_0

def test_case_0():
    try:
        var_0 = {}
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_0)
        var_1 = argument_spec_validator_0.validate(argument_spec_validator_0)
    except BaseException:
        pass

def test_case_1():
    try:
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'n\x9d\x00\xc3\x0b\xb4\xdaD'
        dict_0 = {}
        dict_1 = {}
        list_0 = [bytes_0, dict_0, dict_1, dict_0]
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0, dict_1, list_0)
        bool_0 = True
        int_0 = None
        tuple_0 = (argument_spec_validator_0, bool_0, int_0, argument_spec_validator_0)
        str_0 = '?'
        int_1 = -2886
        list_1 = [dict_1, dict_1, str_0, tuple_0]
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_1, **dict_0)
        var_0 = module_argument_spec_validator_0.validate(int_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'n\x9d\x00\xc3\x0b\xb4\xdaD'
        dict_0 = {}
        dict_1 = {bytes_0: bytes_0}
        list_0 = [bytes_0, dict_0, dict_1, dict_0]
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0, dict_1, list_0)
        var_0 = argument_spec_validator_0.validate(dict_1)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0]
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)
        var_0 = module_argument_spec_validator_0.validate(dict_0)
        str_0 = None
        validation_result_0 = module_0.ValidationResult(str_0)
        str_1 = ''
        validation_result_1 = module_0.ValidationResult(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'options'
        str_1 = {str_0: str_0, str_0: str_0}
        str_2 = {str_0: str_1}
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_2)
        var_0 = argument_spec_validator_0.validate(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'nae'
        str_1 = 'age'
        str_2 = 'type'
        str_3 = 'ansible_ssh_private_key_file'
        str_4 = {str_2: str_3}
        str_5 = 'int'
        str_6 = {str_2: str_5}
        str_7 = {str_0: str_4, str_1: str_6}
        var_0 = []
        var_1 = []
        var_2 = []
        var_3 = []
        var_4 = []
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_7, var_0, var_1, var_2, var_3, var_4)
        str_8 = 'bo'
        str_9 = '42'
        str_10 = {str_0: str_8, str_1: str_9}
        var_5 = argument_spec_validator_0.validate(str_10)
    except BaseException:
        pass