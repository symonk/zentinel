def test_default_target(run_zentinel, capsys):
    res = run_zentinel(("--ports", "0-1"))
    out, err = capsys.readouterr()
    assert "Launching port scan against: localhost" in out
    assert not res


def test_custom_target(run_zentinel, capsys):
    res = run_zentinel(("--ports", "0-1", "--target", "127.0.0.1"))
    out, err = capsys.readouterr()
    assert "Launching port scan against: 127.0.0.1" in out
    assert not res
