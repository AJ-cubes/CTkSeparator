from setuptools import setup, find_packages

setup(
    name="CTkSeparator",  # Package name (must be unique on PyPI)
    version="0.1",  # Version number (update as needed)
    author="AJ-cubes",  # Your name or organization
    description="A customizable separator widget for CustomTkinter",
    long_description=open("README.md").read(),  # Readme as full description
    long_description_content_type="text/markdown",  # Define Readme format
    packages=find_packages(),  # Automatically find submodules
    install_requires=["customtkinter"],  # Dependencies
    license="MIT",  # License type
    classifiers=[  # Metadata for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
)
