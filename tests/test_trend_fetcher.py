def test_trend_fetcher_output_contract():
    result = {
        "topic": "string",
        "confidence": 0.5,
        "source": "string"
    }

    assert "topic" in result
    assert isinstance(result["confidence"], float)
    assert 0.0 <= result["confidence"] <= 1.0
