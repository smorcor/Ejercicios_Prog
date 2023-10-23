import pytest
from prueba1 import mayor

def test_mayor():
    assert mayor(1, 1) == 0
    assert mayor(0, 0) == 0
    assert mayor(100, -100) == 100


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 1, 0),
        (0, 0, 0),
        (100, -100, 100),
        (-15, -1, -1),
        (-3, 8, 8),
        (9, mayor(-1, -2), 9)
    ]
)
def test_mayor_params(input_n1, input_n2, expected):
    assert mayor(input_n1, input_n2) == expected