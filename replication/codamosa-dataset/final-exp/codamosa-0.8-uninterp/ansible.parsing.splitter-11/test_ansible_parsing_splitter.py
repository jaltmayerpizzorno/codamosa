# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xa7\xb5V\xbd\xbal\x10\x9b'
    var_0 = module_0.parse_kv(bytes_0)

def test_case_2():
    str_0 = 'foo=\'bar baz\' baz="bar\'d" name=value "raw string" "other raw string"'
    var_0 = module_0.parse_kv(str_0)

def test_case_3():
    str_0 = 'foo=\'bar baz\' baz="bar\'d" name=value "raw string" "other raw string"'
    bool_0 = True
    var_0 = module_0.parse_kv(str_0, bool_0)

def test_case_4():
    bool_0 = None
    var_0 = module_0.parse_kv(bool_0)

def test_case_5():
    str_0 = '[/r/D[I ij(Wd@X;Va6'
    var_0 = module_0.split_args(str_0)

def test_case_6():
    str_0 = 'Dq-2D2cW3o>IXh{Gl,>'
    var_0 = module_0.join_args(str_0)

def test_case_7():
    str_0 = ''
    var_0 = module_0.split_args(str_0)
    str_1 = ' a=b'
    var_1 = module_0.split_args(str_1)
    str_2 = ' a=b c=d'
    var_2 = module_0.split_args(str_2)
    str_3 = ' a=b c=d '
    var_3 = module_0.split_args(str_3)
    str_4 = ' "a=b c=d"'
    var_4 = module_0.split_args(str_4)
    str_5 = ' a=b\\ c=d'
    var_5 = module_0.split_args(str_5)
    str_6 = ' a=b\\\nc=d'
    var_6 = module_0.split_args(str_6)

def test_case_8():
    str_0 = 'foo=bar baz="qux quux" baz2=\\"qux quux\\"'
    var_0 = module_0.parse_kv(str_0)
    var_1 = len(var_0)
    bool_0 = True
    var_2 = module_0.parse_kv(str_0, bool_0)
    var_3 = len(var_2)

def test_case_9():
    str_0 = 'a b="foo bar"'
    var_0 = module_0.split_args(str_0)
    str_1 = "a=b c='foo bar'"
    var_1 = module_0.split_args(str_1)
    str_2 = 'a="foo bar" b="foo baz" c={{ foo }} d={{ bar }} e={{ baz }}'
    var_2 = module_0.split_args(str_2)

def test_case_10():
    str_0 = '=q'
    var_0 = module_0.parse_kv(str_0)

def test_case_11():
    str_0 = 'a=b c="foo bar" \'d e\' f="{{x}}" g={{y}} \'h i\' {% j %} k={{ z }}'
    var_0 = module_0.split_args(str_0)

def test_case_12():
    var_0 = None
    var_1 = module_0.parse_kv(var_0)
    str_0 = 'a=b c=d'
    var_2 = module_0.parse_kv(str_0)
    str_1 = 'a=b c = d'
    var_3 = module_0.parse_kv(str_1)
    str_2 = 'c= d=e'
    var_4 = module_0.parse_kv(str_2)
    str_3 = '8P3\\=2\t9OQtSc_'
    str_4 = '1pT&]ec~[9\n/{^%ok'
    var_5 = module_0.parse_kv(str_3, str_4)
    var_6 = module_0.parse_kv(str_3)