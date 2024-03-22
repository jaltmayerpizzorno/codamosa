# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '%(v|l"wJ@!;A"Kc>$p'
    var_0 = module_0.parse_kv(str_0)

def test_case_2():
    tuple_0 = None
    var_0 = module_0.parse_kv(tuple_0)

def test_case_3():
    str_0 = ' N9b=J(I'
    var_0 = module_0.split_args(str_0)

def test_case_4():
    set_0 = set()
    var_0 = module_0.join_args(set_0)

def test_case_5():
    str_0 = 'creates=/tmp/foo creates=/tmp/bar arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 arg10 arg11 arg12 arg13 arg14 arg15 arg16 arg17'
    var_0 = module_0.parse_kv(str_0)

def test_case_6():
    str_0 = 'a=1'
    var_0 = module_0.parse_kv(str_0)

def test_case_7():
    str_0 = 'create=true time="2013-09-18 11:29:31" state=present'
    str_1 = 'C|sq\tss\n^?P[+x$j'
    var_0 = module_0.parse_kv(str_1)
    str_2 = 'foo='
    var_1 = module_0.parse_kv(str_2)
    var_2 = module_0.parse_kv(str_0, str_0)
    list_0 = [str_0]
    var_3 = module_0.join_args(list_0)

def test_case_8():
    str_0 = ' N9b=J(I'
    bytes_0 = b'\xa9N\r\x8c8\x0e\xa6\x9c\xe5Z\xfb*'
    var_0 = module_0.parse_kv(str_0, bytes_0)
    var_1 = module_0.split_args(str_0)

def test_case_9():
    str_0 = 'a=b c="foo bar" \nd="foo bar" e=\'foo bar\' f={{ bar }} g=foo{% bar %}h=foo{# bar #}i=foo\nj=baz'
    var_0 = module_0.split_args(str_0)

def test_case_10():
    str_0 = ''
    var_0 = module_0.parse_kv(str_0)
    str_1 = "foo='bar'"
    var_1 = module_0.parse_kv(str_1)
    str_2 = 'foo="bar"'
    var_2 = module_0.parse_kv(str_2)
    str_3 = 'foo="bar \'bar\'"'
    var_3 = module_0.parse_kv(str_3)

def test_case_11():
    str_0 = ''
    var_0 = module_0.parse_kv(str_0)
    var_1 = module_0.parse_kv(str_0)
    str_1 = "foo='bar'"
    var_2 = module_0.parse_kv(str_1)
    str_2 = 'foo="bar"'
    var_3 = module_0.parse_kv(str_2)
    str_3 = 'foo="bar bar"'
    var_4 = module_0.parse_kv(str_3)
    str_4 = 'foo="bar \'bar\'"'
    var_5 = module_0.parse_kv(str_4)
    str_5 = 'foo="bar \\"bar\\""'
    var_6 = module_0.parse_kv(str_5)

def test_case_12():
    str_0 = 'create=true time="2013-09-18 11:29:31" state=present'
    var_0 = module_0.parse_kv(str_0, str_0)
    list_0 = [str_0]
    var_1 = module_0.join_args(list_0)

def test_case_13():
    str_0 = ' "a=b c=d"\nfoo="bar baz"'
    var_0 = module_0.split_args(str_0)
    str_1 = 'a\\="b"'
    var_1 = module_0.split_args(str_1)
    str_2 = 'a\\\\"'
    var_2 = module_0.split_args(str_2)
    str_3 = 'a\\=b'
    var_3 = module_0.split_args(str_3)
    str_4 = 'a\\\\=b'
    var_4 = module_0.split_args(str_4)

def test_case_14():
    str_0 = ''
    var_0 = print(str_0)
    str_1 = '"double quoted" \'single quoted\' unquoted'
    var_1 = module_0.split_args(str_1)
    bytes_0 = b'\x96\x1b\xc6\x14[\xef\xa8\x16^{\xa6\xac\xe53BX'
    var_2 = module_0.parse_kv(bytes_0)
    str_2 = '=P#'
    var_3 = module_0.parse_kv(str_2)

def test_case_15():
    str_0 = 'one two=three four="five six" seven=eight nine'
    var_0 = module_0.parse_kv(str_0)
    str_1 = 'creates=/tmp/a file=/tmp/b'
    var_1 = module_0.parse_kv(str_1)
    bool_0 = True
    var_2 = module_0.parse_kv(str_1, bool_0)