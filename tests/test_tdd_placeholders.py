import pytest

@pytest.mark.xfail(reason="TDD placeholder: publish adapter not implemented yet", strict=True)
def test_publish_social_writes_audit_log():
    # Future behavior: publishing a post should write an audit log record
    assert False, "Not implemented yet (TDD placeholder)"
