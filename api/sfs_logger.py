from api.sfs_colorama import TextColor


class Logger:
    def __init__(self):
        self.default_color = TextColor.DEFAULT

    def info(self, message: str, sep: str = " ", end: str = "\n") -> None:
        print(f"{TextColor.CYAN}[INFO]:{self.default_color} {message}", sep=sep, end=end)

    def error(self, message: str, sep: str = " ", end: str = "\n") -> None:
        print(f"{TextColor.YELLOW}[ERROR]:{self.default_color} {message}", sep=sep, end=end)

    def fatal(self, message: str, sep: str = " ", end: str = "\n") -> None:
        print(f"{TextColor.LIGHT_RED}[FATAL]:{self.default_color} {message}", sep=sep, end=end)
