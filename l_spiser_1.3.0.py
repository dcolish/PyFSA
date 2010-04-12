from sys import argv

from fsas import FSA

input_str = argv[1]

alphabet = ['0', '1']

states = dict(q0=dict(initial=True,
                      final=False,
                      transitions=[('q0', '0'), ('q0', '1'), ('q1', '1')]),
              q1=dict(initial=False,
                      final=False,
                      transitions=[('q2', '0'), ('q2', '1')]),
              q2=dict(initial=False,
                      final=False,
                      transitions=[('q3', '0'), ('q3', '1')]),
              q3=dict(initial=False,
                      final=True,
                      transitions=[]))

nfa = FSA(states, alphabet)

for x in input_str:
    nfa.read_one(x)

if nfa.in_final:
    print 'ACCEPTED'
else:
    print 'REJECTED'

