from logic_utils import check_guess, update_score

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
