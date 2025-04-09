from setuptools import setup

with open('README.md', 'rt') as readme:
    long_description = readme.read()

setup(
    name="immutable-Python-Type",
    version="1.2.3",
    description="A immutable type for Python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="BOXER",
    author_email="vagabonwalybi@gmail.com",
    maintainer="BOXER",
    maintainer_email="vagabonwalybi@gmail.com",
    url="https://github.com/BOXERRMD/immutable",
    project_urls={
        'Documentation': 'https://github.com/BOXERRMD/immutable/wiki',
        'GitHub': 'https://github.com/BOXERRMD/immutable',
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ],
    install_requires=[
    ],

    packages=['immutableType'],
    python_requires=">=3.9",
    include_package_data=True,
)