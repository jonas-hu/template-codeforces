from {{cookiecutter.problem_name}} import main, run
import pytest


def test_main(monkeypatch, capfd):
    inputs = iter(["3", "1", "2", "3"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = "2\n4\n6\n"

    main()

    out, err = capfd.readouterr()
    assert expected_output == out


@pytest.mark.parametrize(
    "value, expected_result",
    [
        (1, 2),
        (2, 4),
        (5, 10),
    ],
)
def test_run(value, expected_result):
    result = run(value)
    assert expected_result == result
