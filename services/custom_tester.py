class Tester():
    def basic_test(self, test_name, expect, actual):
        if expect == actual:
            print(f'\033[32m{test_name}: PASS\033[0m')
        else:
            print(f'\033[31m{test_name}: FAIL\033[0m')
            print(f'expect: {expect}')
            print(f'actual: {actual}')