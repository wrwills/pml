from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='pml',
    version='1.0.0',
    packages=['', 'tests', 'visualise', 'experiments'],
    install_requires=install_requires,
    url='',
    license='',
    author='ajacques',
    author_email='',
    description='EPS sort package'
)
