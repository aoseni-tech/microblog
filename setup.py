from setuptools import find_packages, setup

setup(
    name="microblog",
    version="1.0.0",
    description="a simple blog app",
    author="acetech",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="MIT",
    install_requires=[
        'flask',
    ],
)