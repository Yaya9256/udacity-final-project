net="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Jaja is connected to.\
Jaja likes to play LA Noir, Mafia games, Witcher.\
Peter is connected to Jaja.\
Peter likes to play.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

def create_data_structure(net):
    network = {}
    sentence = net.split(".")
    for i in range(0,len(sentence)-1,2): # 26 items, 0-25
        user = sentence[i][:sentence[i].find(" ")]
        network[user] = [] # key in dictionary is user + empty list
        connection = sentence[i][sentence[i].find(" connected to ") + len(" connected to "):]
        if ", " in connection or "" in connection: 
            network[user].append(connection.split(", "))
        games = sentence[i+1][sentence[i+1].find("play ") + len("play "):]
        network[user].append(games.split(", "))
    for i in network:
        if network[i][0] == ['cted to']:
            network[i][0] = []
        if network[i][1] == ['r likes to play']:
            network[i][1] = []
    return network
print(create_data_structure(net))
def get_connections(network, user):
    for i in network: # for each key in dict
        if i == user:
            return network[i][0] # first list = [friend list]
    return None
# print(get_connections(create_data_structure(net),"John"))
def games_liked(network, user):
    for i in network:
        if i == user: 
            return network[i][1] # second list = [game list]
    return None
# def games_liked(network, user):
#     return network.get(user,None)

# print(games_liked(create_data_structure(net),"John"))
def add_connection(network, user_A, user_B):
    if get_connections(network, user_A) == None or get_connections(network, user_B) == None: 
        return False
    if user_B not in get_connections(network, user_A):
        network[user_A][0].append(user_B)
    return network
#print(add_connection(create_data_structure(net), "Debra", "John"))
def add_new_user(network, user, games):
    if get_connections(network, user) != None:
        return network
    else:
        network[user] = []
        network[user].append([])
        network[user].append(games)
    return network
#print(add_new_user(create_data_structure(net), "Tony", ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']))
def get_secondary_connections(network, user):
    con_of_con = []
    if user in network:
        for i in get_connections(network,user):
            con_of_con+=(get_connections(network,i))
    return con_of_con
#print(get_secondary_connections(create_data_structure(net), "Robin"))
def count_common_connections(network, user_A, user_B): # returns a count (integer) of exact same value in connection for userA and userB
    count_of_same_friends = 0
    if get_secondary_connections(network, user_A) == [] or get_secondary_connections(network, user_B) == []: 
        return False
    A_con = set(get_secondary_connections(network, user_A)) # loose doubles
    B_con = set(get_secondary_connections(network, user_B))
    #print(A_con,B_con)
    for i in A_con: 
        if i in B_con: 
            count_of_same_friends+=1
    return count_of_same_friends
#print(count_common_connections(create_data_structure(net), "John", "Levi"))

def find_path_to_friend(network, user_A, user_B):
    path = []
    connections = get_connections(network, user_A)
    print(connections)
    networkCopy = network.copy()
    print(networkCopy[user_A], "0")
    del(networkCopy[user_A])
    if user_B in connections:
        return user_A
    for user in connections:
        if user in networkCopy.keys():
            print(networkCopy.keys(), "1") # returns all keys, as name of list o lists excluding user_A
            path += [find_path_to_friend(networkCopy, user, user_B)]
    path.append(user_B)
    path.insert(0,user_A)
    if path[0] == user_A and path[-1] == user_B:
        path = [i for i in path if isinstance(i,str)] # list comprehension?
        return path
    return None

print(find_path_to_friend(create_data_structure(net), "John", "Ollie"))

