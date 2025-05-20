from setuptools import setup, find_packages

setup(
    name="CTkSeparator",
    version="1.4",
    author="AJ-cubes",
    author_email="ajcubes33@gmail.com",
    description="A customizable separator widget for CustomTkinter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AJ-cubes/CTkSeparator/",
    keywords=["separator", "customtkinter", "GUI", "widget"],
    packages=find_packages(),
    install_requires=["customtkinter", "pillow"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
