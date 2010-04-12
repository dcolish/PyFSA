import warnings


class FSA(object):
    empty_state = dict(inital=False,
                       final=False,
                       transitions=[])
    EPSILON = 'epi'
    STATE = set()
    states = dict()

    def __init__(self, states, alphabet):
        self.states.update(states)
        for key, value in self.states.items():
            if value['initial']:
                self.STATE.add(key)

        if len(self.STATE) is not 1:
            warnings.warn("Your FSA has more than one initial state")

        self.alphabet = alphabet

    def read_one(self, str_input):
        if str_input not in self.alphabet:
            return self.empty_state

        self._step_over_states(str_input)
        return self.STATE

    def _step_over_states(self, symbol):
        state_set = set()
        for state in self.STATE:
            for trans_state, state_symbol in self.states[state]['transitions']:
                if state_symbol is symbol:
                    state_set.add(trans_state)
        self.STATE = state_set

    def _perform_eps_closure(self):
        self._step_over_states(self.EPSILON)

    @property
    def is_accepted(self):
        for state in self.STATE:
            if self.states[state]['final']:
                return True
            else:
                return False

    @property
    def current_state(self):
        return self.STATE

    def print_accept_state(self):
        if self.is_accepted:
            print "ACCEPTED"
        else:
            print "REJECTED"
