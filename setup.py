from setuptools import setup, find_packages

setup(
    name="hello_world_package",          # Name of the package
    version="0.1.0",                     # Version number
    author="Your Name",
    author_email="you@example.com",
    description="A simple Hello World Python package",
    long_description="This is a longer description of the Hello World package.",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hello_world_package",  # Optional
    packages=find_packages(),           # Automatically find any sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',            # Minimum Python version required
)
