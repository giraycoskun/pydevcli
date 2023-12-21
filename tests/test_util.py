from pydevcli.util.secrets import create_application_secret


def test_create_application_secret():
    """
    Test create_application_secret
    """
    assert len(create_application_secret()) == 64
    assert len(create_application_secret(nb_bytes=16)) == 32