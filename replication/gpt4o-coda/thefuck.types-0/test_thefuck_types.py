# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ' Cba'
    command_0 = module_0.Command(str_0, str_0)

def test_case_2():
    bytes_0 = b''
    bool_0 = True
    float_0 = 0.85
    command_0 = module_0.Command(bytes_0, float_0)
    str_0 = '^eoo\\m\\?;y.@a%A4R7 '
    int_0 = -1163
    list_0 = [bytes_0, float_0, int_0, bool_0]
    bytes_1 = b'J0\x1a'
    dict_0 = {str_0: str_0}
    var_0 = command_0.__eq__(float_0)
    rule_0 = module_0.Rule(float_0, int_0, list_0, str_0, bytes_1, dict_0, bool_0)
    var_1 = rule_0.__repr__()
    var_2 = rule_0.is_match(command_0)

def test_case_3():
    bool_0 = True
    set_0 = set()
    int_0 = -512
    tuple_0 = (bool_0, set_0, int_0)
    str_0 = 'Σ'
    command_0 = module_0.Command(tuple_0, str_0)
    var_0 = command_0.__repr__()

def test_case_4():
    str_0 = 'i.L{"H*ya\tApP>6I${*['
    str_1 = 'o?h'
    dict_0 = {str_0: str_0, str_1: str_1, str_0: str_0, str_1: str_1}
    list_0 = [dict_0, dict_0, str_0]
    command_0 = module_0.Command(list_0, list_0)
    var_0 = command_0.update()

def test_case_5():
    list_0 = None
    bool_0 = True
    bytes_0 = b'QA\x07\x1d'
    corrected_command_0 = module_0.CorrectedCommand(bytes_0, list_0, list_0)
    command_0 = module_0.Command(bool_0, corrected_command_0)
    bool_1 = False
    str_0 = '"Y:2&:,]'
    rule_0 = module_0.Rule(list_0, list_0, command_0, bool_1, str_0, str_0, str_0)
    var_0 = rule_0.is_match(command_0)

def test_case_6():
    float_0 = -400.27617
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    list_0 = []
    corrected_command_0 = module_0.CorrectedCommand(float_0, dict_0, list_0)
    bytes_0 = b'S\x18\xe6sC\xb2m0\xe0?jIIaQ<'
    str_0 = '7]~]FN'
    tuple_0 = (str_0,)
    list_1 = [list_0, bytes_0, bytes_0]
    rule_0 = module_0.Rule(corrected_command_0, bytes_0, dict_0, bytes_0, tuple_0, list_1, dict_0)
    var_0 = rule_0.__eq__(str_0)

def test_case_7():
    int_0 = 5
    list_0 = []
    bytes_0 = b"\x83\xe4\xc3\xf2\x9d'lJP\xd0\x92"
    str_0 = 'a'
    corrected_command_0 = module_0.CorrectedCommand(list_0, bytes_0, str_0)
    var_0 = corrected_command_0.__eq__(int_0)

def test_case_8():
    bytes_0 = b''
    dict_0 = {}
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, dict_0, bytes_0]
    corrected_command_0 = module_0.CorrectedCommand(bytes_0, tuple_0, list_0)
    int_0 = 470
    bool_0 = False
    float_0 = 31.1471
    rule_0 = module_0.Rule(dict_0, corrected_command_0, int_0, corrected_command_0, bool_0, dict_0, float_0)
    corrected_command_1 = module_0.CorrectedCommand(bytes_0, bytes_0, rule_0)
    var_0 = corrected_command_1.__hash__()

def test_case_9():
    float_0 = 925.988
    list_0 = None
    command_0 = module_0.Command(float_0, list_0)
    list_1 = []
    bool_0 = True
    bytes_0 = b'QA\x07\x1d'
    corrected_command_0 = module_0.CorrectedCommand(bytes_0, list_1, list_1)
    command_1 = module_0.Command(bool_0, corrected_command_0)
    bool_1 = False
    str_0 = '"Y:2&:,]'
    str_1 = '\tdMm!y\x0bAk}tzge_~G'
    rule_0 = module_0.Rule(list_1, list_1, command_1, bool_1, str_0, str_0, str_1)
    var_0 = rule_0.is_match(command_0)

def test_case_10():
    bool_0 = False
    bytes_0 = b'\xa3\x87\x96\xec\x08\x15\xd6'
    tuple_0 = (bool_0, bytes_0)
    list_0 = [tuple_0, bool_0, bool_0]
    float_0 = 2649.3
    list_1 = [float_0, bytes_0]
    bytes_1 = None
    str_0 = 'A<?#;Y(]_,G^mtG0`xM{'
    rule_0 = module_0.Rule(list_0, list_0, bool_0, list_1, bytes_1, list_0, str_0)
    dict_0 = {}
    str_1 = ''
    str_2 = 'ev!,jkb`08b&'
    dict_1 = {str_2: dict_0}
    str_3 = "error: pathspec '([^']*)' did not match any file\\(s\\) known to git."
    list_2 = [str_2, dict_1]
    int_0 = 3000
    str_4 = '`e\\'
    float_1 = 149.4
    command_0 = module_0.Command(str_4, float_1)
    str_5 = 'fmX=o'
    bytes_2 = b'\xfb\x00'
    rule_1 = module_0.Rule(str_3, list_2, int_0, command_0, str_5, bytes_2, dict_1)
    int_1 = -1772
    list_3 = [str_3, list_2, str_2]
    rule_2 = module_0.Rule(dict_0, str_1, dict_1, rule_1, int_1, command_0, list_3)
    var_0 = rule_2.__eq__(rule_0)

def test_case_11():
    bytes_0 = b'v w4\xc7\xb1\x07\x92+\xa6\xe7\xbd<'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [bytes_0, bytes_0, dict_0]
    tuple_0 = (bytes_0, dict_0, list_0)
    list_1 = [bytes_0, list_0]
    corrected_command_0 = module_0.CorrectedCommand(dict_0, dict_0, list_1)
    bytes_1 = b'\x84\x0b\xc6u-'
    list_2 = [bytes_1]
    float_0 = -1236.7
    str_0 = ')!Xv7QL}Pg:_xp\n2%~'
    int_0 = 1562
    str_1 = '7=>\rRKt"\r\rpE,~HuZ'
    bytes_2 = b'p'
    str_2 = 'can_configure_automatically'
    bool_0 = False
    dict_1 = {str_1: str_1, str_2: str_0, str_0: bool_0, str_2: float_0}
    rule_0 = module_0.Rule(str_1, bytes_1, bytes_2, str_2, bool_0, list_2, dict_1)
    command_0 = module_0.Command(int_0, rule_0)
    rule_1 = module_0.Rule(str_0, dict_0, tuple_0, list_0, command_0, str_1, list_0)
    float_1 = 2146.591
    corrected_command_1 = module_0.CorrectedCommand(list_0, rule_1, float_1)
    corrected_command_2 = module_0.CorrectedCommand(list_2, float_0, corrected_command_1)
    var_0 = corrected_command_2.__eq__(corrected_command_0)
    int_1 = -1639
    str_3 = 'requires_output'
    corrected_command_3 = module_0.CorrectedCommand(dict_0, int_1, str_3)
    command_1 = module_0.Command(tuple_0, corrected_command_3)
    var_1 = command_1.__repr__()