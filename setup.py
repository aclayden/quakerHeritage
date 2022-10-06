import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent.replace("\\", "/")
README = (HERE / "README.md").read_text()

requirements = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

if __name__ == '__main__':
    setuptools.setup(
        name="quakerheritage",
        version="1.0.1",
        description="",
        long_description=README,
        long_description_content_type="text/markdown",
        author="",
        author_email="",
        license="AGPL",
        packages=["quakerheritage"],
        zip_safe=False,
        requires=requirements
    )