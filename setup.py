from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="is-port-free",
    version="1.0.0",
    author="Abderrahim GHAZALI",
    author_email="gha.abderrahim1@gmail.com",
    description="Check if a port is free - simple and minimalistic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abderrahimghazali/is-port-free",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=[],  # No dependencies!
    entry_points={
        "console_scripts": [
            "is-port-free=is_port_free.cli:main",
        ],
    },
    keywords=["port", "network", "socket", "free", "available", "check"],
)