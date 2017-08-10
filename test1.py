import json
import networkx as nx
import time
start=time.time()       #this is just to know how much time the code need

######### function to create nodes from each of the users##################################
def add_node_ev(data,j):
    repeat_event=0
    if not G.has_node(data[j]['member']['member_id']):  #if the node doesnt exist->create (the name of the node is the member id, the add the event name and the group city, and finally the number of events that have)
        G.add_node(data[j]['member']['member_id'],name=data[j]['member']['member_name'],event1=data[j]['event']['event_name'],group_city1=data[j]['group']['group_city'],n_events=1)
    else: #node already exists
        n_e=G.node[data[j]['member']['member_id']]['n_events']      #read number of events
        for y in range(1,n_e+1):
            if data[j]['event']['event_name'] == G.node[data[j]['member']['member_id']]['event'+str(y)]:        #not repeat event same user
                repeat_event=1  #already read this event on this user
        if repeat_event==0:
            G.node[data[j]['member']['member_id']]['event'+str(n_e+1)]=data[j]['event']['event_name']           #add new event
            G.node[data[j]['member']['member_id']]['n_events']=n_e+1                                            #sum 1 to number of events
            G.node[data[j]['member']['member_id']]['group_city'+str(n_e+1)]=data[j]['group']['group_city']      #add city of new event
    return repeat_event
############# function to add edges between members that share an event#############################
 def add_edge_ev(data,j):
    for i in G:#compare other nodes
        try:
            for t in range(1,G.node[data[j]['member']['member_id']]['n_events']+1):     #for all the events in each node
                if data[j]['event']['event_name']==G.node[i]['event'+str(t)] and data[j]['member']['member_id']!=i:#events are the same with another node
                    try:    #try to add 1 to the edge between links (only works if the link(edge) already exist)
                        wi=G[data[j]['member']['member_id']][i]['weight']
                        G[data[j]['member']['member_id']][i]['weight']=wi+1
                        break
                    except:     #if the edge(link) doesnt exist it will be added with weight equal to 1 or 0
                        G.add_edge(data[j]['member']['member_id'],i,weight=0)
                        break
        except:
            t=t
################### main code#################
G=nx.Graph()    #define graph G
#G.add_node('hello')
data=[]
event_name=[]
j=0
with open('nl_events_complete.json') as data_file:      #open de json file(all the data)
#with open('JSON_stream_Data_2.json') as data_file:
    for line in data_file:
        data.append(json.loads(line))                   # for each line of the file I add the information to my vector data
        repeat_event=add_node_ev(data,j)
        #print j# add node for each line
        #add_node_ev(data,j)
        if j>0 and repeat_event==0:
            #start2=time.time()
            add_edge_ev(data,j)                         #if its a new event for the same node I look for links with other nodes
            #start3=time.time()
            #print(start3-start2)
            #break
        j=j+1
        if j==60000:            #jus to see how much lines the code has already read
            print j
        if j==95000:
            print j
        if j==80000:
            print j
        if j==105000:
            print j
        #if j>500:
        #    #print j
        #    break
#for a in G:
#    for b in G:
#        for e_a in range(1,G.node[a]['n_events']+1):
#            for e_b in range(1,G.node[b]['n_events']+1):
#                if G.node[a]['event'+str(e_a)]==G.node[b]['event'+str(e_b)]:
#                    G[a][b]['weight']=0

end=time.time()
print(end-start)        #total time code


#G.degree(0)
# G.node[data[1]['member']['member_id']]['group_city1']
#G.number_of_nodes()
#G[140366682][12826735]['weight']
#G.get_edge_data(140366682,12826735)
#nx.write_graphml(G, "test_members_events_EDGESM1_world.graphml")          #save graph to read ir in gephi
