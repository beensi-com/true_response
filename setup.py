from setuptools import setup, find_packages

setup(
    name='true_response',
    version='3.1',
    license='BEENSI',
    author='beensi.com dev group',
    # author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/beensi-com/true_response',
    keywords='restfull response',
    install_requires=[],

)
