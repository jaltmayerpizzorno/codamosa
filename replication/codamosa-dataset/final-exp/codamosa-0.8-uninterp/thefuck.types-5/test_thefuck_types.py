# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '4A)RWY4y%fFo{'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    command_0 = module_0.Command(dict_0, dict_0)
    var_0 = command_0.update()

def test_case_2():
    str_0 = 'ㅜ'
    dict_0 = {}
    int_0 = 26
    list_0 = [int_0, int_0, int_0, int_0]
    command_0 = module_0.Command(list_0, list_0)
    set_0 = set()
    str_1 = 'kill {}'
    dict_1 = {str_1: list_0, str_1: int_0, str_1: set_0, str_0: set_0}
    corrected_command_0 = module_0.CorrectedCommand(command_0, set_0, dict_1)
    command_1 = module_0.Command(int_0, corrected_command_0)
    var_0 = command_1.update(**dict_0)
    bool_0 = True
    int_1 = -490
    command_2 = module_0.Command(bool_0, int_1)
    var_1 = command_2.__eq__(str_0)

def test_case_3():
    str_0 = "Test for Rule's `test_is_match` method."
    bool_0 = True
    str_1 = 'dummy'
    int_0 = 11
    rule_0 = module_0.Rule(str_0, str_1, str_0, bool_0, str_0, int_0, bool_0)
    command_0 = module_0.Command(str_1, str_1)
    command_1 = module_0.Command(int_0, str_1)
    var_0 = rule_0.is_match(command_1)
    command_2 = module_0.Command(str_1, rule_0)

def test_case_4():
    str_0 = "Test for Rule's `test_is_match` method."
    str_1 = 'Test Rule'
    bool_0 = True
    var_0 = lambda cmd: str_0
    str_2 = 'dummy'
    var_1 = lambda cmd: str_2
    var_2 = None
    int_0 = 0
    rule_0 = module_0.Rule(str_1, var_0, var_1, bool_0, var_2, int_0, bool_0)
    str_3 = '}fzJ\t~cUT^8X*gJ'
    var_3 = rule_0.__eq__(str_3)
    command_0 = module_0.Command(var_2, str_2)
    var_4 = rule_0.is_match(command_0)
    command_1 = module_0.Command(str_2, var_2)
    var_5 = command_1.__repr__()
    var_6 = rule_0.is_match(command_1)

def test_case_5():
    str_0 = "'qw-k\rsRovQ"
    list_0 = [str_0]
    bytes_0 = b'\xdd\xe3v\x0f6\xa6\x15\x88\xd2Z7\xcd\x01\xd7\x88\x95=\x83'
    corrected_command_0 = module_0.CorrectedCommand(str_0, list_0, bytes_0)

def test_case_6():
    str_0 = '@=r8f-6FF'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    bool_0 = True
    list_0 = [dict_0, str_0, str_0]
    corrected_command_0 = module_0.CorrectedCommand(dict_0, bool_0, list_0)
    var_0 = corrected_command_0.__eq__(str_0)

def test_case_7():
    float_0 = 1134.3
    str_0 = '\\npo'
    str_1 = 'xF_?D [te]/o0}J7spW'
    corrected_command_0 = module_0.CorrectedCommand(float_0, str_0, str_1)
    var_0 = corrected_command_0.__hash__()

def test_case_8():
    int_0 = -1987
    str_0 = 'cp -a'
    corrected_command_0 = None
    str_1 = 'Rerun: process PID {} ({}) could not be terminated'
    command_0 = module_0.Command(corrected_command_0, str_1)
    corrected_command_1 = module_0.CorrectedCommand(int_0, str_0, str_0)
    var_0 = corrected_command_1.__repr__()

def test_case_9():
    str_0 = 'Test Rule'
    bool_0 = True
    var_0 = lambda cmd: bool_0
    var_1 = None
    int_0 = 53
    rule_0 = module_0.Rule(str_0, var_0, str_0, bool_0, var_1, int_0, bool_0)
    command_0 = module_0.Command(str_0, str_0)
    var_2 = rule_0.is_match(command_0)
    command_1 = module_0.Command(str_0, var_1)
    var_3 = rule_0.is_match(command_1)

def test_case_10():
    str_0 = 'test1'
    bool_0 = True
    var_0 = lambda x: bool_0
    str_1 = 'test'
    var_1 = lambda x: str_1
    bool_1 = False
    var_2 = None
    rule_0 = module_0.Rule(str_0, var_0, var_1, bool_1, var_2, bool_0, bool_0)
    str_2 = 'test2'
    var_3 = lambda x: bool_1
    var_4 = lambda x: str_1
    int_0 = 2
    rule_1 = module_0.Rule(str_2, var_3, var_4, bool_0, var_2, int_0, bool_0)
    var_5 = rule_0 == rule_1
    var_6 = lambda x: bool_0
    var_7 = lambda x: str_1
    rule_2 = module_0.Rule(str_1, var_6, var_7, bool_1, var_2, bool_0, bool_0)
    var_8 = lambda x: bool_1
    var_9 = lambda x: str_1
    rule_3 = module_0.Rule(str_1, var_8, var_9, bool_0, var_2, int_0, bool_0)
    var_10 = rule_2 == rule_3

def test_case_11():
    float_0 = 830.0
    str_0 = 'i8\x0c~ScE,- !ThI1Vu'
    rule_0 = None
    bytes_0 = b'M\x86\xb9'
    tuple_0 = (str_0, rule_0, bytes_0)
    int_0 = 1489
    list_0 = []
    corrected_command_0 = module_0.CorrectedCommand(int_0, rule_0, list_0)
    tuple_1 = ()
    bool_0 = False
    bytes_1 = b'\xe0|\xac+U7\xe4\xd1\x89'
    dict_0 = {bytes_0: tuple_0, tuple_1: float_0}
    command_0 = module_0.Command(bytes_0, dict_0)
    corrected_command_1 = module_0.CorrectedCommand(bool_0, bytes_1, command_0)
    command_1 = module_0.Command(tuple_1, corrected_command_1)
    set_0 = set()
    tuple_2 = (corrected_command_1, corrected_command_1, set_0)
    str_1 = 'CnKR}gN\\nAcd+_\x0bVLi?\\'
    corrected_command_2 = module_0.CorrectedCommand(command_1, tuple_2, str_1)
    corrected_command_3 = module_0.CorrectedCommand(corrected_command_2, set_0, tuple_0)
    var_0 = corrected_command_3.__eq__(corrected_command_0)
    float_1 = -1810.52
    str_2 = '{'
    str_3 = '^?iB}\x0cX\\ePorX.o&/<Nb'
    list_1 = []
    var_1 = rule_0.__repr__()
    var_2 = rule_0.__eq__(tuple_0)
    dict_1 = {str_2: str_0, str_3: list_1}
    rule_1 = module_0.Rule(float_0, tuple_0, bytes_0, int_0, tuple_0, float_1, dict_1)
    var_3 = rule_1.__repr__()

def test_case_12():
    bytes_0 = b'E\x95\x06\x1e\xdbx.\x90\x9aM\xda/\x01\xc73\xdc'
    str_0 = 'ㅛ'
    str_1 = 'D('
    str_2 = 'home'
    str_3 = ''
    dict_0 = {str_0: str_0, str_1: str_0, str_1: str_2, str_3: bytes_0}
    tuple_0 = (bytes_0, dict_0)
    str_4 = '\r97y6ARrO?\x0c'
    float_0 = 3194.4
    command_0 = module_0.Command(float_0, tuple_0)
    int_0 = -1055
    list_0 = []
    rule_0 = module_0.Rule(tuple_0, tuple_0, str_4, bytes_0, command_0, int_0, list_0)
    bytes_1 = b'\xcc.\xdb\xd2\x0c*2'
    bytes_2 = None
    corrected_command_0 = module_0.CorrectedCommand(rule_0, bytes_1, bytes_2)
    str_5 = 'ㅓ'
    bool_0 = False
    corrected_command_1 = module_0.CorrectedCommand(corrected_command_0, str_5, bool_0)
    complex_0 = None
    bytes_3 = b'~4\x8b~wUh'
    str_6 = 'git push (.*)'
    float_1 = 1937.7031
    command_1 = module_0.Command(str_6, float_1)
    var_0 = command_1.update()
    int_1 = None
    float_2 = None
    command_2 = module_0.Command(int_1, float_2)
    bool_1 = False
    str_7 = 'env: no such command '
    command_3 = module_0.Command(bool_1, str_7)
    var_1 = command_3.__eq__(bytes_3)
    list_1 = [bool_1, complex_0, bool_1, bool_1]
    tuple_1 = ()
    tuple_2 = (list_1, tuple_1, str_7)
    rule_1 = module_0.Rule(command_3, command_3, tuple_2, complex_0, command_3, bytes_3, complex_0)
    float_3 = -2167.547
    command_4 = module_0.Command(tuple_1, float_3)
    var_2 = rule_1.is_match(command_2)
    bytes_4 = b'\xd2\x16\xa8\x95\x88\nJY'
    list_2 = []
    corrected_command_2 = module_0.CorrectedCommand(bytes_3, bytes_4, list_2)
    var_3 = corrected_command_2.__eq__(complex_0)