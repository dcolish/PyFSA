class DFA(object):
    empty_state = dict(inital=False,
                       final=False,
                       transisions=[])

    def __init__(self, states, alphabet):
        self.states = states
        for key, value in self.states.items():
            if value['initial']:
                self.STATE = self.states[key]


        self.alphabet = alphabet

    def read_one(self, str_input):
        if str_input not in self.alphabet:
            return self.empty_state

        self.STATE = self._step_over_states(str_input)
        return self.STATE

    def _step_over_states(self, str_input):

        for state, symbol in self.STATE['transitions']:
            if symbol in str_input:
                return self.states[state]
