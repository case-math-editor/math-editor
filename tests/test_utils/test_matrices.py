import pytest

from math_editor.utils.matrices import is_present_in_matrix


TEST_IS_PRESENT_IN_MATRIX_DATA = (
    # test args scheme: "matrix,target,result"
    ([[1]], 1, True),
    ([[1]], 10, False),
    ([[1]], -1, False),
    ([[1, 3], [4, 5]], 5, True),
    ([[1, 3], [4, 5]], 10, False),
)


@pytest.mark.utils
@pytest.mark.parametrize("matrix,target,result", TEST_IS_PRESENT_IN_MATRIX_DATA)
def test_is_present_in_matrix(
    matrix: list[list[int]], target: int, result: bool
) -> None:

    assert is_present_in_matrix(matrix, target) == result
