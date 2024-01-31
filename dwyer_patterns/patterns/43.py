from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!q || G (X(!t U (t & F p)) || !(s & XF t)))"
variables_names = ["s", "t", "p", "q"]


@b_thread
def pattern():
    """
    Kind: Response Chain: p responds to s,t
    Scope: After q
    LTL:
       G (!q || G (X(!t U (t && F p)) || !(s && XF t)))
    """
    pass