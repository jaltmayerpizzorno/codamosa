# Automatically generated by Pynguin.
import tqdm.rich as module_0
import tqdm.std as module_1
import rich.progress as module_2
import rich.console as module_3

def test_case_0():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        tqdm_rich_0 = module_0.tqdm_rich(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        dict_0 = {list_0: list_0, list_0: list_0, list_0: list_0, list_0: list_0}
        rate_column_0 = module_0.RateColumn()
        tuple_0 = (dict_0, rate_column_0)
        float_0 = 1443.8
        rate_column_1 = module_0.RateColumn(float_0)
        var_0 = rate_column_1.render(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        tqdm_rich_0 = module_0.tqdm_rich(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        fraction_column_0 = module_0.FractionColumn()
        list_0 = [fraction_column_0, fraction_column_0, fraction_column_0, fraction_column_0]
        str_0 = 'U0[~Y<wH'
        fraction_column_1 = None
        str_1 = 'thread_map'
        dict_0 = {str_0: fraction_column_1, str_1: list_0}
        var_0 = module_0.trrange(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 10
        var_0 = range(int_0)
        tqdm_0 = module_1.tqdm(var_0)
        var_1 = tqdm_0.close()
        var_2 = tqdm_0._task_id
    except BaseException:
        pass

def test_case_6():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_7():
    try:
        fraction_column_0 = module_0.FractionColumn()
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '\\|Rd1/P/T('
        str_1 = "w`'I&:\x0bGd\x0b(%"
        list_0 = [str_1, str_0, str_1, str_1]
        bool_0 = True
        float_0 = 2023.814115
        bool_1 = True
        progress_0 = module_2.Progress(*list_0, auto_refresh=bool_0, refresh_per_second=float_0, redirect_stderr=bool_1)
        var_0 = progress_0.add_task(str_0, bool_1)
        callable_0 = None
        task_0 = module_2.Task(var_0, str_1, float_0, float_0, callable_0, bool_1)
        fraction_column_0 = module_0.FractionColumn()
        var_1 = fraction_column_0.render(task_0)
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\\|Rd1/P/T('
        str_1 = 'lyFV\n\x0c'
        str_2 = "w`'I&:\x0bGd\x0b(%"
        bool_0 = True
        list_0 = [str_2, str_2, str_2]
        bool_1 = True
        float_0 = 2023.814115
        bool_2 = False
        progress_0 = module_2.Progress(*list_0, auto_refresh=bool_1, refresh_per_second=float_0, redirect_stderr=bool_2)
        var_0 = progress_0.add_task(str_0, bool_0)
        callable_0 = None
        bool_3 = False
        task_0 = module_2.Task(var_0, str_2, float_0, float_0, callable_0, bool_3)
        rate_column_0 = module_0.RateColumn()
        var_1 = rate_column_0.render(task_0)
        task_1 = module_2.Task(var_0, str_1, float_0, float_0, callable_0, float_0)
        no_change_0 = module_3.NoChange()
        fraction_column_0 = module_0.FractionColumn(no_change_0)
        var_2 = fraction_column_0.render(task_1)
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass