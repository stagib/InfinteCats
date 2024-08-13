from setuptools import setup, find_packages

setup(
  name="infinite_cats",
  version='0.1',
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    "Flask",
  ],
  entry_points={
    "console_scripts": [
    "cat=app.__main__:main",
    ],
  },
)