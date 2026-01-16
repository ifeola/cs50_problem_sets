from seasons import convert
import sys

def test_one():
	assert convert("2025-01-02") == "Five hundred twenty-five thousand, six hundred minutes"
	assert convert("2024-01-02") == "One million, fifty-two thousand, six hundred forty minutes"