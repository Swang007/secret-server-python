import setuptools

long_description = "None"

setuptools.setup(
    name="secret-server-sdk-client",
    version="1.1",
    author="Paulo Dorado",
    author_email="support@thycotic.com",
    description="Thycotic python client that uses the Thycotic SDK to get secrets from secret server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Swang007/secret-server-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
