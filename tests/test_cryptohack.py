from XOR_starter import xor


def test_xor_starter():
    assert "crypto{" + xor("label") + "}" == "crypto{aloha}"
