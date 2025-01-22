from pyvis.network import Network
import streamlit.components.v1 as components

def render_visualization():
    # Example graph
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
    net.add_node("User", label="User", color="#FF5733")
    net.add_node("Python", label="Python", color="#33FF57")
    net.add_node("Data Scientist", label="Data Scientist", color="#3357FF")
    net.add_edge("User", "Python")
    net.add_edge("Python", "Data Scientist")

    net.save_graph("graph.html")

    with open("graph.html", "r") as f:
        components.html(f.read(), height=600)
