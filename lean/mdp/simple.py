import lean

# Tactics
tac_intro1 = lean.mk_constant(lean.name(lean.name("tactic"), "intro1"))

class SimpleLeanMDP(object):

    def __init__(self, goal_type):
        """
        Create an MDP to interact with Lean.

        Parameters
        ----------
        goal_type: lean.expr
            The type defining the statement we want to prove.
        """
        self.env = lean.import_modules(["/usr/local/lib/lean/library"],
                                       [lean.name("init")], 100000)

        options = lean.options()
        theorem_name = lean.name("random_theorem")
        local_context = lean.local_context()
        metavar_context = lean.metavar_context()

        deq_state = lean.defeq_can_state()
        tactic_user_state = lean.tactic_user_state()

        goal = metavar_context.mk_metavar_decl(local_context, goal_type)
        goals = lean.list_expr(goal, lean.list_expr())

        self.state = lean.tactic_state(self.env, options, theorem_name,
                                       metavar_context, goals, goal, deq_state,
                                       tactic_user_state)

    def run_tactic(self, tactic, args):
        ls = lean.list_name()
        r = lean.run_tactic(self.state, tactic, ls, args)
        return r.value() if r.is_some() else None

    def print_goals(self):
        context = self.state.mctx()
        metavar_decls = [context.get_metavar_decl(g) for g in self.state.goals()]
        for i, metavar_decl in enumerate(metavar_decls):
            print("goal " + str(i) + ": " + str(metavar_decl.get_type()))

    def act(self, tactic, args):
        """
        Return list of possible actions.
        """
        result, self.state = self.run_tactic(tactic, args)
