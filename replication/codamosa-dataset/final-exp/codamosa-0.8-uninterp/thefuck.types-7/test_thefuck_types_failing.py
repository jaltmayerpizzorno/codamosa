# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    try:
        float_0 = 0.5
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        list_0 = [dict_0, float_0, float_0]
        corrected_command_0 = module_0.CorrectedCommand(float_0, dict_0, list_0)
        var_0 = corrected_command_0.__hash__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'g~z?74:'
        bool_0 = False
        str_1 = 'Q~}`}Sk0-kwm'
        str_2 = "Ou+^xop'"
        str_3 = 'git branch -D {0}'
        dict_0 = {str_1: str_2, str_0: bool_0, str_3: str_1, str_3: bool_0}
        corrected_command_0 = module_0.CorrectedCommand(str_0, bool_0, dict_0)
        var_0 = corrected_command_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -631.800258
        bytes_0 = b'\xe5\xfa\x1f\xe6\xadL:\xae\xd5\x81'
        float_1 = 1800.2
        command_0 = module_0.Command(bytes_0, float_1)
        float_2 = -2354.757
        set_0 = {float_2}
        corrected_command_0 = module_0.CorrectedCommand(command_0, float_2, set_0)
        var_0 = corrected_command_0.run(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'name'
        var_0 = None
        rule_0 = module_0.Rule(str_0, var_0, var_0, var_0, var_0, var_0, var_0)
        str_1 = 'command-from-input'
        command_0 = module_0.Command(str_1, var_0)
        var_1 = rule_0.get_corrected_commands(command_0)
        var_2 = next(var_1)
    except BaseException:
        pass