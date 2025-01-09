from setuptools import setup, find_packages

setup(
    name="auto-docs-demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.5.0',
        'mkdocs-material>=9.0.0',
        'mkdocstrings>=0.24.0',
        'mkdocstrings-python>=1.7.0',
        'pytest>=7.0.0',
        'black>=23.0.0',
        'isort>=5.0.0',
    ],
)