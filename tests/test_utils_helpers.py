import datetime
import pytest
from backend.src.utils import helpers


def test_generate_response_formats_message():
    assert helpers.generate_response("hi") == "Response: hi"


def test_validate_input_accepts_non_empty():
    assert helpers.validate_input("data") is True


def test_validate_input_rejects_empty():
    with pytest.raises(ValueError):
        helpers.validate_input("")


def test_format_timestamp_returns_string():
    ts = datetime.datetime(2020, 1, 2, 3, 4, 5)
    assert helpers.format_timestamp(ts) == "2020-01-02 03:04:05"


def test_log_event_and_handle_error_prints(capsys):
    helpers.log_event("something")
    helpers.handle_error("bad")
    captured = capsys.readouterr()
    assert "Event: something" in captured.out
    assert "Error: bad" in captured.out
