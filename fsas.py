class NFA(object):
    empty_state = dict(inital=False,
                       final=False,
                       transitions=[])

    def __init__(self, states, alphabet):
        self.states = states
        for key, value in self.states.items():
            if value['initial']:
                self.STATE = [self.states[key]]

        self.alphabet = alphabet

    def read_one(self, str_input):
        if str_input not in self.alphabet:
            return self.empty_state

        self.STATE = self._step_over_states(str_input)
        return self.STATE

    def _step_over_states(self, str_input):
        state_set = list()
        for state, symbol in self.STATE['transitions']:
            if symbol in str_input:
                state_set.append(self.states[state])

        return state_set


class DFA(NFA):

    @property
    def STATE(self):
        return self.DFA_STATE[0]

    @STATE.setter
    def STATE(self, value):
        self.DFA_STATE = value
