from sys import argv

from fsas import FSA

try:
    input_str = argv[1]
except IndexError, e:
    input_str = []

alphabet = ['a', 'b']

states = dict(q0=dict(initial=True,
                      final=True,
                      transitions=[('q1', 'a'), ('q0', 'b')]),
              q1=dict(initial=False,
                      final=False,
                      transitions=[('q0', 'a'), ('q1', 'b')]))

dfa = FSA(states, alphabet)
for x in input_str:
    dfa.read_one(x)

dfa.print_accept_state()
