async function loadGraph() {
                const response = await fetch('/graph');
                const gData = await response.json();
                console.log(gData);
                const Graph = new ForceGraph3D(document.getElementById('3d-graph'))
                .graphData(gData)
                .nodeLabel('text')
                .nodeAutoColorBy('type')
                // .linkWidth(link => link.strength)
                .linkOpacity(link => link.strength);
                // .onNodeClick();
            }

loadGraph();