import setuptools

with open("README.md", "r", encoding="utf-8") as f:  # this is helpful if we want to publish it as PyPi package. There the README.md file shuold provide necessary information.
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End_to_End_Text_Summerization"
AUTHOR_NAME = "Anindya Sen"
SRC_REPO = "Summerize-Text"
AUTHOR_EMAIL = "joyanindya99@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="End to End Text Summerization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anindya2306/" + SRC_REPO,
    package_dir= {"": "src"},
    packages=setuptools.find_packages(where="src")
)
