from setuptools import setup

setup(
  name="ani-cli-pl",
  version="1.0",
  description="watch anime from command line",
  entry_points={
    "console_scripts": [
      "anicli = src.cli:cli"
    ]
  }
)