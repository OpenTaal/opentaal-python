'''Debug Pytest in IDE.'''

from pdb import set_trace
from pytest import main

set_trace()  # pylint:disable=forgotten-debug-statement
main()
