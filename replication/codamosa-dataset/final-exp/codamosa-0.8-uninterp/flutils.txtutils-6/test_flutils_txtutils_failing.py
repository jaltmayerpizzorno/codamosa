# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    try:
        bytes_0 = None
        int_0 = module_0.len_without_ansi(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "S*KfQE'Jh|j!p"
        bool_0 = True
        int_0 = 1154
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, max_lines=int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -2723
        str_0 = 'kkLqumK5uqZ4\x0c2M'
        bool_0 = False
        bool_1 = True
        bool_2 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_2)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
        int_1 = 2287
        str_1 = 'pre_txt'
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, str_0, bool_0, bool_1, int_1, placeholder=str_1)
        bool_3 = True
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(bool_3)
        list_1 = ansi_text_wrapper_1.wrap(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 's'
        int_0 = 3002
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0, placeholder=str_0)
        str_1 = ')uRb2ST'
        str_2 = ansi_text_wrapper_0.fill(str_1)
        str_3 = '5QqZ4'
        str_4 = ansi_text_wrapper_0.fill(str_3)
        str_5 = 'Ensure the state of the given :obj:`path` is present and a directory.\n\n    This function processes the given ``path`` with\n    :obj:`~flutils.normalize_path`.\n\n    If the given ``path`` does **NOT** exist, it will be created as a\n    directory.\n\n    If the parent paths of the given ``path`` do not exist, they will also be\n    created with the ``mode``, ``user`` and ``group``.\n\n    If the given ``path`` does exist as a directory, the ``mode``, ``user``,\n    and :``group`` will be applied.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path of the directory.\n        mode (:obj:`int`, optional): The mode applied to the ``path``.\n            Defaults to ``0o700``.\n        user (:obj:`str` or :obj:`int`, optional): The "login name" used to\n            set the owner of the given ``path``.  A value of ``\'-1\'`` will\n            leave the owner unchanged.  Defaults to the "login name" of the\n            current user.\n        group (:obj:`str` or :obj:`int`, optional): The group name used to set\n            the group of the given ``path``.  A value of ``\'-1\'`` will leave\n            the group unchanged.  Defaults to the current user\'s group.\n\n    Raises:\n        ValueError: if the given ``path`` contains a glob pattern.\n        ValueError: if the given ``path`` is not an absolute path.\n        FileExistsError: if the given ``path`` exists and is not a directory.\n        FileExistsError: if a parent of the given ``path`` exists and is\n            not a directory.\n\n    :rtype: :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n        >>> from flutils.pathutils import directory_present\n        >>> directory_present(\'~/tmp/test_path\')\n        PosixPath(\'/Users/len/tmp/test_path\')\n\n    '
        list_0 = ansi_text_wrapper_0.wrap(str_5)
        sequence_0 = None
        int_1 = module_0.len_without_ansi(sequence_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ">`a~;'Z"
        int_0 = -462
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, bool_0, bool_0, int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        int_0 = -2701
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0, placeholder=str_0)
        bool_0 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(str_0, bool_0, bool_0, max_lines=int_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
        str_2 = 'A subclass of the module type which triggers loading upon attribute\n    access.\n\n    This class is a "derivative work" of the Python\n    `importlib.util._LazyModule <https://bit.ly/2EBPI1g>`_, and is:\n\n    `Copyright © 2001-2018 Python Software Foundation; All Rights Reserved\n    <https://bit.ly/2JzG17l>`_\n\n    This differs from the ``importlib.util._LazyModule`` in that it tracks\n    the state of the Lazy Loaded module and has had some\n    `unused code <https://bit.ly/2EARVu6>` removed.\n    '
        str_3 = ansi_text_wrapper_0.fill(str_2)
        list_0 = []
        tuple_0 = (list_0,)
        int_1 = module_0.len_without_ansi(tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\x1b[38;5;2{9mfoA6ar\x1b[0m'
        set_0 = {str_0, str_0, str_0, str_0}
        int_0 = module_0.len_without_ansi(set_0)
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(str_0, bool_0, bool_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass