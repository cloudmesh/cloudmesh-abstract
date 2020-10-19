#!/usr/bin/env python
# ----------------------------------------------------------------------- #
# Copyright 2017, Gregor von Laszewski, Indiana University                #
#                                                                         #
# Licensed under the Apache License, Version 2.0 (the "License"); you may #
# not use this file except in compliance with the License. You may obtain #
# a copy of the License at                                                #
#                                                                         #
# http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                         #
# Unless required by applicable law or agreed to in writing, software     #
# distributed under the License is distributed on an "AS IS" BASIS,       #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.#
# See the License for the specific language governing permissions and     #
# limitations under the License.                                          #
# ------------------------------------------------------------------------#

from setuptools import find_packages, setup
import io

def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split()


#requiers = readfile ('requirements.txt')
#
# add minimum requirements here
#
requiers = """
psutil
""".split("\n")

# dependency_links = ['http://github.com/nicolaiarocci/eve.git@develop']

version = readfile("VERSION")[0].strip()

with open('README.md') as f:
    long_description = f.read()



NAME = "cloudmesh-abstract"
DESCRIPTION = "A command called abstract and foo for the cloudmesh shell"
AUTHOR = "Gregor von Laszewski"
AUTHOR_EMAIL = "laszewski@gmail.com"
URL = "https://github.com/cloudmesh/cloudmesh-abstract"


setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=version,
    license="Apache 2.0",
    url=URL,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Environment :: Plugins",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Shells",
        "Topic :: Utilities",
    ],
    install_requires=requiers,
    tests_require=[
        "flake8",
        "coverage",
    ],
    zip_safe=False,
    namespace_packages=['cloudmesh'],
)
