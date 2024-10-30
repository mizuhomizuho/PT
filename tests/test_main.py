import pytest
from contextlib import nullcontext as does_not_raise


# tests/test_main.py::TestMain::test_main[1-2-0.5] FAILED
# tests/test_main.py::TestMain::test_main[5--1--5_0] FAILED
# tests/test_main.py::TestMain::test_main[5--1--5_1] PASSED
class TestMain:
    # @pytest.mark.parametrize(['x', 'y', 'res'])
    @pytest.mark.parametrize('x, y, res', [
        (1, 2, 0.5),
        (5, -1, -5),
        (5, '-1', -5),
    ])
    def test_main(self, x, y, res):
        with pytest.raises(TypeError):
            assert x / y == res


# def test_foo3():
#     try:
#         foo(7)
#     except MyError:
#         pytest.fail("Unexpected MyError ..")


# @pytest.mark.parametrize(
#     "example_input,expectation",
#     [
#         (3, does_not_raise()),
#         (2, does_not_raise()),
#         (1, does_not_raise()),
#         (0, pytest.raises(ZeroDivisionError)),
#     ],
# )
# def test_division(example_input, expectation):
#     with expectation:
#         assert (6 / example_input) is not None


# @pytest.mark.parametrize(
#     "example_input,expectation,message",
#     [
#         (3, pytest.raises(MyError), ERROR1),
#         (11, pytest.raises(MyError), ERROR2),
#         (7, does_not_raise(), None),
#     ],
# )
# def test_foo(example_input, expectation, message):
#     with expectation as e:
#         foo(example_input)
#     assert message is None or message == str(e)