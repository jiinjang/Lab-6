
import io
from contextlib import redirect_stdout

import lab6


def test_intro_to_df():
    data = {"age": [20, 21, 22], "score": [80, 90, 100]}

    output = io.StringIO()
    with redirect_stdout(output):
        lab6.intro_to_df(data)

    result = output.getvalue()
    assert "age" in result
    assert "score" in result
    assert "mean" in result


def test_intro_to_roi():
    output = io.StringIO()
    with redirect_stdout(output):
        lab6.intro_to_roi()

    result = output.getvalue()
    assert "major" in result
    assert "19" in result
    assert "G015855" in result


def test_comparison_cat():
    output = io.StringIO()
    with redirect_stdout(output):
        lab6.comparison_cat("institution_tier")

    result = output.getvalue()
    assert "mid_tier" in result
    assert "top_public" in result


def test_comparison_num():
    output = io.StringIO()
    with redirect_stdout(output):
        lab6.comparison_num("gpa")

    result = float(output.getvalue().strip())
    expected = lab6.df["gpa"].corr(lab6.df["net_roi_usd"])

    assert result == expected
