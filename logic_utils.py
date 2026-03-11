# FIX: Refactored game logic into logic_utils.py

# FIX: Made the Hard difficulty actually harder by increasing the range to 1-200 instead of 1-50.
# FIXME: (get_range_for_difficulty) The range for the "Hard" difficulty is actually smaller than the "Normal" difficulty, making it easier instead of harder. This is a glitch that needs to be fixed.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

# FIX: Ensured that the check_guess function correctly told the user to go higher when their guess is too low, and to go lower when their guess is too high. This was a glitch that has been fixed.
# FIX: Fixed the TypeError fallback branch which also had swapped hint messages for "Too High" and "Too Low".
# FIXME: (check_guess) The function incorrectly tells the user to go higher when their guess is too high, and to go lower when their guess is too low. This is a glitch that needs to be fixed.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


# FIX: Win score calculation used (attempt_number + 1) which over-penalized by one extra attempt; changed to attempt_number.
# FIX: Too High outcome incorrectly awarded +5 points on even attempts; wrong guesses should always deduct 5 points.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
