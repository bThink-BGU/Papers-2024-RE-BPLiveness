from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (((X(!r U (t & F p)) || !(s & X(!r U t))) U r) || !(q & F r))"
variables_names = ["s", "t", "p", "q", "r"]



@b_thread
def pattern():
    """
    Kind: Response Chain: p responds to s,t
    Scope: Between q and r
    LTL:
       G (((X(!r U (t && F p)) || !(s && X(!r U t))) U r) || !(q && F r))
    """
    pass