import timeit


def test_import_whole():
    import json


def test_import_part():
    from json import dumps


print("import_whole:", min(timeit.repeat(test_import_whole)), "s")
print("import_part:", min(timeit.repeat(test_import_part)), "s")
