# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

There were multiple things that were broken when I first ran the game. 
One bug was that, when looking at the hints, the hints were reversed. In other words, if the guess was too low, the hint would say to go lower, and if the guess was too high, the hint would say to go higher. This is opposite from the expected behavior of the hint, as the player would only make guesses further away from the answer.
Another bug that was present is that the New Game button does not reset the game if the game is already finished. When the game finishes, it does not allow any new guesses to be checked. When pressing the "New Game" button, the user would expect to be able to input new attempts, but the program does not accept any new inputs as guesses towards the secret.
A final bug that was noticed is that the difficulty selector names are not representative of the actual difficulty, as the user would expect Hard to have a larger number range than Normal, which is not the case as Hard has a range of 1 to 20 and Normal has a range of 1 to 100.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI tool that I used on this project was Claude Code. 
One example of an AI suggestion that was correct was changing whether "Too High!" or "Too Low!" was returned, dependent on if the guess was truly higher or lower than the secret number, which was verified during playing the games and the tests in test_game_logic.py.
One example of an AI suggestion that was misleading was that Claude found the remaining bugs in app.py, as it did not consider the case where the score did not reset during a New Game, which I tested by doing multiple games and seeing in the debug menu that the score from the previous game would affect the new game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

One way I decide whether a bug was really fixed or not was by testing it by playing the game itself, judging whether the functionality was as intended or not. This showed me that, even if the initial fix was not completely correct, I was on the right path. The AI helped me understand the poorly written initial test as it showed me that the output of the function was not compatible with how the original test cases for the check_guess function, as it was comparing a string to a tuple.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing in the original app because it would randomly typecast the secret to a string, which would trip a safeguard in the code and cause a new random secret number to be generated. Streamlit reruns trigger everytime something on the page is modified, and executes the entire code for any single change, allowing the page to stay consistent no matter the change. A session state is the how the current Streamlit page looks like for the current execution, with it possibly changing for any given rerun. A change that I made that finally gave the game a stable secret number was removing the branch that would execute `secret = str(st.session_state.secret)`, preventing the safeguard for a not found secret number from triggering during a game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit that I want to reuse in future labs and projects is to cross-reference the changes AI create to other code in the codebase, to trace exactly why a certain piece of code is designed and what its new functionality may be, and ensure that the change is actually correct. I also make sure to tell the AI not to modify functions just to make it pass a certain test, or design faulty tests that would incorrectly assert true at a glance. One thing I would do differently is definitely look harder at AI's output, as it can be unreliable at times, especially for big sweeping changes.
This project changed the way I think about AI generated code as something extremely powerful, but something that also needs a lot of specific guidance to work properly, as it does not catch everything possible and can also make mistakes, like a human.