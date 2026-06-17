from ToolVerse.json_tools import jsontools

jt = jsontools()


def test_validate_json():
    assert jt.validate_json('{"name":"Ayaz"}') is True


def test_invalid_json():
    assert jt.validate_json('{"name":}') is False


def test_json_to_string():
    data = {"name": "Ayaz"}
    result = jt.json_to_string(data)

    assert isinstance(result, str)


def test_string_to_json():
    data = '{"name":"Ayaz"}'

    result = jt.string_to_json(data)

    assert result["name"] == "Ayaz"
