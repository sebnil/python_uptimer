from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
print(requirements)

setup(
    name='python_uptimer',
    version='1.4',
    url='',
    license='',
    author='Sebastian Nilsson',
    author_email='',
    description='Monitor web sites and services',
    packages=['python_uptimer', 'tests'],
    install_requires=requirements
)
