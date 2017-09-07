# 07.09.2017
class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ss_settings):
        """Initialize statistics."""
        self.ss_settings = ss_settings
        self.reset_stats()

        # Start game in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ss_settings.bullet_miss_limit = 3
