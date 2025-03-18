from setuptools import setup, find_packages

setup(
    name="notyfico_monitor",
    version="0.1.0",
    packages=find_packages(),  # Automatically finds all packages
    install_requires=[
        "psutil",
        "requests",
	    "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "notyfico_monitor=monitor_modules.main:main",  # Entry point should point to the correct function
            "notyfico_inline_msg=monitor_modules.inline:main",  # New entry point
        ],
    },
    author="Notyfi.co",
    author_email="info@notyfi.co",
    description="A Python package for monitoring server resources and services.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/skotow/NotyfiCo.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
