from setuptools import find_packages, setup

setup(
    name="maps-deduped-tilelist",
    version="0.0.1",
    author="Yiannis Giannelos",
    author_email="jgiannelos@wikimedia.org",
    description="Generate a distinct list of map tiles up to a zoom level",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": ["maps-deduped-tilelist=tileset.cli:main"],
    },
)
