# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    try:
        str_0 = 'Z\rq\x0bBm\t\x0ceNuHdin'
        int_0 = -2241
        dict_0 = {int_0: int_0, int_0: str_0, int_0: str_0}
        validation_0 = module_0.Validation(int_0, dict_0)
        var_0 = validation_0.to_maybe()
        bool_0 = True
        validation_1 = module_0.Validation(str_0, bool_0)
        str_1 = 'D\r:5;,Hd]H1v.)sPl,'
        var_1 = validation_1.map(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n        :param semigroup: other semigroup to concat\n        :type semigroup: Min[B]\n        :returns: new Min with smallest value\n        :rtype: Min[A | B]\n        '
        list_0 = [str_0, str_0, str_0, str_0]
        int_0 = -1368
        list_1 = [int_0]
        validation_0 = module_0.Validation(list_1, list_1)
        var_0 = validation_0.bind(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = True
        bool_0 = True
        list_0 = [bool_0]
        validation_0 = module_0.Validation(bool_0, list_0)
        var_0 = validation_0.to_box()
        bool_1 = True
        tuple_0 = (bool_1,)
        str_0 = 'M|k'
        validation_1 = module_0.Validation(tuple_0, str_0)
        var_1 = validation_1.ap(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = None
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        float_0 = 141.5
        validation_0 = module_0.Validation(list_0, float_0)
        var_0 = validation_0.to_either()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n        Transform Box into Lazy with returning value function.\n\n        :returns: not folded Lazy monad with function returning previous value\n        :rtype: Lazy[Function(() -> A)]\n        '
        str_1 = '\n        :param constructor_fn: function to call during fold method call\n        :type constructor_fn: Function() -> A\n        '
        validation_0 = module_0.Validation(str_0, str_1)
        var_0 = validation_0.is_success()
        var_1 = validation_0.is_success()
        var_2 = validation_0.__str__()
        dict_0 = {}
        str_2 = "n_;f'Ln<[ZpCq+q$^u X"
        var_3 = validation_0.to_maybe()
        validation_1 = module_0.Validation(str_2, dict_0)
        var_4 = validation_1.to_lazy()
        var_5 = validation_1.to_lazy()
        bool_0 = False
        var_6 = validation_0.to_either()
        var_7 = validation_1.to_maybe()
        validation_2 = module_0.Validation(dict_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -304
        set_0 = {int_0, int_0, int_0, int_0}
        float_0 = 218.0
        validation_0 = module_0.Validation(set_0, float_0)
        validation_1 = module_0.Validation(validation_0, validation_0)
        var_0 = validation_0.to_try()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b''
        tuple_0 = ()
        bytes_1 = b'\x0cL\x1aa\xd4\xe7^+<?\xa8\xaf\xa3"\x96\xaej\xdc\xb5'
        validation_0 = module_0.Validation(tuple_0, bytes_1)
        set_0 = set()
        float_0 = 883.2874
        var_0 = validation_0.is_fail()
        var_1 = validation_0.to_try()
        validation_1 = module_0.Validation(set_0, float_0)
        var_2 = validation_1.__eq__(validation_0)
        var_3 = validation_0.to_box()
        var_4 = validation_0.to_either()
        str_0 = 'W2 tmHGjwCe<N`\r:Ca6'
        validation_2 = module_0.Validation(str_0, bytes_0)
        var_5 = validation_2.is_success()
        bool_0 = True
        validation_3 = module_0.Validation(bool_0, bool_0)
        var_6 = validation_3.is_success()
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b''
        tuple_0 = ()
        bytes_1 = b'\x0cL\x1aa\xd4\xe7^+<?\xa8\xaf\xa3"\x96\xaej\xdc\xb5'
        validation_0 = module_0.Validation(tuple_0, bytes_1)
        set_0 = set()
        float_0 = 883.2874
        var_0 = validation_0.is_fail()
        var_1 = validation_0.to_try()
        validation_1 = module_0.Validation(set_0, float_0)
        var_2 = validation_1.__eq__(tuple_0)
        var_3 = validation_1.to_box()
        var_4 = validation_0.to_box()
        var_5 = validation_0.to_either()
        str_0 = 'W2 tmHGjwCe<N`\r:Ca6'
        validation_2 = module_0.Validation(str_0, bytes_0)
        var_6 = validation_0.to_maybe()
        var_7 = validation_0.__eq__(float_0)
        var_8 = validation_0.to_box()
        var_9 = validation_2.to_either()
        str_1 = 'W2 tmHGjwCe<N`\r:Ca6'
        bytes_2 = b'\xceI\xa4\xc9\x8a\x10\x86M\x8c\xf8\x8e\xd4VD\xe4\xe0\t\x19\xe5'
        validation_3 = module_0.Validation(bytes_2, tuple_0)
        var_10 = validation_2.is_success()
        validation_4 = module_0.Validation(tuple_0, validation_0)
        float_1 = -167.00605
        validation_5 = module_0.Validation(float_1, str_1)
        var_11 = validation_5.is_success()
        var_12 = validation_4.map(str_0)
    except BaseException:
        pass