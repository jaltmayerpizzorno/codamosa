# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'E^Xb|o\t3$cIK'
    dict_0 = {str_0: str_0}
    list_0 = [dict_0]
    command_0 = module_0.Command(dict_0, list_0)

def test_case_2():
    str_0 = 'E^Xb|o\t3$cIK'
    dict_0 = {str_0: str_0}
    list_0 = [dict_0]
    command_0 = module_0.Command(dict_0, list_0)
    var_0 = command_0.__repr__()

def test_case_3():
    int_0 = 419
    str_0 = 'D(4q1`}(^cS'
    dict_0 = {str_0: str_0}
    command_0 = module_0.Command(int_0, dict_0)
    var_0 = command_0.update()

def test_case_4():
    str_0 = 'test_output'
    str_1 = 'fixed_script'
    bool_0 = False
    var_0 = None
    int_0 = 2
    rule_0 = module_0.Rule(str_0, str_0, str_1, bool_0, var_0, int_0, bool_0)
    command_0 = module_0.Command(str_1, str_0)
    var_1 = rule_0.is_match(command_0)
    var_2 = rule_0.is_match(command_0)
    str_2 = "z'st_scr7pt2"
    command_1 = module_0.Command(str_2, str_0)

def test_case_5():
    complex_0 = None
    float_0 = 0.1
    str_0 = '.t.<5Sg^\x0c.,bfW[X0'
    str_1 = 'm~n\r0^#3tKot_@(Jc'
    dict_0 = {str_1: float_0}
    list_0 = [str_1]
    dict_1 = None
    int_0 = 2
    corrected_command_0 = module_0.CorrectedCommand(dict_1, int_0, str_1)
    corrected_command_1 = module_0.CorrectedCommand(str_0, dict_0, list_0)
    list_1 = [str_0, float_0]
    float_1 = 0.6
    complex_1 = None
    set_0 = set()
    tuple_0 = (complex_1, list_1, float_0, set_0)
    rule_0 = module_0.Rule(float_0, corrected_command_1, dict_0, list_1, float_1, tuple_0, tuple_0)
    var_0 = rule_0.__eq__(complex_0)

def test_case_6():
    str_0 = 'Test Rule'
    str_1 = 'test_script'
    str_2 = 'test_output'
    var_0 = lambda cmd: cmd.script == str_1 and cmd.stdout == str_2
    str_3 = 'fixed_script'
    var_1 = lambda cmd: str_3
    bool_0 = True
    var_2 = None
    int_0 = 2
    rule_0 = module_0.Rule(str_0, var_0, var_1, bool_0, var_2, int_0, bool_0)
    command_0 = module_0.Command(str_1, str_2)
    var_3 = rule_0.__repr__()
    var_4 = rule_0.is_match(command_0)
    command_1 = module_0.Command(str_1, var_2)
    var_5 = rule_0.is_match(command_1)
    command_2 = module_0.Command(str_0, str_2)
    var_6 = rule_0.is_match(command_2)

def test_case_7():
    str_0 = 'echo 1'
    var_0 = None
    int_0 = 1
    corrected_command_0 = module_0.CorrectedCommand(str_0, var_0, int_0)
    var_1 = corrected_command_0.run(var_0)

def test_case_8():
    str_0 = None
    list_0 = [str_0, str_0, str_0]
    str_1 = 'xCyiIpd\t$\tg~4#[\x0bQO>'
    bytes_0 = None
    dict_0 = {str_0: bytes_0, str_1: list_0}
    str_2 = 'iex "$(thefuck --alias)"'
    dict_1 = {str_0: str_1, str_2: list_0}
    list_1 = [str_2, bytes_0]
    str_3 = 'c x"rqqFxd8<|;+ut'
    int_0 = -3438
    set_0 = {str_2, int_0, str_2}
    float_0 = 4731.0
    rule_0 = module_0.Rule(list_0, list_1, str_3, int_0, set_0, dict_0, float_0)
    corrected_command_0 = module_0.CorrectedCommand(dict_0, dict_1, rule_0)
    command_0 = module_0.Command(bytes_0, corrected_command_0)
    str_4 = 'f'
    str_5 = None
    rule_1 = module_0.Rule(list_0, command_0, str_4, float_0, str_5, bytes_0, dict_1)
    str_6 = 'JMkBi\x0cJ,svE3\n'
    dict_2 = {str_1: list_0, str_1: rule_1, str_6: int_0}
    command_1 = module_0.Command(list_0, dict_2)
    var_0 = command_1.__repr__()

def test_case_9():
    str_0 = None
    list_0 = [str_0, str_0, str_0]
    str_1 = 'xCyiIpd\t$\tg~4#[\x0bQO>'
    dict_0 = {str_0: str_1, str_0: list_0}
    str_2 = 'c x"rqqFxd8<|;+ut'
    str_3 = '\rS_N[#<Sava`2oy;9'
    tuple_0 = (str_3,)
    list_1 = [dict_0, str_2]
    str_4 = '67ErGB\\"\rTRs)vf\\w(zl'
    bool_0 = True
    corrected_command_0 = module_0.CorrectedCommand(list_1, str_4, bool_0)
    var_0 = corrected_command_0.__eq__(tuple_0)

def test_case_10():
    str_0 = 'cmd1'
    str_1 = 'e1'
    int_0 = 1
    corrected_command_0 = module_0.CorrectedCommand(str_0, str_1, int_0)
    corrected_command_1 = module_0.CorrectedCommand(str_0, str_1, int_0)
    var_0 = corrected_command_0 == corrected_command_1

def test_case_11():
    str_0 = 'Test Rule'
    str_1 = 'test_script'
    str_2 = 'test_output'
    str_3 = 'fixed_script'
    var_0 = lambda cmd: str_3
    bool_0 = True
    var_1 = None
    int_0 = 2
    rule_0 = module_0.Rule(str_0, str_2, var_0, bool_0, var_1, int_0, bool_0)
    command_0 = module_0.Command(str_1, str_2)
    var_2 = rule_0.is_match(command_0)
    command_1 = module_0.Command(str_1, var_1)
    var_3 = rule_0.is_match(command_1)
    str_4 = "z'st_scr7pt2"
    command_2 = module_0.Command(str_4, str_2)

def test_case_12():
    str_0 = 'test_output'
    str_1 = 'fixed_script'
    bool_0 = False
    var_0 = None
    int_0 = 2
    rule_0 = module_0.Rule(str_0, str_0, str_1, bool_0, var_0, int_0, bool_0)
    command_0 = module_0.Command(str_1, str_0)
    var_1 = rule_0.is_match(command_0)
    command_1 = module_0.Command(str_0, var_0)
    var_2 = rule_0.is_match(command_1)
    str_2 = "z'st_scr7pt2"
    command_2 = module_0.Command(str_2, str_0)