# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper()

def test_case_1():
    str_0 = 'exists_as'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_2():
    str_0 = 'GIrJ&;'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper()
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_3():
    str_0 = 'b3#[?l~6 E2)L\nMIW`'
    int_0 = 50987760
    str_1 = 'm'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_1)
    list_0 = ansi_text_wrapper_0.wrap(str_0)

def test_case_4():
    str_0 = "\x0clj83'L^&|1Q-s-[p"
    str_1 = 'vgq?b+z2l\\#>ZEz%2K"'
    int_0 = 36
    bool_0 = None
    int_1 = -2633
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, bool_0, bool_0, int_1, max_lines=int_1)
    str_2 = '__]chery_pick_map__'
    str_3 = ansi_text_wrapper_0.fill(str_1)
    list_0 = ansi_text_wrapper_0.wrap(str_2)
    list_1 = ansi_text_wrapper_0.wrap(str_3)
    list_2 = ansi_text_wrapper_0.wrap(str_3)

def test_case_5():
    int_0 = 50987760
    str_0 = 'm'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_0)
    str_1 = 'z `s}|&L7g[xd1?dF '
    list_0 = ansi_text_wrapper_0.wrap(str_1)

def test_case_6():
    str_0 = "\x0clj83'L^&|1Q-s-[p"
    int_0 = 36
    bool_0 = None
    int_1 = -2633
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, bool_0, bool_0, int_1, max_lines=int_1)
    str_1 = "!Vt>_''}M^mLh\x0bK$U"
    str_2 = ansi_text_wrapper_0.fill(str_0)
    list_0 = ansi_text_wrapper_0.wrap(str_1)
    list_1 = ansi_text_wrapper_0.wrap(str_2)
    list_2 = ansi_text_wrapper_0.wrap(str_2)

def test_case_7():
    str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
    int_0 = module_0.len_without_ansi(str_0)

def test_case_8():
    str_0 = '\ni'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper()
    str_1 = ansi_text_wrapper_0.fill(str_0)

def test_case_9():
    int_0 = 50987760
    str_0 = 'm'
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0, placeholder=str_0)
    str_1 = ''
    list_0 = ansi_text_wrapper_0.wrap(str_1)
    list_1 = ansi_text_wrapper_0.wrap(str_0)

def test_case_10():
    str_0 = ''
    str_1 = "\x0cl>83'L^]|1Q-s-[p"
    int_0 = 80
    bool_0 = True
    bool_1 = None
    int_1 = -2659
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, bool_0, bool_1, int_1, max_lines=int_1)
    str_2 = ansi_text_wrapper_0.fill(str_1)
    list_0 = ansi_text_wrapper_0.wrap(str_0)
    str_3 = 'Change ownership of a path.\n\n    This function processes the given ``path`` with\n    :obj:`~flutils.normalize_path`.\n\n    If the given ``path`` does NOT exist, nothing will be done.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path of the file or directory that will have it\'s ownership\n            changed.  This value can be a :term:`glob pattern`.\n        user (:obj:`str` or :obj:`int`, optional): The "login name" used to set\n            the owner of ``path``.  A value of ``\'-1\'`` will leave the\n            owner unchanged.  Defaults to the "login name" of the current user.\n        group (:obj:`str` or :obj:`int`, optional): The group name used to set\n            the group of ``path``.  A value of ``\'-1\'`` will leave the\n            group unchanged.  Defaults to the current user\'s group.\n        include_parent (:obj:`bool`, optional): A value of :obj:`True` will\n            chown the parent directory of the given ``path`` that contains\n            a :term:`glob pattern`.  Defaults to :obj:`False`.\n\n    Raises:\n        OSError: If the given :obj:`user` does not exist as a "login\n            name" for this operating system.\n        OSError: If the given :obj:`group` does not exist as a "group\n            name" for this operating system.\n\n    :rtype: :obj:`None`\n\n    Examples:\n        >>> from flutils.pathutils import chown\n        >>> chown(\'~/tmp/flutils.tests.osutils.txt\')\n\n        Supports a :term:`glob pattern`.  So to recursively change the\n        ownership of a directory just do:\n\n        >>> chown(\'~/tmp/**\')\n\n\n        To change ownership of all the directory\'s immediate contents:\n\n        >>> chown(\'~/tmp/*\', user=\'foo\', group=\'bar\')\n\n    '
    list_1 = ansi_text_wrapper_0.wrap(str_3)