from setuptools import setup, find_packages

setup(
    name="Tp_jenkins",          # Nom de ton projet
    version="0.1",               # Version du package
    packages=find_packages(),    # Trouve automatiquement les packages dans ton repo
    install_requires=[           # Dépendances à installer automatiquement
        "Flask",
        "pytest",
        "flake8"
    ],
)
