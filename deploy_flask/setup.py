import setuptools

setup(
    name='sayhello',
    version='0.0.1',
    url='https://github.com/moshez/twist-wsgi',
    author='Moshe Zadka'
    author_email='zadka.moshe@gmail.com',
    packages=setuptools.find_packages() + ['twisted.plugins'],
    install_requires=['Twisted', 'flask', 'setuptools'],
    package_dir={'sayhello': 'src/sayhello'},
    package_data={'sayhello': ['data/index.html']},
)
