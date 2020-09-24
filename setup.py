import setuptools

setuptools.setup(
    name="nbdlang-jakekara", # Replace with your own username
    version="0.0.1",
    author="Jake Kara",
    author_email="jake@jakekara.com",
    description="A notebook description language parser",
    url="https://github.com/jakekara.com/nbdl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)