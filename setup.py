import os
from setuptools import setup, find_packages

__version__ = '0.0.1'

here = os.path.abspath(os.path.dirname(__file__))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name="processostjrj",
    version=__version__,
    author="Ministério Público do Rio de Janeiro",
    author_email="cadg@mprj.mp.br",
    description=(
        "Download e parsing dos processos do "
        "Tribunal de Justiça do Rio de Janeiro"),
    license="BSD",
    keywords="tjrj jurídico direito",
    url="https://github.com/MinisterioPublicoRJ/processostjrj",
    packages=find_packages(exclude=['tests*']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=install_requires
)
