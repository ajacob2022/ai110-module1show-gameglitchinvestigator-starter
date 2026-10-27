# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - Hints were backwards
  - Answer was shown one round early
  - New game button did not work

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|New Game button| Start a new game | resets turn count but does not allow user to play again | none
|'67'| should have said lower because the secret was 32 | hint said it was higher | none
|'99'| should have said lower because the secret was 32 | hint said it was higher | none

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
-- Claude was used. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
-- AI pointed out that there were two causes for the backwards hints.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
--AI suggested a complete redesign of the game, but I did not find it necessary for a simple bug fix

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
-- By playing the game multiple times and testing the bug with every input I could think of.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
-- I ran pytest on the new tests in tests/test_game_logic.py. My first run failed with ModuleNotFoundError: No module named 'logic_utils', because pytest couldn’t find the project root, and adding a pytest.ini with pythonpath = . fixed it so all 10 tests passed.
- Did AI help you design or understand any tests?
-- AI helped me design AND understand the pytest.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
--anytime a user does anything atreamlit runs your whole program from the top amd any variables or memory is forgotten. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
