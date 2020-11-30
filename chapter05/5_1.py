def isNum(string: str) -> bool:
    expression = eval(string)
    if type(expression) == int or type(expression) == float or type(expression) == complex:
        return True
    else:
        return False


test_string = "5.0+3j"
ret = isNum(test_string)
print(ret)
