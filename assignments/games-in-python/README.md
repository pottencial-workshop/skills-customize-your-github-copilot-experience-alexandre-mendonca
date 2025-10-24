
# 📘 Assignment: Hangman Game Challenge

## Objetivo

Desenvolva um jogo Hangman (forca) em linha de comando para praticar manipulação de strings, laços, condicionais e entrada do usuário. O jogador deve adivinhar uma palavra letra a letra antes de ficar sem tentativas.

## Tarefas

### 🛠️	Build the Hangman Game

#### Description
Implemente um jogo Hangman jogável no terminal. O programa deve escolher uma palavra aleatória de uma lista, receber palpites de letras do jogador e mostrar o progresso atual da palavra até o jogador ganhar ou perder.

#### Requirements
Completed program should:

- Randomly select words from a predefined list.
- Accept single-letter guesses (case-insensitive) and show current progress in _ _ _ format.
- Track and display the number of incorrect guesses remaining.
- Avoid penalizing repeated guesses of the same letter and display the list of letters already guessed.
- End when the word is fully guessed or attempts are exhausted, showing a clear win or lose message.
- Be runnable from the command line (e.g., python3 hangman.py) and include a small, commented starter list of words.

#### Example session

```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Progress: _ a _ _ _
Incorrect guesses remaining: 5
Guessed letters: a
```

---

Siga o template do curso ao submeter: inclua seu código em `starter-code.py` ou outro arquivo indicado dentro desta pasta da atribuição.
