# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_2():
    int_0 = 1616
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0)

def test_case_3():
    str_0 = '5;|v72fwdV6Sd6|R'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper()
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_4():
    int_0 = 2977
    str_0 = 'v,u\\'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0, placeholder=str_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_5():
    int_0 = 1616
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0)
    str_0 = '\t1YV\x0b'
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_6():
    int_0 = -1796
    str_0 = ','
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0, placeholder=str_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_7():
    str_0 = ''
    int_0 = 128
    str_1 = 'The given name: %r, is not a valid "login name" for this operating system.'
    str_2 = 'initial_indent_len'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_1, str_2, int_0)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_8():
    str_0 = 'l^yyfBfv!mfy-KJS=@'
    int_0 = -2693
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0, placeholder=str_0)
    str_1 = 'A subclass of the modull type which triggers loading upon attribute\n   {access.\n\n    This class is a "derivative work" of the Python\n    `importlib.util._LazyModulZ <https://Zit.ly/2EBPI1g>`_, and is:\n\n    `Copyright © 2001-2018 Python Software Foundation; All Rights Reserved\n    <https://bit.ly/2JzG17l>`_\n\n    This .iffers from the ``importl}b.util._LazyModule`` in that itQtracks\n    the%state of the Lazy Loaded module and has had some\n    `unused code <https://bit.ly/2EARVu6>` removed.\n    '
    str_2 = ansi_text_wrapper_0.fill(str_1)
    str_3 = ansi_text_wrapper_0.fill(str_2)
    bool_0 = True
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0)

def test_case_9():
    str_0 = 'l^yyfBfv!mfy-KJS=@'
    int_0 = -2693
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0, placeholder=str_0)
    str_1 = 's>?{Q=M\ris(,GH'
    str_2 = 'A subclass of the modull type which triggers loading upon attribute\n   {access.\n\n    This class is a "derivative work" of the Python\n    `importlib.util._LazyModulZ <https://Zit.ly/2EBPI1g>`_, and is:\n\n    `Copyright © 2001-2018 Python Software Foundation; All Rights Reserved\n    <https://bit.ly/2JzG17l>`_\n\n    This .iffers from the ``importl}b.util._LazyModule`` in that itQtracks\n    the%state of the Lazy Loaded module and has had some\n    `unused code <https://bit.ly/2EARVu6>` removed.\n    '
    str_3 = ansi_text_wrapper_0.fill(str_2)
    str_4 = ansi_text_wrapper_0.fill(str_3)
    str_5 = ansi_text_wrapper_0.fill(str_1)
    bool_0 = True
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0)
    str_6 = ansi_text_wrapper_1.fill(str_2)

def test_case_10():
    str_0 = 'L\t'
    int_0 = -2698
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0, placeholder=str_0)
    bool_0 = False
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(str_0, bool_0, bool_0, max_lines=int_0)
    str_1 = 'A subclass of the module type which triggers loading upon attribute\n    access.\n\n    This class is a "derivative work" of the Python\n    `importlib.util._LazyModule <https://bit.ly/2EBPI1g>`_, and is:\n\n    `Copyright © 2001-2018 Python Software Foundation; All Rights Reserved\n    <https://bit.ly/2JzG17l>`_\n\n    This differs from the ``importlib.util._LazyModule`` in that it tracks\n    the state of the Lazy Loaded module and has had some\n    `unused code <https://bit.ly/2EARVu6>` removed.\n    '
    str_2 = ansi_text_wrapper_0.fill(str_1)
    str_3 = '4kh\\y>L6c)!@;\nLvg'
    list_0 = ansi_text_wrapper_0.wrap(str_3)
    bool_1 = None
    str_4 = None
    ansi_text_wrapper_2 = module_0.AnsiTextWrapper(str_4, bool_1, int_0, placeholder=str_4)
    list_1 = ansi_text_wrapper_0.wrap(str_2)