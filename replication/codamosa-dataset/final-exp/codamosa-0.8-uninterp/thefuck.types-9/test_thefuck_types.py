# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    bytes_0 = b'7\x00($\xe4\x88\xdc\xe7\xb8\xf4s\xc7:\xd1KFC\xd9P'
    command_0 = module_0.Command(bool_0, bytes_0)

def test_case_2():
    str_0 = 'QZl#lpU3M1JtCqw}'
    dict_0 = {str_0: str_0}
    str_1 = 'k]6~lGc.9=D'
    bytes_0 = b'\xb6z\xc66O\xc2'
    bytes_1 = None
    str_2 = ''
    int_0 = 1860
    float_0 = -1772.3
    corrected_command_0 = module_0.CorrectedCommand(str_2, int_0, float_0)
    var_0 = corrected_command_0.__eq__(bytes_1)
    command_0 = module_0.Command(str_1, bytes_0)
    var_1 = command_0.__eq__(dict_0)

def test_case_3():
    str_0 = "6'@\tk"
    set_0 = {str_0}
    command_0 = module_0.Command(str_0, set_0)
    tuple_0 = ()
    dict_0 = {}
    corrected_command_0 = module_0.CorrectedCommand(dict_0, tuple_0, dict_0)
    int_0 = -694
    rule_0 = module_0.Rule(command_0, tuple_0, dict_0, corrected_command_0, int_0, set_0, command_0)
    var_0 = rule_0.__repr__()

def test_case_4():
    bytes_0 = None
    bool_0 = False
    float_0 = -2152.65
    command_0 = module_0.Command(bool_0, float_0)
    var_0 = command_0.update()
    dict_0 = {bytes_0: float_0, bytes_0: bytes_0, bytes_0: bytes_0}
    bytes_1 = b'g3CT\xd4\x10'
    str_0 = '\rYpPse?# j66e'
    rule_0 = module_0.Rule(dict_0, str_0, bytes_1, dict_0, str_0, str_0, float_0)
    var_1 = rule_0.is_match(command_0)
    bool_1 = False
    var_2 = rule_0.get_corrected_commands(bool_1)

def test_case_5():
    str_0 = ''
    int_0 = 5
    var_0 = lambda x: x
    bool_0 = False
    rule_0 = module_0.Rule(str_0, bool_0, str_0, bool_0, str_0, int_0, bool_0)
    command_0 = module_0.Command(str_0, str_0)
    var_1 = rule_0.is_match(command_0)
    command_1 = module_0.Command(str_0, str_0)

def test_case_6():
    float_0 = 0.85
    int_0 = -4511
    bool_0 = True
    str_0 = 'l"uca\nU=d7'
    bytes_0 = b''
    rule_0 = module_0.Rule(float_0, int_0, bool_0, str_0, bytes_0, bytes_0, int_0)
    var_0 = rule_0.__eq__(float_0)

def test_case_7():
    float_0 = 4141.1435
    dict_0 = {float_0: float_0}
    command_0 = None
    tuple_0 = (dict_0, dict_0)
    corrected_command_0 = module_0.CorrectedCommand(dict_0, command_0, tuple_0)

def test_case_8():
    bool_0 = True
    tuple_0 = ()
    int_0 = 28
    list_0 = []
    corrected_command_0 = module_0.CorrectedCommand(tuple_0, int_0, list_0)
    var_0 = corrected_command_0.__eq__(bool_0)

def test_case_9():
    bool_0 = False
    str_0 = 'RM3K\'Dn}=+4<}sK"Dd'
    bool_1 = False
    str_1 = 'x}Id*45lr\rw'
    corrected_command_0 = module_0.CorrectedCommand(str_0, bool_1, str_1)
    set_0 = {corrected_command_0, str_0, str_1}
    str_2 = 'j'
    bytes_0 = b'\x1dy\x8fp'
    corrected_command_1 = module_0.CorrectedCommand(set_0, str_2, bytes_0)
    var_0 = corrected_command_1.__eq__(bool_0)

def test_case_10():
    str_0 = "fatal: not removing '"
    set_0 = set()
    bool_0 = True
    corrected_command_0 = module_0.CorrectedCommand(str_0, set_0, bool_0)
    list_0 = [set_0]
    corrected_command_1 = module_0.CorrectedCommand(corrected_command_0, bool_0, list_0)
    var_0 = corrected_command_1.__repr__()

def test_case_11():
    bytes_0 = None
    float_0 = -260.287506
    bytes_1 = b'H\xdc\xfa\xb9\xde\x0b\xaa\xc7\xbc\x175\x93'
    bytes_2 = b'*\xec'
    dict_0 = {}
    str_0 = "qp06^'"
    dict_1 = {str_0: float_0}
    list_0 = [dict_1]
    corrected_command_0 = module_0.CorrectedCommand(bytes_2, dict_0, list_0)
    dict_2 = {bytes_0: float_0}
    bool_0 = True
    command_0 = module_0.Command(bytes_1, bool_0)
    command_1 = module_0.Command(corrected_command_0, float_0)
    var_0 = command_1.__eq__(command_0)
    command_2 = module_0.Command(float_0, dict_2)
    var_1 = command_2.__eq__(bytes_0)
    bool_1 = True
    command_3 = module_0.Command(bool_1, float_0)
    var_2 = command_3.update()
    dict_3 = {bytes_0: float_0, bytes_0: bytes_0, bytes_0: bytes_0}
    str_1 = '$bdpC^rz"(Q!\'*'
    bytes_3 = b'g3CT\xd4\x10'
    str_2 = '\rYpPse?# j66e'
    rule_0 = module_0.Rule(dict_3, str_1, bytes_3, dict_3, str_2, str_1, float_0)
    var_3 = rule_0.is_match(command_3)
    dict_4 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    bool_2 = False
    bool_3 = True
    corrected_command_1 = module_0.CorrectedCommand(bool_1, bool_3, rule_0)
    var_4 = corrected_command_1.__eq__(str_1)
    var_5 = rule_0.get_corrected_commands(bool_2)
    bytes_4 = b'l\\O[\xebk+\xfbf\x0e|\x9b\x10\xc5'
    set_0 = {float_0, float_0}
    command_4 = module_0.Command(bytes_4, set_0)
    bytes_5 = b'f\x1b\xd9\x0e'
    rule_1 = module_0.Rule(dict_4, dict_4, dict_1, command_4, bytes_4, bytes_5, float_0)

def test_case_12():
    str_0 = ''
    var_0 = lambda x: x
    var_1 = None
    int_0 = 5
    command_0 = module_0.Command(str_0, var_1)
    var_2 = lambda x: x
    bool_0 = False
    rule_0 = module_0.Rule(str_0, var_0, var_2, bool_0, var_1, int_0, bool_0)
    var_3 = rule_0.is_match(command_0)
    rule_1 = module_0.Rule(str_0, bool_0, var_0, bool_0, var_1, int_0, bool_0)
    var_4 = rule_1.is_match(command_0)
    rule_2 = module_0.Rule(str_0, command_0, command_0, bool_0, var_1, int_0, bool_0)
    var_5 = rule_1.is_match(command_0)

def test_case_13():
    str_0 = 'a'
    var_0 = None
    int_0 = 1
    corrected_command_0 = module_0.CorrectedCommand(str_0, var_0, int_0)
    corrected_command_1 = module_0.CorrectedCommand(str_0, var_0, int_0)
    var_1 = corrected_command_0.__eq__(corrected_command_1)
    corrected_command_2 = module_0.CorrectedCommand(str_0, var_0, int_0)
    str_1 = 'b'
    corrected_command_3 = module_0.CorrectedCommand(str_1, var_0, int_0)
    var_2 = corrected_command_2.__eq__(corrected_command_3)
    corrected_command_4 = module_0.CorrectedCommand(str_0, var_0, int_0)
    int_1 = 2
    corrected_command_5 = module_0.CorrectedCommand(str_0, var_0, int_1)
    var_3 = corrected_command_4.__eq__(corrected_command_5)
    corrected_command_6 = module_0.CorrectedCommand(str_0, var_0, int_0)
    corrected_command_7 = module_0.CorrectedCommand(str_0, var_0, var_0)
    var_4 = corrected_command_6.__eq__(corrected_command_7)

def test_case_14():
    str_0 = 'name'
    bool_0 = True
    var_0 = lambda cmd: bool_0
    str_1 = 'a'
    str_2 = 'b'
    int_0 = 0
    rule_0 = module_0.Rule(str_0, var_0, str_1, bool_0, str_2, int_0, bool_0)
    var_1 = lambda cmd: bool_0
    rule_1 = module_0.Rule(str_0, var_1, str_1, bool_0, str_2, int_0, bool_0)
    var_2 = lambda cmd: bool_0
    rule_2 = module_0.Rule(str_0, var_2, str_1, bool_0, str_2, int_0, bool_0)
    var_3 = lambda cmd: bool_0
    bool_1 = False
    rule_3 = module_0.Rule(str_0, var_3, str_1, bool_0, str_2, int_0, bool_1)
    var_4 = rule_2 == rule_3
    var_5 = lambda cmd: bool_0
    rule_4 = module_0.Rule(str_0, var_5, str_1, bool_0, str_2, bool_1, bool_0)
    var_6 = lambda cmd: bool_0
    bool_2 = False
    rule_5 = module_0.Rule(str_0, var_6, str_1, bool_0, str_2, bool_1, bool_2)
    var_7 = rule_4 == rule_5
    var_8 = lambda cmd: bool_0
    rule_6 = module_0.Rule(str_0, var_8, str_1, bool_0, str_2, bool_2, bool_0)
    var_9 = lambda cmd: bool_0
    rule_7 = module_0.Rule(str_0, var_9, str_1, bool_0, str_2, bool_0, bool_0)
    var_10 = rule_6 == rule_7