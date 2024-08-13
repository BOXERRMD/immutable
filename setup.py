from setuptools import setup

setup(
    name="immutable Python Type",
    version="1.0.0",
    description="A immutable type for Python",
    long_description="A library for create immuable 'type' in Python",
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
        "License :: OSI Approved :: MIT License",
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