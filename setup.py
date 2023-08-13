from setuptools import find_packages, setup

setup(
    name='DataPrepManager',
    packages=find_packages(include=['ImagePrepManagerLibrary']),
    version='0.1.0',
    description='Prep image manager for machine learning models.',
    author='Michael Campos',
    license='MIT',
    install_requires=['Pillow', 'numpy', 'pdf2image'],
    setup_requires=['pytest-runner'],
    #tests_require=['pytest==4.4.1'],
    #test_suite='tests',
)