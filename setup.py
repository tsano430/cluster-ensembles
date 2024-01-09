from setuptools import setup, find_packages


VERSION = "1.0.0"
__version__ = VERSION


def parse_requirements_file(filename):
    with open(filename) as f:
        requires = [l.strip() for l in f.readlines() if not l.startswith("#")]
    return requires


setup(
    name="cluster-ensembles",
    version=__version__,
    packages=find_packages(exclude=("tests",)),
    author="Takehiro Sano",
    author_email="tsano430@gmail.com",
    url="https://github.com/tsano430/cluster-ensembles",
    description="A Python package for cluster ensembles",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7, <4",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
    ],
    package_data={
        "cluster_ensembles": [
            "kahypar_config/*",
        ]
    },
    install_requires=parse_requirements_file("requirements.txt"),
)
