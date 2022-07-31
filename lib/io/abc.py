from abc import ABC, abstractmethod


class FileFormatType(ABC):
    pass


class FormatTokenType(ABC):
    pass


class FormatParserABC(ABC):
    RE_NUMBER_PATTERN = "\d+(\.+\d*)?"
    RE_INTEGER_PATTERN = "\d+"
    RE_FLOAT_PATTERN = "\d+\.+\d*"


class FormatCompilerABC(ABC):
    pass


class FileReaderABC(ABC):
    pass


class FileWriterABC(ABC):
    pass
