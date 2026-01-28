import random
import numpy as np
import matplotlib.pyplot as plt
#------ PART 1: MAKING A LIST OF AGENTS AND DISTRIBUTING THEM IN GROUPS
def totalagentsmaker(n):#makes a list with n-many agents, represented by the integers from 1 to n
    return list(range(n))

def beliefassignment(p, e, agents):# assigns beliefs within a margin e of the initial probability/ degree of belief p, to each of the agents in list agents
    beliefs  ={}
    for agent in agents:
        if random.random() < 0.95:
            beliefs[agent] = p + random.uniform(0, e)
        else:
            beliefs[agent] = random.uniform(p, 1)
            
   
    return beliefs
    


def villagedistributer(num_villages, agents):#distributes the agents in the main list of agents through a number villages
    if agents % num_villages != 0:
        raise ValueError("The number of agents must be divisible by the number of villages!")
    agents = agents.copy()
    random.shuffle(agents)
    agents_per_village = round(len(agents)/num_villages) 
    list_of_villages = [agents[i*agents_per_village: (i+1)*agents_per_village] for i in range(num_villages)]
    return list_of_villages

# -------- PART 2: MAKE THE GROUPS INTO GRAPHS IN ORDER TO MODEL DIFFERENT RELATIONSHIPS BETWEEN AGENTS
    

def sym_closure(edges): #Gives the symmetric closure of a list, necessary because the relations between agents are symmetric
    result = set(edges)
    for a, b in result:
        result.add((b,a))
    
    return(list(result))
    
def make_ring_lattice(nodes, k): #Make a ring lattice out of a list of nodes, where each node has k neighbours
    edges_of_ring_lattice = []
    n = len(nodes)
    half_k = k // 2  # number of neighbours on each side

    for i in range(n):
        for l in range(1, half_k + 1):
            j = (i + l) % n
            edges_of_ring_lattice.append((nodes[i], nodes[j]))

    return sym_closure(edges_of_ring_lattice)


def rewiring_ring_lattice(edges, p, nodes):#rewire the graph (nodes, edges) so that each node forms an edge with another node with probability p.
    rewired_list = []
    existing_edges = set()
    for e in edges:
        existing_edges.add(tuple(e))
    for edge in edges:
        if random.random() < p:
            attempts = 0
        
            new_edge = None
            while attempts < 100:
                attempts += 1
                new_node = random.choice(nodes)
                if new_node != edge[0]:
                    candidate = tuple(sorted((edge[0], new_node)))
                   
                    if candidate not in existing_edges:
                       
                        existing_edges.add(candidate)
                        rewired_list.append(candidate)
                        
                     

                        break
          
        else:
            rewired_list.append(edge)
            
    return sym_closure(rewired_list)


def makesmallworldnetworksinvillages(villagelist, k, p): # transform each of the villages in the village list into a small world network
         smallworldedvillages = [rewiring_ring_lattice(make_ring_lattice(v, k), p, v) for v in village list]
         
         return smallworldedvillages
    
#---- PART 3: UPDATE THE AGENTS BELIEFS BASED ON THE BELIEFS OF OTHER AGENTS IN THE NETWORK

def findneighbours(a, list_of_ordered_pairs):# finds all the neighbours (the second element of an ordered pair) of an element a
    neighbours = [a]
 
    for pair in list_of_ordered_pairs:
        if pair[0] == a:
            if pair[1] not in neighbours:
                neighbours.append(pair[1])
         
    return neighbours


def findallneighbours(smallworldedvillages):
     # this function (input: a list of smallworldnetworks; output: a list of lists containing the neighbours of all agents)finds ALL neighbours of ALL AGENTS in each smallword network obtained from the villages
    allneighbours = []

    for village in smallworldedvillages:
        for edge in village:
            if findneighbours(edge[0], village) not in allneighbours:
                allneighbours.append(findneighbours(edge[0], village))
    return allneighbours

def weight_assignment(x):# This is necessary for the deGroot model of belief update: outputs a list with x belief weights for x many agents
    agentweights = [random.random() for _ in range(x)]
    normalized = [w/sum(agentweights) for w in agentweights]
    agentsnice = np.array(normalized)
    return agentsnice

def update_beliefs_with_degroot(allneighbours, beliefs): #performs deGroot belief update

    for listofneighbours in allneighbours:
        
        current_beliefs = np.array([beliefs[a][-1] for a in listofneighbours])

        weights = weight_assignment(len(listofneighbours))
        new_beliefs = weights @ current_beliefs

        beliefs[listofneighbours[0]].append(new_beliefs)
    return beliefs

def update_beliefs_with_degroot_multiple_times(n, allneighbours, beliefs):
    for i in range(n):
   
        update_beliefs_with_degroot(allneighbours, beliefs)
        
    return beliefs






def main():
    try:
        n = int(input("How many agents? "))
    except ValueError:
        print("Value must be an integer")

    while True:
        try:
            g = int(input("How many groups? "))
            if int(n / g):
                break
            else:
                print("The number of agents must be divisible by the number of groups")
        except ValueError:
            print("Value must be an integer")

    while True:
        try:
            m = float(input("Enter an initial probability between 0 and 1: "))  # ask for the initial probability degree of belief
            if 0 <= m <= 1:
                break
            else:
                print("The value must be between 0 and 1")
        except ValueError:
            print("Value must be a float")

    while True:
        try:
            epsilon = float(input("Enter a small value of epsilon (in the order of 0.01): "))
            if 0 <= epsilon <= 0.09:
                break
            else:
                print("The value must be between 0 and 0.09")
        except ValueError:
            print("Value must be a float")

    while True:
        try:
            k = int(input("What is the k(number of connected) neighbours of the network? "))
            if k <= n / g:
                break
            else:
                print("The value must be smaller than the number of agents in each group")
        except ValueError:
            print("Value must be an integer")

    try:
        p = float(input("What is the rewiring probability? "))
    except ValueError:
        print("Value must be a float")

    try:
        r = int(input("How many runs? "))
    except ValueError:  # fixed typo
        print("Value must be an integer")


    beliefsdictionary = beliefassignment(m, epsilon, totalagentsmaker(n))

    #totalagentsmaker(n)
    #villagedistributer(g, totalagentsmaker(n))
    #update_beliefs_with_degroot_multiple_times(r,
        #findallneighbours(
            #makesmallworldnetworksinvillages(
                #villagedistributer(g, totalagentsmaker(n)), k, p
            #)
        #),
        #beliefsdictionary
    #)

    #belief_matrix = np.array(list(beliefsdictionary.values()))
    #average_beliefs = belief_matrix.mean(axis = 0)
    #time_steps = np.arange(len(average_beliefs))
    #plt.plot(time_steps, average_beliefs, marker='o')
    #plt.xlabel("Time step")
    #plt.ylabel("Average belief")
    #plt.title("Average Belief Over Time")
    #plt.grid(True)
    #plt.show()


    #print(beliefassignment(m, epsilon, totalagentsmaker(n)))
    print( beliefassignment(m, epsilon, totalagentsmaker(n)))
    print(f"initial beliefs:{beliefsdictionary}")
    print(makesmallworldnetworksinvillages(villagedistributer(g, totalagentsmaker(n)), k, p))


    print(findallneighbours(
            makesmallworldnetworksinvillages(
                villagedistributer(g, totalagentsmaker(n)), k, p
            )))
    print(update_beliefs_with_degroot(
        findallneighbours(
            makesmallworldnetworksinvillages(
                villagedistributer(g, totalagentsmaker(n)), k, p
            )
        ),
        beliefsdictionary
    )
)
    print(
    update_beliefs_with_degroot_multiple_times(r,
        findallneighbours(
            makesmallworldnetworksinvillages(
                villagedistributer(g, totalagentsmaker(n)), k, p
            )
        ),
        beliefsdictionary
    )
)




























if __name__ == "__main__":
    main()




