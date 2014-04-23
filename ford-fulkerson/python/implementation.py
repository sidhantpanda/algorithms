import datetime
from ford_fulkerson import *

g = FlowNetwork()
for v in "sopqrt":
    g.add_vertex(v)
g.add_edge('s','o',3)
g.add_edge('s','p',3)
g.add_edge('o','p',2)
g.add_edge('o','q',3)
g.add_edge('p','r',2)
g.add_edge('r','t',3)
g.add_edge('q','r',4)
g.add_edge('q','t',2)
a = datetime.datetime.now()
print "Max Flow: ",g.max_flow('s','t')
b = datetime.datetime.now()
print "Time taken: ",(b-a)