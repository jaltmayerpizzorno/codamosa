# Automatically generated by Pynguin.
import ansible.cli.console as module_0
import ansible.utils.display as module_1

def test_case_0():
    try:
        bytes_0 = b"\x0b\x9c\x86H\xec\xc2X!\xec\x9bm\xa6\xe8\xdf\xa3\xec'%Z"
        list_0 = [bytes_0]
        console_c_l_i_0 = module_0.ConsoleCLI(list_0)
        var_0 = console_c_l_i_0.run()
        var_1 = console_c_l_i_0.do_shell(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'B$9)L@GH8&k{\x0c`A=&=,'
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        var_0 = console_c_l_i_0.set_prompt()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 2049
        str_0 = 'collection_list'
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        var_0 = console_c_l_i_0.do_shell(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        int_0 = 2813
        console_c_l_i_0 = module_0.ConsoleCLI(int_0)
        var_0 = console_c_l_i_0.do_timeout(bool_0)
        str_0 = ')U526%%7As_n,b!'
        var_1 = console_c_l_i_0.default(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -2835
        console_c_l_i_0 = module_0.ConsoleCLI(int_0)
        var_0 = console_c_l_i_0.list_modules()
        tuple_0 = (console_c_l_i_0,)
        str_0 = 'dmsetup'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        console_c_l_i_1 = module_0.ConsoleCLI(dict_0)
        var_1 = console_c_l_i_1.do_forks(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = ()
        bytes_0 = b'\xb6\xc5D\xee-\x9b7\xf8q\x9cdr\x1e\xd5\x05De'
        float_0 = 2.0
        dict_0 = {tuple_0: tuple_0, float_0: tuple_0}
        console_c_l_i_0 = module_0.ConsoleCLI(dict_0)
        var_0 = console_c_l_i_0.do_cd(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Oc<U<{|'
        str_1 = 'G8=N^,R9B\x0b#}UX'
        list_0 = [str_1, str_1, str_1]
        console_c_l_i_0 = module_0.ConsoleCLI(list_0)
        var_0 = console_c_l_i_0.do_list(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = 2.0
        str_0 = 'X^FHkZfP\x0cZBCp91Tz\r"'
        dict_0 = None
        float_1 = -2327.4
        dict_1 = {float_0: float_0, float_0: str_0, dict_0: float_1}
        console_c_l_i_0 = module_0.ConsoleCLI(dict_1)
        console_c_l_i_1 = module_0.ConsoleCLI(console_c_l_i_0)
        var_0 = console_c_l_i_1.cmdloop()
        console_c_l_i_2 = module_0.ConsoleCLI(float_0)
        set_0 = {console_c_l_i_2}
        var_1 = console_c_l_i_2.do_become(set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'groups'
        str_1 = '}L\x0b3\x0b'
        console_c_l_i_0 = module_0.ConsoleCLI(str_1)
        list_0 = None
        var_0 = console_c_l_i_0.do_remote_user(list_0)
        var_1 = console_c_l_i_0.default(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        tuple_0 = ()
        int_0 = 1019
        console_c_l_i_0 = module_0.ConsoleCLI(int_0)
        var_0 = console_c_l_i_0.cmdloop()
        bytes_0 = b'~\x10\xbb\x03'
        dict_0 = {tuple_0: tuple_0}
        console_c_l_i_1 = module_0.ConsoleCLI(dict_0)
        var_1 = console_c_l_i_1.do_remote_user(bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'\xe4cd\x89p\r\xfbGh&'
        str_0 = '\rT;J`7=G*mp~R[n< W"'
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        var_0 = console_c_l_i_0.do_become_user(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ']Qo)~'
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        int_0 = -1890
        var_0 = console_c_l_i_0.helpdefault(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b"\x0b\x9c\x86H\xec\xc2X!\xec\x9bm\xa6\xe8\xdf\xa3\xec'%Z"
        list_0 = [bytes_0]
        console_c_l_i_0 = module_0.ConsoleCLI(list_0)
        var_0 = console_c_l_i_0.run()
        bool_0 = True
        var_1 = console_c_l_i_0.do_exit(bool_0)
        bytes_1 = b'pUM\xabr\xff\xb6H$\xe5\xa1w\x9b\xc8'
        var_2 = console_c_l_i_0.module_args(bytes_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '}s?9,o~{sgp$Y'
        set_0 = None
        str_1 = ' 9:[UP[:6\to\n'
        list_0 = [set_0]
        console_c_l_i_0 = module_0.ConsoleCLI(list_0)
        console_c_l_i_1 = module_0.ConsoleCLI(str_0)
        var_0 = console_c_l_i_1.module_args(str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = -3468.36
        str_0 = "t'TG9.5=,eTF7 "
        tuple_0 = (str_0,)
        tuple_1 = (tuple_0,)
        console_c_l_i_0 = module_0.ConsoleCLI(tuple_1)
        var_0 = console_c_l_i_0.do_forks(float_0)
        str_1 = ''
        var_1 = console_c_l_i_0.do_cd(str_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'jh$e+T-Ch'
        tuple_0 = (str_0,)
        console_c_l_i_0 = module_0.ConsoleCLI(tuple_0)
        var_0 = console_c_l_i_0.run()
        var_1 = console_c_l_i_0.default(str_0)
        var_2 = console_c_l_i_0.do_cd(str_0)
        bool_0 = True
        console_c_l_i_1 = module_0.ConsoleCLI(bool_0)
        var_3 = console_c_l_i_1.do_forks(bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        dict_0 = {}
        bytes_0 = b'\xfc\x03\xc5\xbb\xcd\xc1\xbe\xed\x00Cw\xc0L\x03\xd6l'
        set_0 = {bytes_0}
        bytes_1 = None
        bool_0 = False
        tuple_0 = (bytes_0, set_0, bytes_1, bool_0)
        console_c_l_i_0 = module_0.ConsoleCLI(tuple_0)
        var_0 = console_c_l_i_0.do_exit(dict_0)
        bool_1 = True
        int_0 = 356
        dict_1 = {bool_1: bool_1, bool_1: bool_1, bool_1: bool_1}
        console_c_l_i_1 = module_0.ConsoleCLI(dict_1)
        var_1 = console_c_l_i_1.do_verbosity(int_0)
        var_2 = console_c_l_i_1.do_cd(tuple_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '9uX>*My:\x0c*\x0cLGdz?#\x0c'
        tuple_0 = (str_0,)
        console_c_l_i_0 = module_0.ConsoleCLI(tuple_0)
        var_0 = console_c_l_i_0.run()
        int_0 = -1829
        console_c_l_i_1 = module_0.ConsoleCLI(int_0)
        str_1 = 'groups'
        bool_0 = False
        var_1 = console_c_l_i_0.do_become(bool_0)
        var_2 = console_c_l_i_0.default(str_1)
        list_0 = []
        bool_1 = True
        console_c_l_i_2 = module_0.ConsoleCLI(bool_1)
        var_3 = console_c_l_i_2.do_remote_user(list_0)
        console_c_l_i_3 = module_0.ConsoleCLI(list_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '`#'
        float_0 = 931.65
        console_c_l_i_0 = module_0.ConsoleCLI(float_0)
        bytes_0 = b''
        var_0 = console_c_l_i_0.do_check(bytes_0)
        var_1 = console_c_l_i_0.cmdloop()
        bytes_1 = b'&\xac\xe2u\xf1D\x17'
        str_1 = '9t^^kdP/GGS&\rFtJahC'
        list_0 = [str_1]
        str_2 = '%s=%s'
        str_3 = '75yvP\t={y`}N~9>'
        console_c_l_i_1 = module_0.ConsoleCLI(str_3)
        var_2 = console_c_l_i_1.complete_cd(bytes_1, str_1, list_0, str_2)
        tuple_0 = (str_0,)
        console_c_l_i_2 = module_0.ConsoleCLI(tuple_0)
        var_3 = console_c_l_i_2.run()
        dict_0 = None
        var_4 = console_c_l_i_2.do_become_user(dict_0)
        var_5 = console_c_l_i_2.default(str_0)
        set_0 = {console_c_l_i_2, var_3, console_c_l_i_2, var_3}
        var_6 = console_c_l_i_2.do_verbosity(set_0)
        set_1 = set()
        var_7 = console_c_l_i_2.do_list(tuple_0)
        var_8 = console_c_l_i_2.do_forks(dict_0)
        var_9 = console_c_l_i_2.do_diff(set_1)
        var_10 = console_c_l_i_2.do_cd(console_c_l_i_2)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'Q'
        bool_0 = False
        set_0 = {str_0, str_0, str_0, str_0}
        console_c_l_i_0 = module_0.ConsoleCLI(set_0)
        var_0 = console_c_l_i_0.do_become_method(bool_0)
        bytes_0 = b''
        bool_1 = True
        console_c_l_i_1 = module_0.ConsoleCLI(bool_1)
        set_1 = {str_0, bool_1, str_0, str_0, bytes_0}
        console_c_l_i_2 = module_0.ConsoleCLI(set_1)
        var_1 = console_c_l_i_2.do_timeout(console_c_l_i_1)
        str_1 = '7#5yvP\t={y`}$~9>'
        console_c_l_i_3 = module_0.ConsoleCLI(str_1)
        tuple_0 = (str_0,)
        var_2 = console_c_l_i_1.get_names()
        console_c_l_i_4 = module_0.ConsoleCLI(tuple_0)
        var_3 = console_c_l_i_4.run()
        var_4 = console_c_l_i_4.default(str_0)
        set_2 = {console_c_l_i_4, var_3, console_c_l_i_4, var_3}
        int_0 = 754
        var_5 = console_c_l_i_1.do_timeout(int_0)
        var_6 = console_c_l_i_4.do_verbosity(set_2)
        set_3 = set()
        var_7 = console_c_l_i_4.helpdefault(bool_1)
        var_8 = console_c_l_i_4.do_list(tuple_0)
        var_9 = console_c_l_i_4.do_diff(set_3)
        var_10 = console_c_l_i_4.do_cd(console_c_l_i_4)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '|'
        bytes_0 = b''
        bool_0 = True
        console_c_l_i_0 = module_0.ConsoleCLI(bool_0)
        set_0 = {str_0, bool_0, str_0, str_0, bytes_0}
        console_c_l_i_1 = module_0.ConsoleCLI(set_0)
        tuple_0 = (str_0,)
        console_c_l_i_2 = module_0.ConsoleCLI(tuple_0)
        var_0 = console_c_l_i_2.run()
        int_0 = -1829
        var_1 = console_c_l_i_2.default(str_0)
        set_1 = {console_c_l_i_2, var_0, console_c_l_i_2, var_0}
        var_2 = console_c_l_i_0.do_timeout(int_0)
        var_3 = console_c_l_i_2.do_verbosity(set_1)
        var_4 = console_c_l_i_2.helpdefault(bool_0)
        var_5 = console_c_l_i_2.do_list(tuple_0)
        var_6 = console_c_l_i_2.do_cd(console_c_l_i_2)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = '#'
        bytes_0 = b'&\xac\xe2u\xf1D\x17'
        str_1 = '9t^^kdP/GGS&\rFtJahC'
        list_0 = [str_1]
        bool_0 = True
        console_c_l_i_0 = module_0.ConsoleCLI(bool_0)
        set_0 = {str_1, str_0, str_0}
        console_c_l_i_1 = module_0.ConsoleCLI(set_0)
        var_0 = console_c_l_i_1.do_timeout(console_c_l_i_0)
        str_2 = '75yvP\t={y`}$~9>'
        console_c_l_i_2 = module_0.ConsoleCLI(str_2)
        var_1 = console_c_l_i_2.complete_cd(bytes_0, str_1, list_0, str_2)
        tuple_0 = (str_0,)
        console_c_l_i_3 = module_0.ConsoleCLI(tuple_0)
        var_2 = console_c_l_i_3.run()
        var_3 = console_c_l_i_3.default(str_0)
        var_4 = console_c_l_i_3.do_verbosity(set_0)
        set_1 = set()
        var_5 = console_c_l_i_3.do_list(tuple_0)
        var_6 = console_c_l_i_3.do_diff(set_1)
        var_7 = console_c_l_i_3.do_cd(console_c_l_i_3)
    except BaseException:
        pass

def test_case_22():
    try:
        bool_0 = True
        str_0 = '7#5yvP\t={y`}$~9>'
        console_c_l_i_0 = module_0.ConsoleCLI(str_0)
        tuple_0 = (str_0,)
        console_c_l_i_1 = module_0.ConsoleCLI(tuple_0)
        var_0 = console_c_l_i_1.run()
        var_1 = console_c_l_i_1.default(str_0)
        set_0 = {console_c_l_i_1, var_0, console_c_l_i_1, var_0}
        var_2 = console_c_l_i_1.do_verbosity(set_0)
        var_3 = console_c_l_i_1.helpdefault(bool_0)
        var_4 = console_c_l_i_1.do_list(tuple_0)
        int_0 = -74
        display_0 = module_1.Display(int_0)
        var_5 = console_c_l_i_0.do_cd(display_0)
    except BaseException:
        pass