"""Command line tool to template the structure of a new ansible role."""

__author__ = "Robert Kaussow"
__project__ = "ansible-role"
__version__ = "0.1.0"
__license__ = "MIT"
__maintainer__ = "Robert Kaussow"
__email__ = "mail@geeklabor.de"
__status__ = "Production"


from ansiblerole.utils import setup_logging
from ansiblerole.utils import Settings


defaults = Settings()
setup_logging(log_level=defaults.log_level)
