# Automatically generated by Pynguin.
import tornado.queues as module_0

def test_case_0():
    queue_empty_0 = module_0.QueueEmpty()

def test_case_1():
    bool_0 = False
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    queue_iterator_0 = module_0._QueueIterator(bool_0)

def test_case_2():
    queue_0 = module_0.Queue()

def test_case_3():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()

def test_case_4():
    awaitable_0 = None
    queue_0 = module_0.Queue()
    bool_0 = queue_0.empty()
    set_0 = {awaitable_0, awaitable_0, awaitable_0, awaitable_0}
    str_0 = "pW@C'+`iS"
    queue_iterator_0 = module_0._QueueIterator(str_0)
    queue_1 = module_0.Queue()
    var_0 = queue_1.__aiter__()
    queue_iterator_1 = module_0._QueueIterator(set_0)

def test_case_5():
    var_0 = None
    queue_0 = module_0.Queue()
    queue_0.put_nowait(var_0)

def test_case_6():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__repr__()

def test_case_7():
    priority_queue_0 = module_0.PriorityQueue()

def test_case_8():
    lifo_queue_0 = module_0.LifoQueue()