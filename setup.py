from setuptools import setup, find_packages

setup(
    name="CTkSeparator",
    version="1.0",
    author="AJ-cubes",
    description="A customizable separator widget for CustomTkinter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["customtkinter"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
