class Colors:
    """
    Class to derive colors for use in stdout
    """
    def __init__(self) -> None:
        # TODO: make these colors depend on the system's detected colorscheme
        self.BOLD = '\033[1m'
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.RESET = '\033[0m'
