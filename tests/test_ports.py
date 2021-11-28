import pytest


def test_ports_are_correct(run_zentinel, capsys) -> None:
    run_zentinel(("--ports", "10-20"))
    out, err = capsys.readouterr()
    assert "Executing coroutines for ports in range: 10 -> 19" in out
    assert not err


def test_invalid_port_regex(run_zentinel, capsys) -> None:
    with pytest.raises(SystemExit):
        result = run_zentinel(("--ports", "x=y"))
        assert result == 2
    _, err = capsys.readouterr()
    assert "--ports should be a hyphen separated range of ports" in err


def test_exceeding_tcp_limit(run_zentinel, capsys):
    with pytest.raises(SystemExit):
        result = run_zentinel(("--ports", "300-75000"))
        assert result == 2
    _, err = capsys.readouterr()
    assert "TCP port limit is: 65535, it was exceeded by: 300-75000" in err
