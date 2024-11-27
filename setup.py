from setuptools import setup, find_packages

setup(
    name="SecretSantaApp",  # The name of your package
    version="0.1",          # Version number
    packages=find_packages(),  # Automatically finds all packages (like `app`)
    install_requires=[],    # List any dependencies here (optional)
    python_requires=">=3.6",  # Specify Python version compatibility
)