from setuptools import setup, find_packages

setup(
    name="mdtoc",
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['mdtoc=mdtoc.__main__:main']}
)

