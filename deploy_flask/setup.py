import setuptools

setuptools.setup(
    name='sayhello',
    version='0.0.1',
    url='https://github.com/moshez/twist-wsgi',
    author='Moshe Zadka',
    author_email='zadka.moshe@gmail.com',
    packages=setuptools.find_packages(where='src') + ['twisted.plugins'],
    install_requires=['Twisted', 'flask', 'setuptools', 'txacme'],
    package_dir={'': 'src'},
    package_data={'sayhello': ['data/index.html']},
)
