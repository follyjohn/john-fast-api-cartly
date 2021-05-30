import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="john-fast-api-cartly",
    version="0.0.1",
    author="follyjohn",
    author_email="follyjohn@outlook.fr",
    description="A small example of API made with FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/follyjohn/john-fast-api-cartly",
    project_urls={
        "Bug Tracker": "https://github.com/follyjohn/john-fast-api-cartly/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "app"},
    packages=setuptools.find_packages(where="app"),
    python_requires=">=3.7",
)
