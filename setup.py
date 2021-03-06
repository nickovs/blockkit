# Setup file for blockkit
import setuptools
import re

version_line_finder = re.compile(r'__version__\s*=\s*"(\d+\.\d+(\.\d+)?)"')

with open("blockkit/__init__.py", "r") as fh:
    for line in fh:
        match = version_line_finder.match(line)
        if match:
            __version__ = match.groups()[0]
            break
    else:
        print("WARNING: Version info missing from module")
        __version__ = "0.0.0"

with open("README.rst", "r") as fh:
    desc_lines = fh.readlines()
    stops = [i for i,l in enumerate(desc_lines) if "PyPI STOP" in l]
    if stops:
        desc_lines = desc_lines[:stops[0]]
    long_description = "".join(desc_lines)

setuptools.setup(
    name="blockkit",
    version=__version__,
    author="Nicko van Someren",
    author_email="nicko@nicko.org",
    description="A library for the efficient construction of Slack Block Kit data strucures",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/nickovs/blockkit",
    project_urls={
        'Documentation': 'https://blockkit.readthedocs.io/',
        'Issue Tracker': 'https://github.com/nickovs/blockkit/issues'
    },
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    python_requires='>=3.6',
    keywords=['slack', 'json'],
)
