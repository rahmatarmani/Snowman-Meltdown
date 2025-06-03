# Expanded Snowman ASCII Art with smoother transitions
STAGES = [
    # Stage 0: Full snowman
    """
       _____  
      /_____\\ 
     |  O O  |
     |   ^   |
     |  \\_/  |
     |_______|
    """,
    # Stage 1: Lost base
    """
       _____  
      /_____\\ 
     |  O O  |
     |   ^   |
     |  \\_/  |
    """,
    # Stage 2: Lost torso
    """
       _____  
      /_____\\ 
     |  O O  |
     |   ^   |
    """,
    # Stage 3: Head melting
    """
       _____  
      /_____\\ 
     |  O O  |
    """,
    # Stage 4: Almost gone
    """
       _____  
      /_____\\ 
    """,
    # Stage 5: Completely melted
    """
       ~ ~  
      ~~~~~ 
    """
]

MAX_MISTAKES = len(STAGES) - 1