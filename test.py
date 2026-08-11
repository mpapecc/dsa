import plotly.graph_objects as go
from collections import deque

graph_adjacency_list = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def compute_layout(graph, source):
    """BFS-based layered layout: x = depth (distance from source), y = spread within layer."""
    pos = {}
    visited = set()
    queue = deque([(source, 0)])   # (node, depth)
    visited.add(source)
    layers = {}                    # depth -> list of nodes

    while queue:
        node, depth = queue.popleft()
        layers.setdefault(depth, []).append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, depth + 1))

    # assign coordinates: x = depth, y = evenly spaced within layer
    for depth, nodes in layers.items():
        n = len(nodes)
        for i, node in enumerate(nodes):
            y = (i - (n - 1) / 2)   # center the layer vertically
            pos[node] = (depth, y)

    return pos

pos = compute_layout(graph_adjacency_list, "a")

# --- Build edge lines ---
edge_x, edge_y = [], []
for src, neighbours in graph_adjacency_list.items():
    for dst in neighbours:
        x0, y0 = pos[src]
        x1, y1 = pos[dst]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=2, color="gray"),
    hoverinfo="none",
    mode="lines"
)

# --- Build node markers ---
node_x = [pos[node][0] for node in pos]
node_y = [pos[node][1] for node in pos]
node_labels = list(pos.keys())

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode="markers+text",
    text=node_labels,
    textposition="middle center",
    marker=dict(size=40, color="lightblue", line=dict(width=2, color="black")),
    textfont=dict(size=14, color="black"),
    hoverinfo="text"
)

# --- Arrows for direction ---
annotations = []
for src, neighbours in graph_adjacency_list.items():
    for dst in neighbours:
        x0, y0 = pos[src]
        x1, y1 = pos[dst]
        annotations.append(dict(
            ax=x0, ay=y0, x=x1, y=y1,
            xref="x", yref="y", axref="x", ayref="y",
            showarrow=True, arrowhead=3, arrowsize=1.5,
            arrowwidth=2, arrowcolor="gray",
            standoff=20
        ))

fig = go.Figure(data=[edge_trace, node_trace])
fig.update_layout(
    annotations=annotations,
    showlegend=False,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    plot_bgcolor="white",
    width=600, height=500,
    title="Graph Visualization (pure Plotly)"
)
fig.show()