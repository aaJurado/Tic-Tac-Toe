
from board import Board


class LoggingBoard(Board):
    """A Board subclass that records moves made by players and prints a log when the game ends."""

    def __init__(self):
        """Initialize the board and a log list."""
        super().__init__()
        self.log = []

    def claim_square(self, player, index):
        """Claim a square and record the player's move in the log."""
        # Call the parent method to claim the square
        super().claim_square(player, index)
        # Add an entry to the log
        self.log.append(f"{player.name} selects square {index}")

    def get_winner(self):
        """Determine if there is a winner, log the winner if found, and return the result."""
        winner = super().get_winner()
        if winner:
            self.log.append(f"{winner.name} wins")
        return winner

    def game_over(self):
        """When the game ends, print the move log and return the result."""
        over = super().game_over()
        if over:
            print("\nGame log:")
            for entry in self.log:
                print(entry)
        return over
