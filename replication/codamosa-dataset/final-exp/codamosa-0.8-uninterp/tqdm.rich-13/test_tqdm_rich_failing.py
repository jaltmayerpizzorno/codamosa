# Automatically generated by Pynguin.
import tqdm.rich as module_0
import rich.progress as module_1
import rich.console as module_2
import builtins as module_3

def test_case_0():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '}lT9\x0c68u'
        list_0 = [str_0, str_0]
        list_1 = [str_0]
        tqdm_rich_0 = module_0.tqdm_rich(*list_1)
        var_0 = tqdm_rich_0.display(*list_0)
        var_1 = tqdm_rich_0.display()
        dict_0 = {str_0: list_0}
        tqdm_rich_1 = module_0.tqdm_rich(**dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = module_0.trrange()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'LINES'
        bool_0 = False
        dict_0 = {str_0: str_0, str_0: str_0}
        str_1 = '\r14N\\r9:'
        list_0 = [str_1, str_1, str_1]
        progress_0 = module_1.Progress(*list_0)
        var_0 = progress_0.add_task(str_0, bool_0, **dict_0)
        str_2 = '.a;'
        float_0 = -269.0
        no_change_0 = module_2.NoChange()
        str_3 = 'Y\tHM74R"H'
        dict_1 = {str_3: float_0}
        task_0 = module_1.Task(var_0, str_2, float_0, float_0, no_change_0, dict_1)
        fraction_column_0 = module_0.FractionColumn()
        var_1 = fraction_column_0.render(task_0)
        dict_2 = None
        fraction_column_1 = module_0.FractionColumn()
        var_2 = module_0.trrange(**dict_2)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = module_0.trrange()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 1
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = None
        str_0 = '{'
        float_0 = 1826.0
        task_0 = module_1.Task(var_0, str_0, float_0, float_0, str_0)
        rate_column_0 = module_0.RateColumn()
        segment_0 = None
        list_0 = [segment_0]
        object_0 = module_3.object()
        var_1 = task_0.__eq__(object_0)
        list_1 = [list_0, list_0, list_0]
        fraction_column_0 = module_0.FractionColumn(list_1)
        var_2 = fraction_column_0.render(task_0)
        var_3 = rate_column_0.render(task_0)
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass