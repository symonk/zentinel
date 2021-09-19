import pytest

from zentinel import main

pytestmark = pytest.mark.skip  # github won't like me running these unstubbed on their infra!


def test_ports_are_correct(capsys) -> None:
    main(("--ports", "10-20"))
    out, err = capsys.readouterr()
    assert "Executing coroutines for ports in range: 10 -> 19" in out
    assert not err


def test_invalid_port_regex(capsys) -> None:
    with pytest.raises(SystemExit):
        result = main(("--ports", "x=y"))
        assert result == 2
    _, err = capsys.readouterr()
    assert "--ports should be a hyphen separated range of ports" in err
