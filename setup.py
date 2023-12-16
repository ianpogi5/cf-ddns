from setuptools import setup, find_packages

setup(
    name="cflare-ddns",
    long_description="Yet another Cloudflare Dynamic DNS application.",
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
)
