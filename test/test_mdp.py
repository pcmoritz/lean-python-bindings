import lean
from lean.mdp.simple import SimpleLeanMDP
import pytest

ex_falso_quod_libet = lean.mk_arrow(lean.mk_constant(lean.name("false")), lean.mk_constant(lean.name("true")))
tmp = lean.mk_pi(lean.name("m"), lean.mk_constant(lean.name("nat")), lean.mk_app(lean.mk_constant(lean.name("even")), lean.mk_var(0)))
even_plus_even_is_even = lean.mk_app(lean.mk_constant(lean.name("even")), lean.mk_constant(lean.name("m")))

mdp = SimpleLeanMDP(ex_falso_quod_libet)

mdp.print_goals()

import IPython
IPython.embed()
