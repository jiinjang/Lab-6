
import lab6


def test_intro_to_df(capsys):
    data = {"age": [20, 21, 22], "score": [80, 90, 100]}

    lab6.intro_to_df(data)
    result = capsys.readouterr().out

    assert "age" in result
    assert "score" in result
    assert "mean" in result


def test_intro_to_roi(capsys):
    lab6.intro_to_roi()
    result = capsys.readouterr().out

    assert "major" in result
    assert "19" in result
    assert "G015855" in result


def test_comparison_cat(capsys):
    lab6.comparison_cat("institution_tier")
    result = capsys.readouterr().out

    assert "mid_tier" in result
    assert "top_public" in result


def test_comparison_num(capsys):
    lab6.comparison_num("gpa")
    result = float(capsys.readouterr().out.strip())

    expected = lab6.df["gpa"].corr(lab6.df["net_roi_usd"])

    assert result == expected
