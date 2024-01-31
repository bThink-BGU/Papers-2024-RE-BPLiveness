from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!q || ((!p || (!r U (!r & s && !z & X((!r & !z) U t)))) U (r || G (!p || (s & !z & X(!z U t))))))"
variables_names = ["s", "t", "z", "p", "q", "r"]


@b_thread
def pattern():
    """
    Kind: Constrained Chain: s,t without z responds to p
    Scope: After q until r
    LTL:
       G (!q || ((!p || (!r U (!r && s && !z && X((!r && !z) U t)))) U (r || G (!p || (s && !z && X(!z U t))))))
    """
    pass