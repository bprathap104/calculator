from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='calc',
    version='0.1.0',
    author='Saran',
    author_email='bprathap104@gmail.com',
    description='A utility for doing arithmetic operations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bprathap104/calculator',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_Requires=[],
    python_requires='>=3.6',
        entry_points={
        'console_scripts': [
            'calculator=calculator.cli:main',
        ],
    }
)
