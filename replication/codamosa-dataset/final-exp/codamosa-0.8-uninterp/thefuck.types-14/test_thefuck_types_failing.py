# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    try:
        dict_0 = None
        dict_1 = {}
        str_0 = 'X*P/?g~8R]#~ZfRv\x0bl'
        str_1 = 'A'
        str_2 = "F\\'aav*eJG"
        str_3 = 'e5-G>ld{!y*lms/3mS'
        dict_2 = {str_0: str_1, str_2: str_1, str_3: str_2}
        command_0 = module_0.Command(str_1, dict_2)
        command_1 = module_0.Command(command_0, command_0)
        float_0 = 2022.116
        complex_0 = None
        bytes_0 = b'!\xc5\xd6G\x14\xfb4\xc3\xeaM\xcc\xfe;\x07\x80(\x1c\xa7\xe0\xff'
        corrected_command_0 = module_0.CorrectedCommand(float_0, complex_0, bytes_0)
        list_0 = [command_0, command_1]
        bool_0 = False
        var_0 = command_1.__eq__(bool_0)
        command_2 = module_0.Command(command_1, list_0)
        int_0 = -581
        corrected_command_1 = module_0.CorrectedCommand(command_2, dict_1, int_0)
        corrected_command_2 = module_0.CorrectedCommand(dict_1, str_0, corrected_command_1)
        var_1 = corrected_command_2.run(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '1-cl'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        str_1 = 'python '
        set_0 = set()
        list_0 = []
        command_0 = module_0.Command(set_0, list_0)
        command_1 = module_0.Command(str_1, command_0)
        list_1 = [dict_0, str_0, str_0]
        command_2 = module_0.Command(list_1, list_1)
        var_0 = command_2.__eq__(command_1)
        dict_1 = {str_0: str_0, str_0: dict_0}
        str_2 = '3mjC]\x0cRXV}QA\n'
        bytes_0 = None
        corrected_command_0 = module_0.CorrectedCommand(bytes_0, list_0, list_0)
        str_3 = "J|>Z}QQaq'uL"
        command_3 = module_0.Command(str_2, str_3)
        var_1 = command_3.update(**dict_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        int_0 = 1453
        str_0 = '&f\t;aUM1'
        command_0 = module_0.Command(str_0, int_0)
        int_1 = -739
        tuple_0 = ()
        tuple_1 = (command_0, int_1, tuple_0)
        str_1 = 'c26_z@]#a%B<^@['
        float_0 = 750.0
        corrected_command_0 = module_0.CorrectedCommand(tuple_1, str_1, float_0)
        command_1 = module_0.Command(bool_0, int_0)
        str_2 = '1IG<@8.pziZd'
        str_3 = 'U_bF@lC,lB\r=\tqZ>$f^'
        dict_0 = {str_3: str_2}
        list_0 = [command_1, int_0]
        command_2 = module_0.Command(dict_0, list_0)
        corrected_command_1 = module_0.CorrectedCommand(str_2, command_2, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = None
        dict_1 = {}
        str_0 = 'X*P/?g~8R]#~ZfRv\x0bl'
        str_1 = 'A'
        str_2 = "F\\'aav*eJG"
        str_3 = 'e5-G>ld{!y*lms/3mS'
        dict_2 = {str_0: str_1, str_2: str_1, str_3: str_2}
        command_0 = module_0.Command(str_1, dict_2)
        command_1 = module_0.Command(command_0, command_0)
        list_0 = [command_0, command_1]
        command_2 = module_0.Command(command_1, list_0)
        int_0 = -581
        corrected_command_0 = module_0.CorrectedCommand(command_2, dict_1, int_0)
        corrected_command_1 = module_0.CorrectedCommand(dict_1, str_0, corrected_command_0)
        var_0 = corrected_command_1.run(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'a'
        bool_0 = False
        var_0 = lambda cmd: bool_0
        var_1 = lambda cmd: cmd
        bool_1 = True
        var_2 = None
        int_0 = 2
        rule_0 = module_0.Rule(str_0, var_0, var_1, bool_1, var_2, int_0, bool_1)
        str_1 = ''
        command_0 = module_0.Command(str_1, str_1)
        var_3 = rule_0.get_corrected_commands(command_0)
        var_4 = tuple(var_3)
        corrected_command_0 = module_0.CorrectedCommand(str_1, var_2, int_0)
        var_5 = lambda cmd: bool_0
        var_6 = lambda cmd: [cmd, cmd]
        rule_1 = module_0.Rule(str_0, var_5, var_6, bool_1, var_2, int_0, bool_1)
        var_7 = rule_1.get_corrected_commands(command_0)
        var_8 = tuple(var_7)
        corrected_command_1 = module_0.CorrectedCommand(str_1, var_2, int_0)
        int_1 = 4
        corrected_command_2 = module_0.CorrectedCommand(str_1, var_2, int_1)
        var_9 = lambda cmd: var_7
        var_10 = lambda cmd: str_1
        rule_2 = module_0.Rule(str_0, var_9, var_10, bool_1, var_2, int_0, bool_1)
        command_1 = module_0.Command(str_1, str_1)
        var_11 = tuple(rule_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'rule1'
        bool_0 = False
        var_0 = lambda c: bool_0
        str_1 = 'out1'
        str_2 = 'out2'
        str_3 = [str_1, str_2]
        var_1 = lambda c: str_3
        bool_1 = True
        var_2 = None
        int_0 = 100
        rule_0 = module_0.Rule(str_0, var_0, var_1, bool_1, var_2, int_0, bool_0)
        str_4 = ''
        command_0 = module_0.Command(str_4, var_2)
        var_3 = rule_0.get_corrected_commands(command_0)
        var_4 = list(var_3)
    except BaseException:
        pass