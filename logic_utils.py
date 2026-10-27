"""Game logic for the number guessing game.

Kept free of Streamlit imports so it can be unit-tested with plain pytest.
"""
import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
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


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: the hint messages were reversed ("Too High" said Go HIGHER). Moved this
    # function into logic_utils.py and swapped them, using Claude (agent mode).
    # Also removed the old try/except TypeError string-comparison fallback; app.py
    # no longer passes the secret as a str, so plain int comparison is correct.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def new_game_state(low: int, high: int):
    """Return a fresh game's session values, with the secret drawn from [low, high]."""
    # FIX: "New Game" only reset attempts and picked the secret from 1-100 no matter
    # the difficulty; score, history and status were left over, so a finished game
    # stayed locked. All of that now resets here in one place (found with Claude).
    # FIX: attempts used to start at 1, so "Attempts left" was off by one and the
    # game ended (revealing the secret) one guess early. It now starts at 0.
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }


def attempts_left(attempt_limit: int, attempts: int):
    """How many guesses remain (never negative)."""
    return max(attempt_limit - attempts, 0)
