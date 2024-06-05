# Automatically generated by Pynguin.
import flutils.namedtupleutils as module_0
import types as module_1

def test_case_0():
    str_0 = 'LD1k\nqntD+w]JCDZ'
    dict_0 = {str_0: str_0}
    float_0 = 2872.715
    tuple_0 = (str_0, dict_0, float_0)
    var_0 = module_0.to_namedtuple(tuple_0)

def test_case_1():
    str_0 = 'Ensure the state of the given :obj:`path` is present and a directory.\n\n    This function processes the given ``path`` with\n    :obj:`~flutils.normalize_path`.\n\n    If the given ``path`` does **NOT** exist, it will be created as a\n    directory.\n\n    If the parent paths of the given ``path`` do not exist, they will also be\n    created with the ``mode``, ``user`` and ``group``.\n\n    If the given ``path`` does exist as a directory, the ``mode``, ``user``,\n    and :``group`` will be applied.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path of the directory.\n        mode (:obj:`int`, optional): The mode applied to the ``path``.\n            Defaults to ``0o700``.\n        user (:obj:`str` or :obj:`int`, optional): The "login name" used to\n            set the owner of the given ``path``.  A value of ``\'-1\'`` will\n            leave the owner unchanged.  Defaults to the "login name" of the\n            current user.\n        group (:obj:`str` or :obj:`int`, optional): The group name used to set\n            the group of the given ``path``.  A value of ``\'-1\'`` will leave\n            the group unchanged.  Defaults to the current user\'s group.\n\n    Raises:\n        ValueError: if the given ``path`` contains a glob pattern.\n        ValueError: if the given ``path`` is not an absolute path.\n        FileExistsError: if the given ``path`` exists and is not a directory.\n        FileExistsError: if a parent of the given ``path`` exists and is\n            not a directory.\n\n    :rtype: :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n        >>> from flutils.pathutils import directory_present\n        >>> directory_present(\'~/tmp/test_path\')\n        PosixPath(\'/Users/len/tmp/test_path\')\n\n    '
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)

def test_case_2():
    simple_namespace_0 = module_1.SimpleNamespace()
    var_0 = module_0.to_namedtuple(simple_namespace_0)

def test_case_3():
    str_0 = 'camel_to_underscore'
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    list_0 = [var_0, var_0, var_0]
    var_1 = module_0.to_namedtuple(list_0)

def test_case_4():
    str_0 = 'Ensure the state of the given :obj:`path` is present and a directory.\n\n    This function processes the given ``path`` with\n    :obj:`~flutils.normalize_path`.\n\n    If the given ``path`` does **NOT** exist, it will be created as a\n    directory.\n\n    If the parent paths of the given ``path`` do not exist, they will also be\n    created with the ``mode``, ``user`` and ``group``.\n\n    If the given ``path`` does exist as a directory, the ``mode``, ``user``,\n    and :``group`` will be applied.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path of the directory.\n        mode (:obj:`int`, optional): The mode applied to the ``path``.\n            Defaults to ``0o700``.\n        user (:obj:`str` or :obj:`int`, optional): The "login name" used to\n            set the owner of the given ``path``.  A value of ``\'-1\'`` will\n            leave the owner unchanged.  Defaults to the "login name" of the\n            current user.\n        group (:obj:`str` or :obj:`int`, optional): The group name used to set\n            the group of the given ``path``.  A value of ``\'-1\'`` will leave\n            the group unchanged.  Defaults to the current user\'s group.\n\n    Raises:\n        ValueError: if the given ``path`` contains a glob pattern.\n        ValueError: if the given ``path`` is not an absolute path.\n        FileExistsError: if the given ``path`` exists and is not a directory.\n        FileExistsError: if a parent of the given ``path`` exists and is\n            not a directory.\n\n    :rtype: :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n        >>> from flutils.pathutils import directory_present\n        >>> directory_present(\'~/tmp/test_path\')\n        PosixPath(\'/Users/len/tmp/test_path\')\n\n    '
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    list_0 = [var_0, var_0, var_0]
    var_1 = module_0.to_namedtuple(list_0)
    simple_namespace_0 = module_1.SimpleNamespace()

def test_case_5():
    int_0 = 3250
    tuple_0 = None
    dict_0 = {int_0: int_0, tuple_0: tuple_0}
    tuple_1 = (dict_0,)
    tuple_2 = (tuple_1, int_0)
    var_0 = module_0.to_namedtuple(tuple_2)