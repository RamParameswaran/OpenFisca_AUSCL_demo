# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "OpenFisca_AUSCL_demo",
    version = "0.0.1",
    author = "Ram Parameswaran",
    author_email = "ram@findram.dev",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Information Analysis",
        ],
    description = "OpenFisca Demonstration Repo - for Australian Society for Computers and Law (AUSCL) forum series",
    keywords = "OpenFisca Rules as Code AUSCL",
    license ="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    url = "https://github.com/openfisca/OpenFisca_AUSCL_demo",
    include_package_data = True,  # Will read MANIFEST.in
    data_files = [],
    install_requires = [
        "OpenFisca-Core[web-api]",
        ],
    packages=find_packages(),
    )
