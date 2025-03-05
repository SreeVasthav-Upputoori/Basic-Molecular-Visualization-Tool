Molecular Visualization Tool

This project is a **Dash-based web app** that allows users to visualize **2D and 3D molecular structures** from SMILES input.

Features
- Convert **SMILES** notation to **2D** molecular structure
- Generate **3D** molecular visualization
- Works in **VS Code** and **Google Colab**
- Uses **RDKit** for cheminformatics and **py3Dmol** for 3D rendering

Installation
For VS Code
1. Clone the repository:
   ```sh
git clone https://github.com/SreeVasthav-Upputoori/Basic-Molecular-Visualization-Tool.git
cd molecular-visualization
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. Open **http://127.0.0.1:8050/** in your browser.

For Google Colab
1. Install dependencies:
   ```python
   !pip install dash dash-bootstrap-components rdkit-pypi py3Dmol flask
   ```
2. Run `app.py` and click the generated link to access the UI.

License
MIT License
