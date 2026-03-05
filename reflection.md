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

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
