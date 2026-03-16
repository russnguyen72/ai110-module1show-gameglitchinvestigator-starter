from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_win_on_first_attempt():
    # Winning on attempt 1 should give 100 - 10*1 = 90 points
    assert update_score(0, "Win", 1) == 90


def test_win_on_later_attempt():
    # Winning on attempt 5 should give 100 - 10*5 = 50 points
    assert update_score(0, "Win", 5) == 50


def test_win_score_minimum():
    # At attempt 10+, the formula drops below 10, so the minimum of 10 is applied
    assert update_score(0, "Win", 10) == 10
    assert update_score(0, "Win", 50) == 10


def test_win_adds_to_existing_score():
    assert update_score(100, "Win", 1) == 190


def test_too_high_deducts_points():
    assert update_score(50, "Too High", 1) == 45


def test_too_high_deducts_on_even_attempt():
    # Even attempts should also deduct, not reward
    assert update_score(50, "Too High", 2) == 45


def test_too_low_deducts_points():
    assert update_score(50, "Too Low", 1) == 45


def test_too_high_and_too_low_deduct_equally():
    # Both wrong-guess outcomes should penalize the same amount
    assert update_score(100, "Too High", 3) == update_score(100, "Too Low", 3)


def test_unknown_outcome_does_not_change_score():
    assert update_score(75, "Unknown", 1) == 75


def test_decimal_input_rejected():
    ok, _, err = parse_guess("1.9")
    assert not ok
    assert "whole number" in err.lower()


def test_decimal_zero_rejected():
    ok, _, _ = parse_guess("5.0")
    assert not ok


def test_scientific_notation_rejected():
    ok, _, _ = parse_guess("1e5")
    assert not ok


def test_scientific_notation_with_decimal_rejected():
    ok, _, _ = parse_guess("1.5e2")
    assert not ok


def test_out_of_range_too_low():
    ok, _, err = parse_guess("-5", 1, 20)
    assert not ok
    assert "between" in err


def test_out_of_range_too_high():
    ok, _, err = parse_guess("999", 1, 20)
    assert not ok
    assert "between" in err


def test_in_range_valid():
    ok, val, _ = parse_guess("10", 1, 20)
    assert ok
    assert val == 10


def test_no_range_check_without_params():
    # Without low/high args, out-of-range values still parse successfully
    ok, val, _ = parse_guess("999")
    assert ok
    assert val == 999
