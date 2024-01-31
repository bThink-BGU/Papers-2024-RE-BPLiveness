from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!p || F (s & !z & X(!z U t)))"
variables_names = ["s", "t", "z", "p"]

@b_thread
def pat_51():
    """
    Kind: Constrained Chain: s,t without z responds to p
    Scope: Globally
    LTL:
       G (!p || F (s && !z && X(!z U t)))
    """
    pass