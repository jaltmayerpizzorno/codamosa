# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'this command has to be run under the root user.'
    list_0 = [str_0, str_0, str_0]
    list_1 = [str_0, list_0]
    command_0 = module_0.Command(list_0, list_1)

def test_case_2():
    bytes_0 = b':'
    float_0 = -1289.818
    str_0 = ';yX<|T~z6L'
    command_0 = None
    dict_0 = {str_0: float_0, str_0: command_0}
    float_1 = -262.4
    tuple_0 = (dict_0, float_1)
    command_1 = module_0.Command(float_0, tuple_0)
    var_0 = command_1.__eq__(bytes_0)

def test_case_3():
    float_0 = -2118.345675
    str_0 = ''
    tuple_0 = (str_0, float_0)
    command_0 = module_0.Command(float_0, tuple_0)
    list_0 = [command_0]
    int_0 = -2267
    command_1 = module_0.Command(list_0, int_0)
    var_0 = command_1.__repr__()

def test_case_4():
    str_0 = 'g'
    set_0 = {str_0, str_0}
    str_1 = 'ox'
    list_0 = [str_0, set_0, set_0, set_0]
    int_0 = 4595
    str_2 = '. $profile'
    dict_0 = {str_2: int_0}
    rule_0 = module_0.Rule(str_0, set_0, str_1, set_0, list_0, int_0, dict_0)
    var_0 = rule_0.__repr__()

def test_case_5():
    set_0 = set()
    list_0 = []
    list_1 = []
    str_0 = '82'
    str_1 = "G'pGh8{&H6$7y 5wk"
    dict_0 = {str_0: list_0, str_1: str_1, str_1: list_0}
    bytes_0 = b''
    int_0 = 2996
    command_0 = module_0.Command(bytes_0, int_0)
    var_0 = command_0.__eq__(list_0)
    bool_0 = False
    command_1 = module_0.Command(bool_0, list_0)
    rule_0 = module_0.Rule(list_0, list_1, dict_0, dict_0, str_0, command_1, command_1)
    var_1 = rule_0.__eq__(set_0)

def test_case_6():
    bool_0 = True
    str_0 = 'T$5V#'
    str_1 = '\x0c\n=i~",='
    dict_0 = {str_0: str_0, str_0: bool_0, str_1: bool_0, str_1: str_0}
    command_0 = module_0.Command(bool_0, dict_0)
    list_0 = []
    dict_1 = {}
    rule_0 = module_0.Rule(command_0, bool_0, dict_0, list_0, list_0, bool_0, dict_1)
    bool_1 = False
    tuple_0 = (bool_1,)
    bytes_0 = b'M\x18\xc2'
    int_0 = -3183
    str_2 = None
    str_3 = None
    dict_2 = {str_2: bool_1, str_2: str_2, str_3: bytes_0}
    command_1 = module_0.Command(int_0, dict_2)
    float_0 = 1168.8
    command_2 = module_0.Command(float_0, tuple_0)
    corrected_command_0 = module_0.CorrectedCommand(command_1, command_2, bytes_0)
    corrected_command_1 = module_0.CorrectedCommand(tuple_0, bytes_0, corrected_command_0)
    str_4 = 'H`^h\tA^'
    str_5 = 'gj,%86Ecib<|3lNc8'
    str_6 = None
    dict_3 = {str_6: command_2}
    list_1 = [dict_3]
    float_1 = -676.0
    rule_1 = module_0.Rule(corrected_command_1, bytes_0, str_4, str_5, bytes_0, list_1, float_1)
    var_0 = rule_1.__eq__(rule_0)
    float_2 = 160.46
    str_7 = 'YMS=6+*x'
    float_3 = 1181.0
    corrected_command_2 = module_0.CorrectedCommand(float_2, str_7, float_3)
    var_1 = corrected_command_2.__repr__()
    var_2 = corrected_command_2.__hash__()
    str_8 = 't0C,5'
    var_3 = corrected_command_2.__eq__(str_8)
    var_4 = corrected_command_2.__repr__()
    var_5 = corrected_command_2.__hash__()

def test_case_7():
    float_0 = 0.85
    str_0 = '\\QWHCP'
    command_0 = module_0.Command(float_0, str_0)
    str_1 = 'mZ|#08S-h~upN577D}\t'
    tuple_0 = ()
    str_2 = 'z)v?(7'
    set_0 = set()
    dict_0 = {str_1: command_0}
    rule_0 = module_0.Rule(command_0, str_0, tuple_0, str_2, set_0, dict_0, float_0)
    var_0 = rule_0.is_match(command_0)

def test_case_8():
    str_0 = 'RH\\mr1nyW@*!P$+Q'
    complex_0 = None
    dict_0 = {complex_0: complex_0, complex_0: str_0, str_0: complex_0}
    corrected_command_0 = module_0.CorrectedCommand(str_0, complex_0, dict_0)
    bytes_0 = None
    tuple_0 = (bytes_0,)
    command_0 = module_0.Command(corrected_command_0, tuple_0)

def test_case_9():
    bytes_0 = None
    tuple_0 = None
    dict_0 = {tuple_0: tuple_0}
    float_0 = -208.0
    bool_0 = False
    corrected_command_0 = module_0.CorrectedCommand(float_0, tuple_0, bool_0)
    corrected_command_1 = module_0.CorrectedCommand(dict_0, corrected_command_0, tuple_0)
    var_0 = corrected_command_1.__eq__(bytes_0)

def test_case_10():
    dict_0 = {}
    command_0 = None
    bool_0 = False
    str_0 = 'JE&[:{Q$\x0b>\td*p>'
    str_1 = "e}A\n`O'"
    dict_1 = {str_0: bool_0, str_1: str_0}
    str_2 = "Z|rHwBKgI'\t"
    list_0 = []
    tuple_0 = (bool_0, dict_1, str_2, list_0)
    int_0 = None
    list_1 = [bool_0, tuple_0]
    corrected_command_0 = module_0.CorrectedCommand(tuple_0, int_0, list_1)
    set_0 = set()
    bytes_0 = b''
    float_0 = None
    corrected_command_1 = module_0.CorrectedCommand(bytes_0, float_0, list_1)
    str_3 = '>7LSnFn## #LA1[/98{t'
    bytes_1 = b'\xa7\xed,>1\xcbd\xfa'
    rule_0 = None
    bytes_2 = b'`\xe0\xde\x83N*'
    bytes_3 = b'\xdcj\xb3\xc1\xc9\x19\xaf\xbf\x1bz?\xb9\x88\xbc\n\xbe\xb4\x13\x7fG'
    rule_1 = module_0.Rule(rule_0, tuple_0, command_0, dict_1, bytes_2, dict_0, bytes_3)
    rule_2 = module_0.Rule(str_3, set_0, corrected_command_1, bytes_1, bytes_0, rule_1, dict_1)
    rule_3 = module_0.Rule(command_0, corrected_command_0, set_0, dict_0, corrected_command_1, rule_2, bytes_3)
    str_4 = 'cmW#Pp"CtrVo?::T`496'
    dict_2 = {str_4: dict_0, str_4: str_4}
    command_1 = module_0.Command(dict_0, dict_2)
    command_2 = module_0.Command(command_1, dict_0)
    str_5 = '.rb'
    list_2 = [str_5, str_5, str_5, str_5]
    var_0 = command_2.update()
    command_3 = module_0.Command(str_5, list_2)
    list_3 = None
    bytes_4 = b'5\x9e<\x98\x06\x96\x9a\x02\x9e\xc7&\x87\xe3\xbbb\xebzcd\x81'
    corrected_command_2 = module_0.CorrectedCommand(list_3, bytes_4, str_4)
    bool_1 = True
    corrected_command_3 = module_0.CorrectedCommand(corrected_command_2, bool_1, bool_1)
    str_6 = 'w;EQ4\x0b'
    bytes_5 = b'\xd8q\xf4\x06\x96\xa4l\xe0\xd1'
    list_4 = [list_2, command_3, dict_0, command_1]
    corrected_command_4 = module_0.CorrectedCommand(str_6, bytes_5, list_4)
    var_1 = corrected_command_4.__eq__(corrected_command_3)
    var_2 = command_3.update()

def test_case_11():
    str_0 = 'RH\\mr1nyW@*!P$+Q'
    complex_0 = None
    dict_0 = {complex_0: complex_0, complex_0: str_0, str_0: complex_0}
    corrected_command_0 = module_0.CorrectedCommand(str_0, complex_0, dict_0)
    int_0 = 60
    set_0 = {complex_0, corrected_command_0, int_0}
    var_0 = corrected_command_0.run(set_0)

def test_case_12():
    bytes_0 = b''
    int_0 = -2861
    float_0 = 1034.0
    command_0 = module_0.Command(int_0, float_0)
    bool_0 = True
    str_0 = ']>ESM~dm.?&U'
    str_1 = 'V\\:_\tn'
    list_0 = [int_0, int_0]
    list_1 = [list_0]
    dict_0 = {str_0: bytes_0, str_1: list_1}
    str_2 = ''
    rule_0 = module_0.Rule(bool_0, bool_0, bool_0, dict_0, dict_0, str_0, str_2)
    command_1 = module_0.Command(command_0, rule_0)
    list_2 = [bytes_0, bytes_0, bytes_0, bytes_0]
    bool_1 = False
    tuple_0 = (bytes_0, list_2, bool_1)
    bool_2 = True
    list_3 = [tuple_0]
    dict_1 = {int_0: bool_2, bool_1: float_0, bytes_0: rule_0}
    dict_2 = {str_1: bytes_0}
    bytes_1 = b''
    corrected_command_0 = module_0.CorrectedCommand(dict_1, dict_2, bytes_1)
    corrected_command_1 = module_0.CorrectedCommand(tuple_0, bool_2, list_3)
    var_0 = corrected_command_1.__repr__()

def test_case_13():
    str_0 = None
    command_0 = module_0.Command(str_0, str_0)
    float_0 = 0.85
    tuple_0 = ()
    str_1 = 'z)v?(7'
    set_0 = set()
    dict_0 = {str_1: command_0}
    rule_0 = module_0.Rule(command_0, str_1, tuple_0, str_1, set_0, dict_0, float_0)
    var_0 = rule_0.is_match(command_0)
    str_2 = 'excluded_search_path_prefixes'
    str_3 = 't'
    int_0 = 600
    corrected_command_0 = module_0.CorrectedCommand(str_2, int_0, str_3)