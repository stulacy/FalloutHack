# FalloutHack
Solver for the hacking minigames in Fallout 3 and Fallout New Vegas, written in Python.


Simply run the solver by calling

```
python terminal_hack.py <word1> <word2> ... <wordn>
```

It will provide an initial guess, asking you to input how many letters were correct. It then refines its prediction and the process iterates until the word has been solved. It so far has not failed to guess a word in either of my playthroughs in both Fallout 3 and Fallout New Vegas, including terminals requiring a science skill of 75 to hack.

**NB: Code only runs under Python 3**
