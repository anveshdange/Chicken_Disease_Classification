# imports
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Constants
__version__: str = "0.0.0"
REPO_NAME: str = "CNN_Classifier"
AUTHOR_USER_NAME: str = "anveshdange"
SRC_REPO: str = "Chicken_Disease_Classification"
AUTHOR_EMAIL: str = "dangeanv@gmail.com"

# Setup tools configurations
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Package for CNN Application",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src")
)
