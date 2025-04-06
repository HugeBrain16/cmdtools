import setuptools


from cmdtools import __version__ as version


setuptools.setup(
    name="cmdtools-py",
    description="A (not quite) flexible command framework",
    version=version,
    author="HugeBrain16",
    author_email="hugebrain16@gmail.com",
    license="MIT",
    keywords="command-parser command-processor command cmd cmd-parser framework command-framework",
    url="https://github.com/HugeBrain16/cmdtools",
    include_package_data=True,
    packages=["cmdtools"],
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://cmdtools-py.readthedocs.io/en/latest",
        "Issues Tracker": "https://github.com/HugeBrain16/cmdtools/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
    ],
)
