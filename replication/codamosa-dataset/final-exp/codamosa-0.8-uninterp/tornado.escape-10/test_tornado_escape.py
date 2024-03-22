# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Hello http://tornadoweb.org!'
    str_1 = module_0.linkify(str_0)

def test_case_2():
    str_0 = ', x[2~'
    str_1 = module_0.xhtml_unescape(str_0)

def test_case_3():
    bytes_0 = b'.\t\x1d\xa1\xf3\x9d\xa5\xfe'
    str_0 = module_0.url_escape(bytes_0)

def test_case_4():
    str_0 = ")x=\x0b'~9i@=DN"
    optional_0 = module_0.utf8(str_0)

def test_case_5():
    str_0 = 'A command line parsing module that lets modules define their own options.\n\nThis module is inspired by Google\'s `gflags\n<https://github.com/google/python-gflags>`_. The primary difference\nwith libraries such as `argparse` is that a global registry is used so\nthat options may be defined in any module (it also enables\n`tornado.log` by default). The rest of Tornado does not depend on this\nmodule, so feel free to use `argparse` or other configuration\nlibraries if you prefer them.\n\nOptions must be defined with `tornado.options.define` before use,\ngenerally at the top level of a module. The options are then\naccessible as attributes of `tornado.options.options`::\n\n    # myapp/db.py\n    from tornado.options import define, options\n\n    define("mysql_host", default="127.0.0.1:3306", help="Main user DB")\n    define("memcache_hosts", default="127.0.0.1:11011", multiple=True,\n           help="Main user memcache servers")\n\n    def connect():\n        db = database.Connection(options.mysql_host)\n        ...\n\n    # myapp/server.py\n    from tornado.options import define, options\n\n    define("port", default=8080, help="port to listen on")\n\n    def start_server():\n        app = make_app()\n        app.listen(options.port)\n\nThe ``main()`` method of your application does not need to be aware of all of\nthe options used throughout your program; they are all automatically loaded\nwhen the modules are loaded.  However, all modules that define options\nmust have been imported before the command line is parsed.\n\nYour ``main()`` method can parse the command line or parse a config file with\neither `parse_command_line` or `parse_config_file`::\n\n    import myapp.db, myapp.server\n    import tornado.options\n\n    if __name__ == \'__main__\':\n        tornado.options.parse_command_line()\n        # or\n        tornado.options.parse_config_file("/etc/server.conf")\n\n.. note::\n\n   When using multiple ``parse_*`` functions, pass ``final=False`` to all\n   but the last one, or side effects may occur twice (in particular,\n   this can result in log messages being doubled).\n\n`tornado.options.options` is a singleton instance of `OptionParser`, and\nthe top-level functions in this module (`define`, `parse_command_line`, etc)\nsimply call methods on it.  You may create additional `OptionParser`\ninstances to define isolated sets of options, such as for subcommands.\n\n.. note::\n\n   By default, several options are defined that will configure the\n   standard `logging` module when `parse_command_line` or `parse_config_file`\n   are called.  If you want Tornado to leave the logging configuration\n   alone so you can manage it yourself, either pass ``--logging=none``\n   on the command line or do the following to disable it in code::\n\n       from tornado.options import options, parse_command_line\n       options.logging = None\n       parse_command_line()\n\n.. versionchanged:: 4.3\n   Dashes and underscores are fully interchangeable in option names;\n   options can be defined, set, and read with any mix of the two.\n   Dashes are typical for command-line usage while config files require\n   underscores.\n'
    any_0 = module_0.recursive_unicode(str_0)

def test_case_6():
    str_0 = "Decorator to run a synchronous method asynchronously on an executor.\n\n    Returns a future.\n\n    The executor to be used is determined by the ``executor``\n    attributes of ``self``. To use a different attribute name, pass a\n    keyword argument to the decorator::\n\n        @run_on_executor(executor='_thread_pool')\n        def foo(self):\n            pass\n\n    This decorator should not be confused with the similarly-named\n    `.IOLoop.run_in_executor`. In general, using ``run_in_executor``\n    when *calling* a blocking method is recommended instead of using\n    this decorator when *defining* a method. If compatibility with older\n    versions of Tornado is required, consider defining an executor\n    and using ``executor.submit()`` at the call site.\n\n    .. versionchanged:: 4.2\n       Added keyword arguments to use alternative attributes.\n\n    .. versionchanged:: 5.0\n       Always uses the current IOLoop instead of ``self.io_loop``.\n\n    .. versionchanged:: 5.1\n       Returns a `.Future` compatible with ``await`` instead of a\n       `concurrent.futures.Future`.\n\n    .. deprecated:: 5.1\n\n       The ``callback`` argument is deprecated and will be removed in\n       6.0. The decorator itself is discouraged in new code but will\n       not be removed in 6.0.\n\n    .. versionchanged:: 6.0\n\n       The ``callback`` argument was removed.\n    "
    bytes_0 = b''
    bool_0 = False
    str_1 = ':l"%4A_w_2eW[H37#uV'
    var_0 = module_0.url_unescape(bytes_0, bool_0)
    str_2 = ';$1y!Ysy,\t`v'
    str_3 = module_0.xhtml_unescape(str_1)
    list_0 = [str_2, str_0]
    str_4 = module_0.linkify(bytes_0, bool_0, str_1, list_0)
    any_0 = module_0.recursive_unicode(bytes_0)
    var_1 = module_0.url_unescape(str_0)
    str_5 = module_0.squeeze(str_4)
    str_6 = module_0.linkify(str_2, list_0)

def test_case_7():
    str_0 = 'A command line parsing module that lets modules define their own options.\n\nThis module is inspired by Google\'s `gflags\n<https://github.com/google/python-gflags>`_. The primary difference\nwith libraries such as `argparse` is that a global registry is used so\nthat options may be defined in any module (it also enables\n`tornado.log` by default). The rest of Tornado does not depend on this\nmodule, so feel free to use `argparse` or other configuration\nlibraries if you prefer them.\n\nOptions must be defined with `tornado.options.define` before use,\ngenerally at the top level of a module. The options are then\naccessible as attributes of `tornado.options.options`::\n\n    # myapp/db.py\n    from tornado.options import define, options\n\n    define("mysql_host", default="127.0.0.1:3306", help="Main user DB")\n    define("memcache_hosts", default="127.0.0.1:11011", multiple=True,\n           help="Main user memcache servers")\n\n    def connect():\n        db = database.Connection(options.mysql_host)\n        ...\n\n    # myapp/server.py\n    from tornado.options import define, options\n\n    define("port", default=8080, help="port to listen on")\n\n    def start_server():\n        app = make_app()\n        app.listen(options.port)\n\nThe ``main()`` method of your application does not need to be aware of all of\nthe options used throughout your program; they are all automatically loaded\nwhen the modules are loaded.  However, all modules that define options\nmust have been imported before the command line is parsed.\n\nYour ``main()`` method can parse the command line or parse a config file with\neither `parse_command_line` or `parse_config_file`::\n\n    import myapp.db, myapp.server\n    import tornado.options\n\n    if __name__ == \'__main__\':\n        tornado.options.parse_command_line()\n        # or\n        tornado.options.parse_config_file("/etc/server.conf")\n\n.. note::\n\n   When using multiple ``parse_*`` functions, pass ``final=False`` to all\n   but the last one, or side effects may occur twice (in particular,\n   this can result in log messages being doubled).\n\n`tornado.options.options` is a singleton instance of `OptionParser`, and\nthe top-level functions in this module (`define`, `parse_command_line`, etc)\nsimply call methods on it.  You may create additional `OptionParser`\ninstances to define isolated sets of options, such as for subcommands.\n\n.. note::\n\n   By default, several options are defined that will configure the\n   standard `logging` module when `parse_command_line` or `parse_config_file`\n   are called.  If you want Tornado to leave the logging configuration\n   alone so you can manage it yourself, either pass ``--logging=none``\n   on the command line or do the following to disable it in code::\n\n       from tornado.options import options, parse_command_line\n       options.logging = None\n       parse_command_line()\n\n.. versionchanged:: 4.3\n   Dashes and underscores are fully interchangeable in option names;\n   options can be defined, set, and read with any mix of the two.\n   Dashes are typical for command-line usage while config files require\n   underscores.\n'
    any_0 = module_0.recursive_unicode(str_0)
    list_0 = [str_0, str_0, str_0, str_0]
    str_1 = module_0.linkify(str_0, list_0)

def test_case_8():
    str_0 = 'Hello https://ornadoweb.org/en/stable/#hello-world!'
    str_1 = module_0.linkify(str_0, str_0)

def test_case_9():
    str_0 = 'A command line parsing module that lets modules define their own options.\n\nThis module is inspired by Google\'s `gflags\n<https://github.com/google/python-gflags>`_. The primary difference\nwith libraries such as `argparse` is that a global registry is used so\nthat options may be defined in any module (it also enables\n`tornado.log` by default). The rest of Tornado does not depend on this\nmodule, so feel free to use `argparse` or other configuration\nlibraries if you prefer them.\n\nOptions must be defined with `tornado.options.define` before use,\ngenerally at the top level of a module. The options are then\naccessible as attributes of `tornado.options.options`::\n\n    # myapp/db.py\n    from tornado.options import define, options\n\n    define("mysql_host", default="127.0.0.1:3306", help="Main user DB")\n    define("memcache_hosts", default="127.0.0.1:11011", multiple=True,\n           help="Main user memcache servers")\n\n    def connect():\n        db = database.Connection(options.mysql_host)\n        ...\n\n    # myapp/server.py\n    from tornado.options import define, options\n\n    define("port", default=8080, help="port to listen on")\n\n    def start_server():\n        app = make_app()\n        app.listen(options.port)\n\nThe ``main()`` method of your application does not need to be aware of all of\nthe options used throughout your program; they are all automatically loaded\nwhen the modules are loaded.  However, all modules that define options\nmust have been imported before the command line is parsed.\n\nYour ``main()`` method can parse the command line or parse a config file with\neither `parse_command_line` or `parse_config_file`::\n\n    import myapp.db, myapp.server\n    import tornado.options\n\n    if __name__ == \'__main__\':\n        tornado.options.parse_command_line()\n        # or\n        tornado.options.parse_config_file("/etc/server.conf")\n\n.. note::\n\n   When using multiple ``parse_*`` functions, pass ``final=False`` to all\n   but the last one, or side effects may occur twice (in particular,\n   this can result in log messages being doubled).\n\n`tornado.options.options` is a singleton instance of `OptionParser`, and\nthe top-level functions in this module (`define`, `parse_command_line`, etc)\nsimply call methods on it.  You may create additional `OptionParser`\ninstances to define isolated sets of options, such as for subcommands.\n\n.. note::\n\n   By default, several options are defined that will configure the\n   standard `logging` module when `parse_command_line` or `parse_config_file`\n   are called.  If you want Tornado to leave the logging configuration\n   alone so you can manage it yourself, either pass ``--logging=none``\n   on the command line or do the following to disable it in code::\n\n       from tornado.options import options, parse_command_line\n       options.logging = None\n       parse_command_line()\n\n.. versionchanged:: 4.3\n   Dashes and underscores are fully interchangeable in option names;\n   options can be defined, set, and read with any mix of the two.\n   Dashes are typical for command-line usage while config files require\n   underscores.\n'
    any_0 = module_0.recursive_unicode(str_0)
    str_1 = '.o'
    str_2 = '"V3$vI_%C\r05+7'
    list_0 = [str_0, str_1, str_0, str_2]
    str_3 = module_0.linkify(str_0, list_0)
    bool_0 = False
    var_0 = module_0.url_unescape(str_3)
    dict_0 = module_0.parse_qs_bytes(str_1, bool_0, bool_0)
    str_4 = module_0.xhtml_unescape(str_2)
    dict_1 = module_0.parse_qs_bytes(str_0)
    none_type_0 = None
    optional_0 = module_0.to_unicode(str_1)
    var_1 = module_0.url_unescape(str_4, none_type_0)
    str_5 = module_0.squeeze(str_4)
    str_6 = module_0.linkify(str_4, bool_0)

def test_case_10():
    str_0 = '<p>You can get more information at <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>.</p>'
    bool_0 = True
    list_0 = []
    str_1 = module_0.xhtml_escape(str_0)
    str_2 = module_0.linkify(str_0, bool_0, list_0)
    str_3 = 'Hello www.tornadoweb.org!'
    str_4 = module_0.linkify(str_3)
    bool_1 = True
    dict_0 = module_0.parse_qs_bytes(str_2, bool_0)
    str_5 = module_0.linkify(str_3, bool_1, str_2)

def test_case_11():
    str_0 = 'mydomain.com'
    str_1 = module_0.linkify(str_0)
    str_2 = 'www.mydomain.com'
    str_3 = module_0.linkify(str_2)
    str_4 = 'B^:8j&EO'
    str_5 = module_0.linkify(str_4)
    str_6 = module_0.linkify(str_3)
    bool_0 = True
    str_7 = 'https://github.com/google'
    list_0 = [str_7]
    str_8 = module_0.linkify(str_6, bool_0, str_2, list_0)
    str_9 = module_0.linkify(str_2, str_3)

def test_case_12():
    str_0 = 'A command line parsing module that lets modules define their own options.\n\nThis module is inspired by Google\'s `gflags\n<https://github.com/google/python-gflags>`_. The primary difference\nwith libraries such as `argparse` is that a global registry is used so\nthat options may be defined in any module (it also enables\n`tornado.log` by default). The rest of Tornado does not depend on this\nmodule, so feel free to use `argparse` or other configuration\nlibraries if you prefer them.\n\nOptions must be defined with `tornado.options.define` before use,\ngenerally at the top level of a module. The options are then\naccessible as attributes of `tornado.options.options`::\n\n    # myapp/db.py\n    from tornado.options import define, options\n\n    define("mysql_host", default="127.0.0.1:3306", help="Main user DB")\n    define("memcache_hosts", default="127.0.0.1:11011", multiple=True,\n           help="Main user memcache servers")\n\n    def connect():\n        db = database.Connection(options.mysql_host)\n        ...\n\n    # myapp/server.py\n    from tornado.options import define, options\n\n    define("port", default=8080, help="port to listen on")\n\n    def start_server():\n        app = make_app()\n        app.listen(options.port)\n\nThe ``main()`` method of your application does not need to be aware of all of\nthe options used throughout your program; they are all automatically loaded\nwhen the modules are loaded.  However, all modules that define options\nmust have been imported before the command line is parsed.\n\nYour ``main()`` method can parse the command line or parse a config file with\neither `parse_command_line` or `parse_config_file`::\n\n    import myapp.db, myapp.server\n    import tornado.options\n\n    if __name__ == \'__main__\':\n        tornado.options.parse_command_line()\n        # or\n        tornado.options.parse_config_file("/etc/server.conf")\n\n.. note::\n\n   When using multiple ``parse_*`` functions, pass ``final=False`` to all\n   but the last one, or side effects may occur twice (in particular,\n   this can result in log messages being doubled).\n\n`tornado.options.options` is a singleton instance of `OptionParser`, and\nthe top-level functions in this module (`define`, `parse_command_line`, etc)\nsimply call methods on it.  You may create additional `OptionParser`\ninstances to define isolated sets of options, such as for subcommands.\n\n.. note::\n\n   By default, several options are defined that will configure the\n   standard `logging` module when `parse_command_line` or `parse_config_file`\n   are called.  If you want Tornado to leave the logging configuration\n   alone so you can manage it yourself, either pass ``--logging=none``\n   on the command line or do the following to disable it in code::\n\n       from tornado.options import options, parse_command_line\n       options.logging = None\n       parse_command_line()\n\n.. versionchanged:: 4.3\n   Dashes and underscores are fully interchangeable in option names;\n   options can be defined, set, and read with any mix of the two.\n   Dashes are typical for command-line usage while config files require\n   underscores.\n'
    any_0 = module_0.recursive_unicode(str_0)
    str_1 = ''
    var_0 = module_0.url_unescape(str_0, str_0)
    str_2 = '\x0ctq\x0b&6O==V'
    list_0 = [str_2, str_2, str_1, str_2, str_0, str_2]
    str_3 = module_0.linkify(str_0, list_0)
    str_4 = module_0.url_escape(str_2)
    any_1 = module_0.recursive_unicode(list_0)
    str_5 = module_0.json_encode(list_0)
    str_6 = module_0.json_encode(str_3)
    str_7 = module_0.xhtml_unescape(str_3)
    bool_0 = None
    str_8 = module_0.xhtml_unescape(str_2)
    dict_0 = module_0.parse_qs_bytes(str_0)
    var_1 = module_0.url_unescape(str_1, bool_0)
    bool_1 = False
    bool_2 = False
    str_9 = module_0.linkify(str_5, bool_2, str_8, bool_1, list_0)

def test_case_13():
    str_0 = 'You can get more information at www.tornadoweb.org.'
    str_1 = module_0.linkify(str_0)