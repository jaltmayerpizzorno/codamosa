# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    set_0 = None
    command_0 = module_0.Command(list_0, set_0)

def test_case_2():
    str_0 = '>9lKE2'
    bool_0 = False
    command_0 = module_0.Command(str_0, bool_0)
    corrected_command_0 = module_0.CorrectedCommand(str_0, bool_0, command_0)
    var_0 = command_0.__eq__(corrected_command_0)
    var_1 = corrected_command_0.run(corrected_command_0)

def test_case_3():
    str_0 = 'initialization required'
    bool_0 = True
    bool_1 = False
    rule_0 = module_0.Rule(str_0, bool_1, bool_1, bool_1, bool_1, bool_0, bool_0)
    command_0 = module_0.Command(str_0, str_0)
    var_0 = command_0.__repr__()
    var_1 = rule_0.is_match(command_0)

def test_case_4():
    str_0 = 'initialization required'
    bool_0 = True
    rule_0 = module_0.Rule(str_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0)
    command_0 = module_0.Command(str_0, str_0)
    var_0 = rule_0.is_match(command_0)

def test_case_5():
    str_0 = 'iniialization required'
    bool_0 = True
    rule_0 = module_0.Rule(str_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0)
    command_0 = module_0.Command(str_0, str_0)
    var_0 = rule_0.is_match(command_0)
    bool_1 = False
    var_1 = rule_0.__eq__(bool_1)

def test_case_6():
    str_0 = 'nitialzto# equied'
    bool_0 = False
    bool_1 = None
    rule_0 = module_0.Rule(str_0, bool_0, bool_0, bool_0, bool_1, bool_0, str_0)
    tuple_0 = ()
    bool_2 = True
    list_0 = [tuple_0, bool_2, tuple_0, rule_0]
    int_0 = 3986
    command_0 = module_0.Command(int_0, rule_0)
    var_0 = command_0.__repr__()
    corrected_command_0 = module_0.CorrectedCommand(str_0, tuple_0, list_0)
    var_1 = corrected_command_0.run(rule_0)
    command_1 = module_0.Command(str_0, str_0)
    var_2 = rule_0.is_match(command_1)
    bytes_0 = b'9v\x89'
    corrected_command_1 = module_0.CorrectedCommand(bytes_0, rule_0, command_1)

def test_case_7():
    str_0 = '>9lKE2'
    bool_0 = False
    command_0 = module_0.Command(str_0, bool_0)
    corrected_command_0 = module_0.CorrectedCommand(str_0, bool_0, command_0)
    var_0 = corrected_command_0.run(corrected_command_0)

def test_case_8():
    set_0 = None
    dict_0 = None
    float_0 = 0.85
    corrected_command_0 = module_0.CorrectedCommand(set_0, dict_0, float_0)
    str_0 = 'cp2V9['
    var_0 = corrected_command_0.__eq__(str_0)

def test_case_9():
    str_0 = '>9lKE2'
    bool_0 = False
    command_0 = module_0.Command(str_0, bool_0)
    corrected_command_0 = module_0.CorrectedCommand(str_0, bool_0, command_0)
    var_0 = corrected_command_0.__repr__()
    var_1 = corrected_command_0.run(corrected_command_0)

def test_case_10():
    bytes_0 = b'\xa1'
    dict_0 = {bytes_0: bytes_0}
    command_0 = module_0.Command(bytes_0, dict_0)
    str_0 = ' }l&e1AQ;JC'
    bool_0 = False
    var_0 = command_0.__repr__()
    int_0 = -1291
    str_1 = 'IfBB?G'
    list_0 = [bytes_0, str_1]
    list_1 = [bytes_0, command_0, list_0, str_1]
    str_2 = '='
    rule_0 = module_0.Rule(int_0, dict_0, list_1, str_2, str_2, bytes_0, command_0)
    command_1 = module_0.Command(dict_0, rule_0)
    int_1 = -1344
    corrected_command_0 = module_0.CorrectedCommand(list_0, command_1, int_1)
    str_3 = 'a'
    float_0 = 2.0711383805496273
    bytes_1 = None
    var_1 = command_0.__eq__(command_0)
    var_2 = rule_0.__eq__(command_0)
    tuple_0 = (dict_0, float_0, bytes_1)
    dict_1 = {}
    int_2 = -1017
    rule_1 = module_0.Rule(str_0, bool_0, str_3, dict_0, tuple_0, dict_1, int_2)
    var_3 = rule_1.is_match(command_0)

def test_case_11():
    str_0 = 'echo'
    var_0 = None
    int_0 = 0
    corrected_command_0 = module_0.CorrectedCommand(str_0, var_0, int_0)
    int_1 = 1
    corrected_command_1 = module_0.CorrectedCommand(str_0, var_0, int_1)
    var_1 = corrected_command_0 == corrected_command_1
    corrected_command_2 = module_0.CorrectedCommand(str_0, var_0, int_1)
    int_2 = 2
    corrected_command_3 = module_0.CorrectedCommand(str_0, var_0, int_2)
    var_2 = corrected_command_2 == corrected_command_3
    str_1 = 'ab'
    corrected_command_4 = module_0.CorrectedCommand(str_0, str_1, int_0)
    var_3 = corrected_command_4 == corrected_command_1
    corrected_command_5 = module_0.CorrectedCommand(str_0, str_1, int_1)
    corrected_command_6 = module_0.CorrectedCommand(str_0, str_1, int_2)
    var_4 = corrected_command_5 == corrected_command_6
    corrected_command_7 = module_0.CorrectedCommand(str_0, var_0, int_0)
    corrected_command_8 = module_0.CorrectedCommand(str_0, str_1, int_1)
    var_5 = corrected_command_7 == corrected_command_8
    corrected_command_9 = module_0.CorrectedCommand(str_0, str_1, int_1)
    corrected_command_10 = module_0.CorrectedCommand(str_0, var_0, int_0)
    var_6 = corrected_command_9 == corrected_command_10

def test_case_12():
    str_0 = 'test_rule1'
    bool_0 = True
    str_1 = 'test_output'
    var_0 = lambda x: str_1
    var_1 = None
    int_0 = 6
    bool_1 = False
    rule_0 = module_0.Rule(str_0, str_1, var_0, bool_0, var_1, int_0, bool_1)
    str_2 = 'test_rule2'
    var_2 = lambda x: bool_0
    var_3 = lambda x: str_1
    rule_1 = module_0.Rule(str_2, var_2, var_3, bool_0, var_1, int_0, bool_1)
    var_4 = rule_0 == rule_1
    str_3 = 'test_rule'
    var_5 = lambda x: bool_0
    str_4 = 'test_output1'
    var_6 = lambda x: str_4
    rule_2 = module_0.Rule(str_3, var_5, var_6, bool_0, var_1, int_0, bool_1)
    var_7 = lambda x: bool_0
    str_5 = 'test_output2'
    var_8 = lambda x: str_5
    rule_3 = module_0.Rule(str_3, var_7, var_8, bool_0, var_1, int_0, bool_1)

def test_case_13():
    str_0 = 'test_rule'
    bool_0 = True
    var_0 = lambda cmd: bool_0
    var_1 = lambda cmd: cmd.script
    bool_1 = False
    var_2 = None
    rule_0 = module_0.Rule(str_0, var_0, var_1, bool_1, var_2, bool_0, bool_0)
    list_0 = []
    tuple_0 = None
    command_0 = module_0.Command(list_0, tuple_0)
    var_3 = rule_0.is_match(command_0)

def test_case_14():
    str_0 = 'test_rule'
    bool_0 = False
    var_0 = lambda cmd: bool_0
    var_1 = lambda cmd: cmd.script
    var_2 = None
    rule_0 = module_0.Rule(str_0, var_0, var_1, bool_0, var_2, bool_0, bool_0)
    list_0 = []
    tuple_0 = None
    command_0 = module_0.Command(list_0, tuple_0)
    var_3 = rule_0.is_match(command_0)

def test_case_15():
    str_0 = 'test_ruule'
    bool_0 = True
    var_0 = lambda cmd: cmd.script
    rule_0 = module_0.Rule(str_0, var_0, var_0, bool_0, bool_0, var_0, bool_0)
    str_1 = '5'
    command_0 = module_0.Command(str_1, str_1)
    var_1 = rule_0.is_match(command_0)

def test_case_16():
    str_0 = 'test_rule'
    bool_0 = True
    var_0 = lambda cmd: bool_0
    var_1 = lambda cmd: cmd.script
    bool_1 = False
    var_2 = None
    rule_0 = module_0.Rule(str_0, var_1, var_1, bool_1, var_2, bool_0, bool_0)
    list_0 = None
    command_0 = module_0.Command(list_0, var_0)
    var_3 = rule_0.is_match(command_0)