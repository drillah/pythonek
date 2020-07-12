import random
HANGMAN = (
    """
    -------
    |     |
    |
    |
    |
    |
    |
    |
    |
    --------------
    """,
    """
    -------
    |     |
    |     O
    |
    |
    |
    |
    |
    |
    --------------    
    """,
    """
    -------
    |     |
    |     O
    |    -+-
    |
    |
    |
    |
    |
    --------------    
    """,
    """
    -------
    |     |
    |     O
    |   /-+-
    |
    |
    |
    |
    |
    --------------    
    """,
    """
    -------
    |     |
    |     O
    |   /-+-/
    |
    |
    |
    |
    |
    --------------    
    """,
    """
    -------
    |     |
    |     O
    |   /-+-/
    |     |
    |
    |
    |
    |
    --------------    
    """,
    """
    -------
    |     |
    |     O
    |   /-+-/
    |     |
    |    /
    |   |
    |
    |
    --------------    
    """,
    """
    -------
    |     |
    |     O
    |   /-+-/
    |     |
    |    / |
    |   |  |
    |
    |
    --------------    
    """)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("NADUŻYWANY", "MAŁŻ", "GUMA", "TAFLA", "PYTHON")

word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Witaj w grze 'Szubienica'. Powodzenia!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystałeś już następujące litery:\n", used)
    print("\nBa razie zagadkowe słow wygląda tak:\n", so_far)