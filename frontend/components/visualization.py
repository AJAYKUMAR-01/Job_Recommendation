from pyvis.network import Network
import streamlit.components.v1 as components

def render_visualization():
    # Example graph
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
    net.add_node("User", label="User", color="#FF5733")
    net.add_node("Python", label="Python", color="#33FF57")
    net.add_node("dsa", label="Data Structures & Algos", color="#33FF57")
    net.add_node("js", label="Java Script", color="#33FF57")
    net.add_node("sql", label="SQL", color="#33FF57")
    net.add_node("Machine Learning", label="Machine Learning", color="#33FF57")
    net.add_node("Data Scientist", label="Data Scientist", color="#3357FF")
    net.add_node("Software Engineer", label="Software Engineer", color="#3357FF")
    net.add_edge("User", "Python")
    net.add_edge("User", "sql")
    net.add_edge("User", "js")
    net.add_edge("User", "dsa")
    net.add_edge("User", "Machine Learning")
    net.add_edge("Python", "Data Scientist")
    net.add_edge("Python", "Software Engineer")
    net.add_edge("dsa", "Software Engineer")
    net.add_edge("sql", "Software Engineer")
    net.add_edge("js", "Software Engineer")
    net.add_edge("Machine Learning", "Data Scientist")

    net.save_graph("graph.html")

    with open("graph.html", "r") as f:
        components.html(f.read(), height=600)
