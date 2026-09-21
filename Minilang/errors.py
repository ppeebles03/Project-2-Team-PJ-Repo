class MiniLangError(Exception):
    """Base class for all MiniLang errors."""
    pass


class LexicalError(MiniLangError):
    """Error found while breaking source code into tokens."""
    pass


class SyntaxError(MiniLangError):
    """Error found while parsing the program."""
    pass


class SemanticError(MiniLangError):
    """Error found during semantic analysis."""
    pass


class RuntimeError(MiniLangError):
    """Error found while executing the program."""
    pass