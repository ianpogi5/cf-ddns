from setuptools import setup, find_packages

setup(
    name="cf-ddns",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests>=2.31.0"],
    entry_points={
        "console_scripts": [
            "cf-ddns=cf-ddns.__main__:main",
        ],
    },
)
