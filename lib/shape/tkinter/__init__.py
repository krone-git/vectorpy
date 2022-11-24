from .rectangle import *
from .rectangle import __all__ as __rectangleall__
from .oval import *
from .oval import __all__ as __ovalall__
from .line import *
from .line import __all__ as __lineall__
from .triangle import *
from .triangle import __all__ as __triangleall__

__all__ = (
    *__rectangleall__,
    *__ovalall__,
    *__lineall__,
    *__triangleall__
    )
