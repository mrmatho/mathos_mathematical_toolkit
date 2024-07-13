import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

st.title("Task Scheduling Network Graph")

# Function to create the graph
def create_graph(tasks, dependencies, times):
    G = nx.DiGraph()
    for task, time in zip(tasks, times):
        G.add_node(task, duration=time)
    
    for dep in dependencies:
        G.add_edge(dep[0], dep[1])
        
    
    return G

# Sample data
tasks = ["Task A", "Task B", "Task C", "Task D"]
dependencies = [("Task A", "Task B"), ("Task B", "Task C"), ("Task A", "Task D")]
times = [3, 2, 4, 1]

st.sidebar.title("Input Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    tasks = data['Task'].tolist()
    dependencies = list(zip(data['Dependency_Start'], data['Dependency_End']))
    times = data['Time'].tolist()

# Creating the graph
G = create_graph(tasks, dependencies, times)
st.write(G, G.nodes, G.edges)
'''
# Draw the graph
fig, ax = plt.subplots(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=12, font_weight='bold', ax=ax)
labels = nx.get_node_attributes(G, 'times')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['times']} units" for u, v, d in G.edges(data=True)}, ax=ax)

st.pyplot(fig)
'''