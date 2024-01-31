from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

# spec = "G (X (t & F p) | ! (s & X t))"
# variables_names = ["s", "t", "p"]

@b_thread
def patterns():
    """
    Kind: Response Chain: p responds to s,t
    Scope: Globally
    LTL:
       G (XF (t && F p) || !(s && XF t))
    """
    while True:
        yield {waitFor: s}
        yield {waitFor: t}
        yield {waitFor: p, mustFinish: True}