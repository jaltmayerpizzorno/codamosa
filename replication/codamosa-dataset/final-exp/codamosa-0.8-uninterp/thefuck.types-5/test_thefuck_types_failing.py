# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    try:
        str_0 = '6&2N'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        command_0 = module_0.Command(str_0, dict_0)
        var_0 = command_0.__repr__()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        list_0 = [bool_0]
        bytes_0 = b'\xf0\x96\x89\xf6\xb5s\x0co\xac\xf0'
        bytes_1 = None
        str_0 = '~IgP]VGpCr.gF&D'
        str_1 = '19B'
        float_0 = -3162.514
        tuple_0 = (float_0,)
        command_0 = module_0.Command(str_1, tuple_0)
        float_1 = 0.6
        rule_0 = module_0.Rule(command_0, bool_0, list_0, list_0, float_1, command_0, bool_0)
        command_1 = module_0.Command(str_0, rule_0)
        tuple_1 = (bytes_1, str_0, bytes_0, command_1)
        corrected_command_0 = module_0.CorrectedCommand(bytes_0, tuple_1, command_1)
        list_1 = []
        float_2 = -2813.2474
        rule_1 = module_0.Rule(bool_0, list_0, corrected_command_0, command_1, list_1, float_2, rule_0)
        var_0 = rule_1.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -1865.534338
        int_0 = -1036
        set_0 = set()
        str_0 = '@Edzoy%?'
        dict_0 = {str_0: int_0}
        corrected_command_0 = module_0.CorrectedCommand(int_0, set_0, dict_0)
        var_0 = corrected_command_0.run(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 834.310474
        set_0 = {float_0, float_0}
        list_0 = [float_0, set_0, set_0, set_0]
        str_0 = 'qvsN{iHyan?vuY\\RW[cz'
        str_1 = '%^QIie'
        str_2 = 'r\nA!\x0bkr\n>TI'
        dict_0 = {str_0: set_0, str_1: float_0, str_2: str_2}
        str_3 = 'NM?wt"'
        str_4 = 'Str?EQX`o+S&a8'
        tuple_0 = (dict_0, str_3, str_4)
        bytes_0 = b'f&\xe8Q\xd8\x9btd\xdaE\r<\x87\xb0z\xb5f\x92\xac\xb3'
        command_0 = module_0.Command(str_2, bytes_0)
        str_5 = '7o8`+TK>h, '
        set_1 = set()
        var_0 = command_0.__eq__(set_1)
        str_6 = None
        str_7 = 'enable'
        dict_1 = {str_5: str_4, str_3: dict_0, str_6: str_5, str_7: str_1}
        corrected_command_0 = module_0.CorrectedCommand(dict_0, command_0, dict_1)
        dict_2 = {str_1: command_0}
        float_1 = 2645.0
        rule_0 = module_0.Rule(tuple_0, corrected_command_0, dict_2, dict_2, bytes_0, bytes_0, float_1)
        var_1 = rule_0.__eq__(list_0)
        command_1 = module_0.Command(set_0, float_0)
        var_2 = command_1.__repr__()
        var_3 = corrected_command_0.run(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '<RHKR5jYNY\r7;1urKC-O'
        set_0 = {str_0, str_0}
        list_0 = [str_0, set_0, set_0]
        float_0 = None
        list_1 = [set_0, set_0, str_0, set_0]
        command_0 = module_0.Command(float_0, list_1)
        corrected_command_0 = None
        tuple_0 = (command_0, list_1, corrected_command_0)
        dict_0 = {}
        str_1 = 'OCkLTggJTC<'
        corrected_command_1 = module_0.CorrectedCommand(dict_0, str_1, command_0)
        list_2 = [corrected_command_0]
        bool_0 = True
        bool_1 = False
        rule_0 = module_0.Rule(bool_0, corrected_command_1, corrected_command_1, command_0, corrected_command_1, set_0, bool_1)
        var_0 = rule_0.get_corrected_commands(list_2)
        corrected_command_2 = module_0.CorrectedCommand(list_0, tuple_0, corrected_command_1)
        command_1 = module_0.Command(command_0, float_0)
        var_1 = command_0.__eq__(command_1)
        corrected_command_3 = module_0.CorrectedCommand(set_0, corrected_command_2, dict_0)
        var_2 = corrected_command_3.__hash__()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'npm i -S react'
        var_0 = None
        int_0 = 1765
        corrected_command_0 = module_0.CorrectedCommand(str_0, var_0, int_0)
        str_1 = 'npm i --save react'
        int_1 = 4
        corrected_command_1 = module_0.CorrectedCommand(str_1, var_0, int_1)
        str_2 = 'npm i -S'
        int_2 = 6
        corrected_command_2 = module_0.CorrectedCommand(str_2, var_0, int_2)
        str_3 = 'npm i'
        corrected_command_3 = module_0.CorrectedCommand(str_3, var_0, int_2)
        str_4 = 'npm install -S'
        corrected_command_4 = module_0.CorrectedCommand(str_4, var_0, int_1)
        int_3 = 0
        rule_0 = module_0.Rule(var_0, var_0, var_0, var_0, var_0, int_3, var_0)
        var_1 = rule_0.get_corrected_commands(var_0)
        var_2 = list(var_1)
    except BaseException:
        pass