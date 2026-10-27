from logic_utils import (
    attempts_left,
    check_guess,
    get_range_for_difficulty,
    new_game_state,
)


# check_guess returns (outcome, message), so the starter tests unpack the tuple.
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


# --- Bug: hints were reversed -------------------------------------------------
def test_too_high_guess_tells_player_to_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_guess_tells_player_to_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_comparison_is_numeric_not_alphabetical():
    # "9" > "50" as strings, but 9 is a low guess for a secret of 50.
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"


# --- Bug: New Game didn't fully reset / off-by-one attempts -------------------
def test_new_game_state_is_fully_reset():
    state = new_game_state(1, 100)
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []


def test_new_game_secret_respects_difficulty_range():
    low, high = get_range_for_difficulty("Easy")
    for _ in range(200):
        assert low <= new_game_state(low, high)["secret"] <= high


def test_full_attempts_available_before_first_guess():
    # Normal allows 8 attempts; none should be used up before the first guess.
    assert attempts_left(8, new_game_state(1, 100)["attempts"]) == 8


def test_attempts_left_never_negative():
    assert attempts_left(8, 9) == 0
