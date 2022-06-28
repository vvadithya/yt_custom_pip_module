import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yt_downloaderr",
    version="0.0.1",
    author="Adithya",
    author_email="sampleemail@gmail.com",
    description="Package to download videos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vvadithya/yt_custom_pip_module",
    packages=setuptools.find_packages(),
    install_requires  = ['Click','requests',...], # List all your dependencies inside the list
    license = 'MIT'
)