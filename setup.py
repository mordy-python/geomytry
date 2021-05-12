from setuptools import setup, find_packages

with open("DOCS.md") as readme_file:
    README = readme_file.read()

setup_args = dict(
    name="geomytry",
    version="0.0.3",
    description="Useful functions to work with geometry",
    long_description_content_type="text/markdown",
    long_description=README,
    license="MIT",
    packages=find_packages(),
    author="Mordy Waldo",
    author_email="imky171@gmail.com",
    keywords=["Geometry", "Math", "Shapes"],
    url="https://github.com/mordy-python/geomytry",
    download_url="https://pypi.org/project/geomytry/",
)

install_requires = []

if __name__ == "__main__":
    setup(**setup_args, install_requires=install_requires)
