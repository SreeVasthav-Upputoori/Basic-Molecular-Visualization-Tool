from setuptools import setup, find_packages

setup(
    name="molecular_visualization_tool",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "dash",
        "dash-bootstrap-components",
        "rdkit-pypi",
        "py3Dmol",
        "flask"
    ],
    entry_points={
        "console_scripts": [
            "molecular-visualizer=app:run_dash"
        ]
    },
    author="Sree Vasthav Upputoori",
    author_email="sreevasthav.upputoori@gmail.com",
    description="A web-based molecular visualization tool using Dash and RDKit",
    license="MIT",
    url="https://github.com/SreeVasthav-Upputoori/molecular-visualization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
