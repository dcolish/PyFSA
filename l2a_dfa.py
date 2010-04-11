from sys import argv

from fsas import DFA

input_str = argv[1]

alphabet = ['a', 'b']

states = dict(q0=dict(initial=True,
                      final=True,
                      transitions=[('q1', 'a'), ('q0', 'b')]),
              q1=dict(initial=False,
                      final=False,
                      transitions=[('q0', 'a'), ('q1', 'b')]))


dfa = DFA(states, alphabet)

for x in input_str:
    current_state = dfa.read_one(x)

if current_state['final']:
    print 'ACCEPTED'
else:
    print 'REJECTED'
