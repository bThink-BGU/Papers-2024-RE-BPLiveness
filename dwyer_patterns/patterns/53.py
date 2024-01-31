from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!q || G (!p || (s & !z & X(!z U t))))"
variables_names = ["s", "t", "z", "p", "q"]

@b_thread
def pattern():
    """
    Kind: Constrained Chain: s,t without z responds to p
    Scope: After q
    LTL:
       G (!q || G (!p || (s && !z && X(!z U t))))
    """
    pass
