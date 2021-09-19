from zentinel import main


def test_ports_are_correct(capsys):
    main(("--ports", "10-20"))
    out, err = capsys.readouterr()
    assert "Executing coroutines for ports in range: 10 -> 19" in out
    assert not err
