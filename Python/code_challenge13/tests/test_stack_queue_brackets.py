from stack_queue_brackets.stack_queue_brackets import validate_brackets



def test_stack_queue_brackets1():
    assert validate_brackets("{}") == True

def test_stack_queue_brackets2():
    assert validate_brackets("{}(){}") == True

def test_stack_queue_brackets3():
    assert validate_brackets("()[[Extra Characters]]") == True

def test_stack_queue_brackets4():
    assert validate_brackets("(){}[[]]") == True

def test_stack_queue_brackets5():
    assert validate_brackets("{}{Code}[Fellows](())") == True

def test_stack_queue_brackets6():
    assert validate_brackets("{[({}]") == False

def test_stack_queue_brackets7():
    assert validate_brackets("(](") == False

def test_stack_queue_brackets8():
    assert validate_brackets("{(})") == False