import lean

env = lean.import_modules(["/usr/local/lib/lean/library"], [lean.name("init")], 100000)

options = lean.options()
decl_name = lean.name("my_theorem")

lctx = lean.local_context()
mctx = lean.metavar_context()

goal_type = lean.mk_arrow(lean.mk_constant(lean.name("true")), lean.mk_constant(lean.name("false")))

goal = mctx.mk_metavar_decl(lctx, goal_type)
goals = lean.list_expr(goal, lean.list_expr()) # TODO(dhs): python lists

deq_state = lean.defeq_can_state()
tustate = lean.tactic_user_state()

tstate = lean.tactic_state(env, options, decl_name, mctx, goals, goal, deq_state, tustate)

ls = lean.list_name()

tactic = lean.mk_constant(lean.name(lean.name("tactic"), "intro1"))

new_tstate = lean.run_tactic(tstate, tactic, ls)

print new_tstate
