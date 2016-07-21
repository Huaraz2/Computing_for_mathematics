import doctest
import os
import unittest


def load_tests(loader, tests, ignore):
    for root, dirs, files in os.walk("./_labsheets"):
        for f in files:
            if f.endswith(".md"):
                 tests.addTests(doctest.DocFileSuite(os.path.join(root, f),
                                                  optionflags=doctest.ELLIPSIS))

    return tests


if __name__ == '__main__':
    unittest.main()
