import os
import dash
from dash import dcc, html, Input, Output
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
import base64
import io
import py3Dmol
import threading
from flask import Flask

# Detect if running in Google Colab
try:
    from google.colab import output
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

# Flask App for Dash
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("Molecular Visualization Tool"),
    dcc.Input(id="smiles-input", type="text", placeholder="Enter SMILES string..."),
    html.Button("Visualize", id="submit-btn", n_clicks=0),
    html.H3("2D Structure"),
    html.Img(id="mol-image", style={"marginTop": 20}),
    html.H3("3D Structure"),
    html.Div(id="mol-3d")
])

@app.callback(
    [Output("mol-image", "src"), Output("mol-3d", "children")],
    [Input("submit-btn", "n_clicks"), Input("smiles-input", "value")]
)
def update_molecule(n_clicks, smiles):
    if not smiles:
        return None, None
    
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, None
    
    # Generate 2D Image
    img = Draw.MolToImage(mol, size=(300, 300))
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode()
    
    # Generate 3D Structure
    mol_3d = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol_3d, AllChem.ETKDG())
    mol_block = Chem.MolToMolBlock(mol_3d)
    
    viewer = py3Dmol.view(width=400, height=400)
    viewer.addModel(mol_block, "mol")
    viewer.setStyle({"stick": {}})
    viewer.zoomTo()
    
    return f"data:image/png;base64,{encoded_image}", html.Div([
        html.Iframe(srcDoc=viewer._make_html(), width="400", height="400")
    ])

def run_dash():
    """Run the Dash app based on the environment"""
    if IN_COLAB:
        print("🚀 Your app is running! Click the link below to open it:")
        from google.colab import output
        app_url = output.serve_kernel_port_as_iframe(8050, path="/")
        print(app_url)
        app.run_server(host='0.0.0.0', port=8050, debug=False)
    else:
        app.run_server(debug=True)

# Run Dash in a separate thread
if __name__ == "__main__":
    threading.Thread(target=run_dash, daemon=True).start()