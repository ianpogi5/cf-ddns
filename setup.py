from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="cflare-ddns",
    version="0.2.0",
    author="Ian Dela Cruz",
    author_email="iandc76@gmail.com",
    url="https://github.com/ianpogi5/cflare-ddns",
    packages=find_packages(),
    install_requires=["requests>=2.31.0"],
    entry_points={
        "console_scripts": [
            "cflare-ddns=cflare_ddns.main:main",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
