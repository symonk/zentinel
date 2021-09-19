import pytest

from zentinel import main

pytestmark = pytest.mark.skip  # github won't like me running these unstubbed on their infra!


def test_default_target(capsys):
    res = main(("--ports", "0-1"))
    out, err = capsys.readouterr()
    assert "Launching port scan against: localhost" in out
    assert not res


def test_custom_target(capsys):
    res = main(("--ports", "0-1", "--target", "127.0.0.1"))
    out, err = capsys.readouterr()
    assert "Launching port scan against: 127.0.0.1" in out
    assert not res
