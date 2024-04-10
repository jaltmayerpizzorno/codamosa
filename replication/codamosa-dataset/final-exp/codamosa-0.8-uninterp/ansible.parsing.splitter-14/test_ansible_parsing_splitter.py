# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'z5}_qkNN\x0csE\n|%l'
    var_0 = module_0.parse_kv(str_0)

def test_case_2():
    str_0 = 'creates=/tmp/foo removes=/tmp/bar chdir=/tmp/baz executable=/bin/bash warn=yes stdin=hello stdin_add_newline=yes strip_empty_ends=yes'
    var_0 = module_0.parse_kv(str_0)

def test_case_3():
    str_0 = 'z5}_!qkNN\x0c?E\n=%l'
    var_0 = module_0.parse_kv(str_0)

def test_case_4():
    str_0 = 'k1=v1 k2==v2 $3="v3" k4="v 4" "k5=v5"'
    var_0 = module_0.parse_kv(str_0)

def test_case_5():
    str_0 = '& %s; exit $LASTEXITCODE'
    var_0 = module_0.parse_kv(str_0)

def test_case_6():
    str_0 = 'k1=v1 k2=v2'
    var_0 = module_0.parse_kv(str_0)
    tuple_0 = None
    var_1 = module_0.parse_kv(tuple_0)
    str_1 = 'k1=v1 k2=v2 k3'
    bool_0 = True
    var_2 = module_0.parse_kv(str_1, bool_0)
    var_3 = module_0.parse_kv(str_1)
    var_4 = module_0.parse_kv(tuple_0)

def test_case_7():
    str_0 = 'Remove strings in ``no_log_strings`` from value.\n\n    If value is a container type, then remove a lot more.\n\n    Use of ``deferred_removals`` exists, rather than a pure recursive solution,\n    because of the potential to hit the maximum recursion depth when dealing with\n    large amounts of data (see `issue #24560 <https://github.com/ansible/ansible/issues/24560>`_).\n    '
    var_0 = module_0.parse_kv(str_0)

def test_case_8():
    str_0 = 'k1=v1 k2=v2'
    var_0 = module_0.parse_kv(str_0)
    str_1 = 'k1=v1 k2=v2 k3'
    bool_0 = True
    var_1 = module_0.parse_kv(str_1, bool_0)
    str_2 = 'k1=\\"v1\\" k2=\\\'v2\\\''
    var_2 = module_0.parse_kv(str_2)

def test_case_9():
    str_0 = 'a=b c=d'
    var_0 = module_0.parse_kv(str_0)
    var_1 = module_0.parse_kv(str_0)
    var_2 = module_0.parse_kv(str_0, str_0)

def test_case_10():
    str_0 = 'arg1="foo bar"'
    var_0 = module_0.split_args(str_0)
    str_1 = 'arg1="foo\nbar"'
    var_1 = module_0.split_args(str_1)

def test_case_11():
    str_0 = 'echo "this is a test" {{ foo }} {% bar %} {# baz #}'
    var_0 = module_0.split_args(str_0)

def test_case_12():
    str_0 = 'creates=/tmp/foo removes=/tmp/bar warn=no executable=/some/path creates=/another/path'
    bool_0 = True
    var_0 = module_0.parse_kv(str_0, bool_0)
    str_1 = 'some space separated parameters'
    var_1 = module_0.parse_kv(str_1, bool_0)

def test_case_13():
    var_0 = None
    var_1 = module_0.parse_kv(var_0)
    str_0 = 'dominion'
    var_2 = module_0.parse_kv(str_0)
    str_1 = 'ab'
    var_3 = module_0.parse_kv(str_1)
    str_2 = "a=b c='d e'"
    var_4 = module_0.parse_kv(str_2)
    str_3 = 'a\\=b c\\=d'
    var_5 = module_0.parse_kv(str_3)
    str_4 = 'a\\=b=c\\=d'
    var_6 = module_0.parse_kv(str_4)