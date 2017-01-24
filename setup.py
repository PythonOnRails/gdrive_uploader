from setuptools import setup

install_requires = [
    "google-api-python-client",
    "httplib2",
]

packages = [
    'gdrive',
]

setup(
    name="gdrive",
    version="0.0.1",
    license='MIT',
    description="Drive Upload Helper",
    author='orvice',
    author_email='orvice@orx.me',
    url='https://github.com/PythonOnRails/gdrive_uploader',
    package_data={
        'gdrive': ['README.md', 'LICENSE']
    },
    packages=packages,
    install_requires=install_requires,
    long_description="",
    classifiers=[
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
