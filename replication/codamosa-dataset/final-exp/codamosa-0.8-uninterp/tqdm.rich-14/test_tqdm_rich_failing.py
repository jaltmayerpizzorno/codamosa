# Automatically generated by Pynguin.
import tqdm.rich as module_0

def test_case_0():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 0.1
        fraction_column_0 = module_0.FractionColumn(float_0)
        int_0 = 4
        list_0 = [fraction_column_0, int_0]
        var_0 = fraction_column_0.render(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = module_0.trrange()
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = module_0.trrange()
    except BaseException:
        pass

def test_case_5():
    try:
        tqdm_rich_0 = module_0.tqdm_rich()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n    >>> task = object()\n    >>> col = FractionColumn()\n    >>> print(col.render(task))\n    None/None\n    '
        list_0 = [str_0]
        tqdm_rich_0 = module_0.tqdm_rich(*list_0)
    except BaseException:
        pass