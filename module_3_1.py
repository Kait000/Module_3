def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [i.lower() for i in list_to_search]
    if string in list_to_search:
        return True
    else:
        return False


calls = 0
print(string_info('GitHub.com'))
print(string_info('Python'))
print(is_contains('GitHub', ['Python', 'Delphi', 'Github', 'php']))
print(is_contains('bool', ['List', 'Tuple', 'Set', 'Dictionary']))
print(calls)
