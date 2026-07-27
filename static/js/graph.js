const typeColors = {
  noun: '#8cd0e3',
  verb: '#e38c8c',
  adjective: '#8ce3a8',
  adverb: '#e3c98c',
  phrase: '#c98ce3',
  idiom: '#e38cc9',
  other: '#aaaaaa'
};

async function loadGraph() {
                const response = await fetch('/graph');
                const gData = await response.json();
                console.log(gData);
                const Graph = new ForceGraph3D(document.getElementById('3d-graph'))
                .graphData(gData)
                .nodeLabel('text')
                .nodeColor(node => typeColors[node.type] || "#aaaaaa")
                .backgroundColor("#05081c")
                // // .linkWidth(link => link.strength)
                .linkOpacity(link => link.strength)
                .onNodeClick(node => showDetails(node));
            }

loadGraph();

function showDetails(node) {
  document.getElementById('panel-text').textContent = node.text;
  document.getElementById('panel-type').textContent = node.type;
  document.getElementById('panel-definition').textContent = node.definition;
  document.getElementById('details-panel').style.setProperty('--accent', typeColors[node.type] || '#aaaaaa');
  document.getElementById('details-panel').classList.remove('hidden');
}

document.getElementById('panel-close').addEventListener('click', () => {
  document.getElementById('details-panel').classList.add('hidden');
});