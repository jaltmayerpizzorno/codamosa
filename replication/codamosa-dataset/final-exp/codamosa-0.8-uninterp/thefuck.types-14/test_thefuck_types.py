# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xccn\xf4\x81\xa0\x96)'
    list_0 = None
    int_0 = -2006
    tuple_0 = (list_0, int_0)
    command_0 = module_0.Command(bytes_0, tuple_0)
    var_0 = command_0.update()

def test_case_2():
    set_0 = set()
    bytes_0 = b"'\x11c,s,\xf5\xec\x87*\x9e X\xc5\xd5\xb5\xdb\x92\x17"
    tuple_0 = (set_0, set_0, bytes_0)
    int_0 = 1964
    command_0 = module_0.Command(tuple_0, int_0)
    var_0 = command_0.__repr__()

def test_case_3():
    str_0 = 'test_rule'
    bool_0 = False
    var_0 = lambda _: bool_0
    bool_1 = True
    var_1 = None
    rule_0 = module_0.Rule(str_0, var_0, str_0, bool_1, var_1, bool_0, bool_1)
    command_0 = module_0.Command(str_0, str_0)
    var_2 = rule_0.is_match(command_0)

def test_case_4():
    str_0 = 'Ό'
    str_1 = 'd;8;'
    bytes_0 = b'd\x95i'
    float_0 = -3594.6484
    list_0 = [str_1]
    corrected_command_0 = module_0.CorrectedCommand(bytes_0, float_0, list_0)
    bool_0 = False
    float_1 = 289.4
    int_0 = 4
    list_1 = [float_0]
    rule_0 = module_0.Rule(str_1, corrected_command_0, str_0, bool_0, float_1, int_0, list_1)
    var_0 = rule_0.__eq__(str_0)

def test_case_5():
    bytes_0 = b'\xfd'
    tuple_0 = ()
    bool_0 = False
    str_0 = '/#x}Y`]9?t'
    dict_0 = {bool_0: bytes_0, tuple_0: bool_0}
    float_0 = 1187.0
    command_0 = module_0.Command(dict_0, float_0)
    int_0 = -387
    str_1 = 'brew'
    float_1 = -2098.122
    dict_1 = {}
    int_1 = 1024
    rule_0 = module_0.Rule(str_0, command_0, int_0, str_1, float_1, dict_1, int_1)
    corrected_command_0 = module_0.CorrectedCommand(tuple_0, bool_0, rule_0)
    command_1 = module_0.Command(bytes_0, corrected_command_0)
    var_0 = command_1.__repr__()

def test_case_6():
    corrected_command_0 = None
    float_0 = 2861.443
    set_0 = None
    corrected_command_1 = module_0.CorrectedCommand(corrected_command_0, float_0, set_0)

def test_case_7():
    int_0 = 900
    bytes_0 = b'\x83\xd5R;'
    int_1 = -1306
    list_0 = [bytes_0, int_1, bytes_0]
    str_0 = 'Lists used for decomposing korean letters.'
    corrected_command_0 = module_0.CorrectedCommand(bytes_0, list_0, str_0)
    var_0 = corrected_command_0.__eq__(int_0)

def test_case_8():
    complex_0 = None
    str_0 = 'PowerShell'
    corrected_command_0 = module_0.CorrectedCommand(str_0, complex_0, str_0)
    var_0 = corrected_command_0.run(str_0)

def test_case_9():
    str_0 = '1'
    var_0 = None
    int_0 = 0
    corrected_command_0 = module_0.CorrectedCommand(str_0, var_0, int_0)
    int_1 = 1
    corrected_command_1 = module_0.CorrectedCommand(str_0, var_0, int_1)
    var_1 = corrected_command_0 == corrected_command_1
    corrected_command_2 = module_0.CorrectedCommand(str_0, var_0, int_0)
    corrected_command_3 = module_0.CorrectedCommand(str_0, var_0, int_1)
    var_2 = corrected_command_2 == corrected_command_3
    corrected_command_4 = module_0.CorrectedCommand(str_0, var_0, int_1)
    corrected_command_5 = module_0.CorrectedCommand(str_0, var_0, int_1)
    var_3 = corrected_command_4 == corrected_command_5
    corrected_command_6 = module_0.CorrectedCommand(str_0, var_0, int_1)
    str_1 = '2'
    corrected_command_7 = module_0.CorrectedCommand(str_1, var_0, int_1)
    var_4 = corrected_command_6 == corrected_command_7
    corrected_command_8 = module_0.CorrectedCommand(str_1, var_0, int_1)
    corrected_command_9 = module_0.CorrectedCommand(str_1, var_0, int_1)
    var_5 = corrected_command_8 == corrected_command_9
    corrected_command_10 = module_0.CorrectedCommand(str_1, var_0, int_1)
    corrected_command_11 = module_0.CorrectedCommand(str_0, var_0, int_1)
    corrected_command_12 = module_0.CorrectedCommand(str_0, var_0, int_1)
    int_2 = 2
    corrected_command_13 = module_0.CorrectedCommand(str_1, var_0, int_2)
    var_6 = corrected_command_12 == corrected_command_13
    corrected_command_14 = module_0.CorrectedCommand(str_1, var_0, int_1)
    corrected_command_15 = module_0.CorrectedCommand(str_1, var_0, int_2)
    var_7 = corrected_command_14 == corrected_command_15
    corrected_command_16 = module_0.CorrectedCommand(str_1, var_0, int_2)

def test_case_10():
    str_0 = 'test'
    bool_0 = True
    var_0 = lambda c: bool_0
    str_1 = ''
    var_1 = lambda c: str_1
    var_2 = None
    var_3 = lambda c, s: var_2
    int_0 = 0
    rule_0 = module_0.Rule(str_0, var_0, var_1, bool_0, var_3, int_0, bool_0)
    var_4 = lambda c: bool_0
    var_5 = lambda c: str_1
    var_6 = lambda c, s: var_2
    var_7 = lambda c: bool_0
    var_8 = lambda c: str_1
    var_9 = lambda c, s: var_2
    rule_1 = module_0.Rule(str_0, var_7, var_8, bool_0, var_9, int_0, bool_0)
    var_10 = lambda c: bool_0
    var_11 = lambda c: str_1
    var_12 = lambda c, s: var_2
    rule_2 = module_0.Rule(str_1, var_10, var_11, bool_0, var_12, int_0, bool_0)
    var_13 = rule_1 == rule_2
    var_14 = lambda c: bool_0
    var_15 = lambda c: str_1
    var_16 = lambda c, s: var_2
    rule_3 = module_0.Rule(str_0, var_14, var_15, bool_0, var_16, int_0, bool_0)
    bool_1 = False
    var_17 = lambda c: bool_1
    var_18 = lambda c: str_1
    var_19 = lambda c, s: var_2
    rule_4 = module_0.Rule(str_0, var_17, var_18, bool_0, var_19, bool_1, bool_0)
    var_20 = rule_3 == rule_4

def test_case_11():
    str_0 = 'test_rule'
    bool_0 = False
    var_0 = lambda _: bool_0
    str_1 = 'ls'
    var_1 = lambda _: var_0
    bool_1 = True
    var_2 = None
    rule_0 = module_0.Rule(str_0, var_0, var_1, bool_1, var_2, bool_0, bool_1)
    command_0 = module_0.Command(str_1, var_2)
    var_3 = rule_0.is_match(command_0)
    command_1 = module_0.Command(str_0, str_1)
    var_4 = rule_0.is_match(command_1)

def test_case_12():
    bool_0 = False
    var_0 = lambda _: bool_0
    str_0 = 'ls'
    var_1 = lambda _: bool_0
    bool_1 = False
    var_2 = None
    rule_0 = module_0.Rule(str_0, var_0, var_1, bool_1, var_2, bool_0, bool_1)
    command_0 = module_0.Command(str_0, str_0)
    var_3 = rule_0.is_match(command_0)
    command_1 = module_0.Command(str_0, var_2)
    var_4 = rule_0.is_match(command_1)
    var_5 = rule_0.is_match(command_1)