from graphviz import Digraph
dot = Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
print(dot.source)
#dot.render('test-output/round-table.gv', view=True)
#dot.node('A', 'King Arthur',
##shape="circle", style="filled", color = ".7 .3 1.0")
import random as rd

x = [ rd.randint(-100, 100) for i in range(1,30)]

def swap (x, i, j):
    tmp = x[i]
    x[i] = x[j]
    x[j] = tmp
    
def make_heap(x):
    for i in range(1,len(x)):
        node = x[i]
        current = i
        parent = (i-1)//2
        while( (current > 0) and (node > x[parent])):
            swap(x, current, parent)
            node = x[parent]
            current = parent
            parent = (parent-1) //2;
               
                
class heap_graph:  

    leaf_attr = {'shape' : "circle",
                 'style' :"filled",
                 'peripheries' :"1",
                 'fillcolor' : "lightgrey",
                 'fixedsize' : "true"}

    node_attr = {'shape' : "circle",
                 'style' :"filled",
                 'peripheries' :"1",
                 'fillcolor' : "white",
                 'fixedsize' : "true"}

    current_attr = {'shape' : "circle",
                 'style' :"filled",
                 'peripheries' :"1",
                 'fillcolor' : "lightgreen",
                 'fixedsize' : "true"}

    swap_attr = {'shape' : "circle",
                 'style' :"filled",
                 'peripheries' :"1",
                 'fillcolor' : "yellow",
                 'fixedsize' : "true"}

    def __init__(self, name, numbers):
        self.name = name
        self.heap = numbers
        
    def create_heap_graph(self, current =-1, swap=-1 ):
        heapdot = Digraph(comment =' Heap structure ')
        heapdot.format = 'png'
        for (i, node) in enumerate(self.heap):
            col = ""
            if (i == current):
                heapdot.node(str(i),str(node),**self.current_attr)
            elif (i == swap) :
                heapdot.node(str(i),str(node),**self.swap_attr)
            elif (i >= len(self.heap)//2):
                col = "lightgrey"
                heapdot.node(str(i),str(node),**self.leaf_attr)
        ##        heapdot.node(str(i),str(node),
        ##                 shape="circle",
        ##                 style="filled",
        ##                 peripheries="1",
        ##                 fillcolor = col,
        ##                 fixedsize ="true")
            else:
                heapdot.node(str(i),str(node),**self.node_attr)
                
            if (i >0):
                heapdot.edge(str((i-1)//2),str(i))
        return heapdot

    def draw_graph(self, name_base, dot):

        #print(dot.source)
        name = 'test-output/heap' + name_base +'.gv'
        dot.render(name, view=False)

    def make_heap(self):
        name = self.name + "{:0>3d}_{:0>2d}"         
        dot = self.create_heap_graph(0)
        self.draw_graph(name.format(0, 0), dot)

        for i in range(1,len(self.heap)):
            node = self.heap[i]               
            current = i
            parent = (i-1)//2
            dot = self.create_heap_graph(i)
            self.draw_graph(name.format(i, 0), dot)
            swap_count = 0 
            while( (current > 0) and (node > self.heap[parent])):
                swap_count += 1
                swap(self.heap, current, parent)
                dot = self.create_heap_graph(current, parent)
                self.draw_graph(name.format(i, swap_count), dot)
                node = self.heap[parent]
                current = parent
                parent = (parent-1) //2
            

                
#draw_heap_graph(23, 10)
print(x)
#make_heap(x)
#print(x)

y = [1, 5, 7, 2 , 8, 0]
print(y)
make_heap(y)
print(y)

y = [1, 5, 7, 2 , 8, 0]
h1 = heap_graph("h1", y)
h1.make_heap()


h2 = heap_graph("h2_", x)
h2.make_heap()


