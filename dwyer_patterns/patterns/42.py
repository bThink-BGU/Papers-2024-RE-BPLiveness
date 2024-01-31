from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "((X(!r U (t & F p)) || !(s & X(!r U t))) U r) || !F r"
variables_names = ["s", "t", "p", "r"]


@b_thread
def pattern():
    """
    Kind: Response Chain: p responds to s,t
    Scope: Before r
    LTL:
       ((X(!r U (t && F p)) || !(s && X(!r U t))) U r) || !F r
    """
    pass