from setuptools import setup, find_packages

setup(
    name="ToolVerse",
    version="1.3.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)