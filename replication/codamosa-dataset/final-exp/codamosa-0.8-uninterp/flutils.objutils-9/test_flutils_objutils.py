# Automatically generated by Pynguin.
import flutils.objutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = None
    dict_0 = {str_0: str_0, str_0: str_0}
    bool_0 = module_0.has_any_callables(dict_0)

def test_case_2():
    str_0 = 'index'
    str_1 = (str_0, str_0, str_0, str_0)
    bool_0 = module_0.has_any_callables(str_0, *str_1)

def test_case_3():
    str_0 = "The given 'setup_dir' of %r does NOT contain a setup.cfg file."
    bool_0 = module_0.has_attrs(str_0)

def test_case_4():
    str_0 = '%Y-pYpA\x0c@\x0bNcq#~6u'
    list_0 = [str_0, str_0]
    bool_0 = module_0.has_callables(str_0, *list_0)

def test_case_5():
    str_0 = '%Y-pYpA\x0c@\x0bNcq#~6u'
    list_0 = []
    bool_0 = module_0.has_callables(str_0, *list_0)

def test_case_6():
    str_0 = 'items'
    bool_0 = module_0.is_list_like(str_0)
    str_1 = (str_0, str_0, str_0, str_0)
    var_0 = dict()
    bool_1 = module_0.has_callables(var_0, *str_1)

def test_case_7():
    var_0 = dict()
    str_0 = 'keys'
    str_1 = 'values'
    str_2 = (str_0, str_0, str_0, str_1)
    bool_0 = module_0.is_list_like(str_2)
    bool_1 = module_0.has_any_callables(var_0, *str_2)

def test_case_8():
    int_0 = 2404
    bool_0 = module_0.is_subclass_of_any(int_0)

def test_case_9():
    tuple_0 = ()
    list_0 = [tuple_0]
    str_0 = 's{t*t'
    list_1 = [str_0, str_0]
    bool_0 = module_0.has_any_callables(list_0, *list_1)

def test_case_10():
    str_0 = 'items'
    str_1 = (str_0, str_0, str_0, str_0)
    var_0 = dict()
    bool_0 = module_0.has_callables(var_0, *str_1)

def test_case_11():
    str_0 = '__doc__'
    list_0 = []
    bool_0 = module_0.has_any_callables(str_0, *list_0)
    str_1 = 'Run the given command line command and return the command\'s\n    return code.\n\n    When the given ``command`` is executed, the command\'s stdout and\n    stderr outputs are captured in a pseudo terminal.  The captured\n    outputs are then added to this function\'s ``stdout`` and ``stderr``\n    IO objects.\n\n    This function will capture any ANSI escape codes in the output of\n    the given command.  This even includes ANSI colors.\n\n    Args:\n        command (str, List[str], Tuple[str]): The command to execute.\n        stdout (:obj:`typing.IO`, optional):  An input/output stream\n            that will hold the command\'s ``stdout``.  Defaults to:\n            :obj:`sys.stdout <sys.stdout>`; which will output\n            the command\'s ``stdout`` to the terminal.\n        stderr (:obj:`typing.IO`, optional):  An input/output stream\n            that will hold the command\'s ``stderr``.  Defaults to:\n            :obj:`sys.stderr <sys.stderr>`; which will output\n            the command\'s ``stderr`` to the terminal.\n        columns (int, optional): The number of character columns the pseudo\n            terminal may use.  If ``force_dimensions`` is :obj:`False`, this\n            will be the fallback columns value when the the current terminal\'s\n            column size cannot be found.  If ``force_dimensions`` is\n            :obj:`True`, this will be actual character column value.\n            Defaults to: ``80``.\n        lines (int, optional): The number of character lines the pseudo\n            terminal may use.  If ``force_dimensions`` is :obj:`False`, this\n            will be the fallback lines value when the the current terminal\'s\n            line size cannot be found.  If ``force_dimensions`` is :obj:`True`,\n            this will be actual character lines value.  Defaults to: ``24``.\n        force_dimensions (bool, optional): This controls how the given\n            ``columns`` and ``lines`` values are to be used.  A value of\n            :obj:`False` will use the given ``columns`` and ``lines`` as\n            fallback values if the current terminal dimensions cannot be\n            successfully queried.  A value of :obj:`True` will resize the\n            pseudo terminal using the given ``columns`` and ``lines`` values.\n            Defaults to: :obj:`False`.\n        interactive (bool, optional): A value of :obj:`True` will\n            interactively run the given ``command``.  Defaults to:\n            :obj:`False`.\n        **kwargs: Any additional key-word-arguments used with\n            :obj:`Popen <subprocess.Popen>`.  ``stdout`` and ``stderr``\n            will not be used if given in ``**default_kwargs``.  Defaults to:\n            ``{}``.\n\n    Returns:\n        int: The return value from running the given ``command``\n\n    Raises:\n        RuntimeError: When using ``interactive=True`` and the ``bash``\n            executable cannot be located.\n        OSError: Any errors raised when trying to read the pseudo terminal.\n\n    Example:\n        An example using :obj:`~flutils.cmdutils.run` in code::\n\n            from flutils.cmdutils import run\n            from io import BytesIO\n            import sys\n            import os\n\n            home = os.path.expanduser(\'~\')\n            with BytesIO() as stream:\n                return_code = run(\n                    \'ls "%s"\' % home,\n                    stdout=stream,\n                    stderr=stream\n                )\n                text = stream.getvalue()\n            text = text.decode(sys.getdefaultencoding())\n            if return_code == 0:\n                print(text)\n            else:\n                print(\'Error: %s\' % text)\n    '
    int_0 = 3
    list_1 = [str_0, str_0]
    bool_1 = module_0.has_callables(int_0, *list_1)
    list_2 = [str_1, str_0, str_1]
    bool_2 = module_0.has_attrs(str_0, *list_2)
    str_2 = 'S=XLG'
    bool_3 = module_0.has_any_callables(str_2)
    bool_4 = module_0.has_any_callables(list_1)
    bool_5 = module_0.is_subclass_of_any(list_2)
    bool_6 = module_0.is_list_like(bool_5)
    list_3 = [str_1, str_1, str_2]
    bool_7 = module_0.is_subclass_of_any(str_0)
    dict_0 = {}
    bool_8 = module_0.has_attrs(bool_7, *list_1)
    bool_9 = module_0.has_any_attrs(int_0, *list_2)
    bool_10 = True
    bool_11 = module_0.is_list_like(list_1)
    str_3 = 'n<@\n+L\x0c4hLUI'
    list_4 = None
    bool_12 = False
    bool_13 = module_0.has_any_callables(bool_12, *list_1)
    list_5 = []
    bool_14 = module_0.has_callables(list_4, *list_5)
    bool_15 = module_0.has_attrs(str_3, *list_2)
    tuple_0 = (list_3, dict_0, bool_10, list_3)
    list_6 = []
    bool_16 = module_0.is_subclass_of_any(tuple_0, *list_6)