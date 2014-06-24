from setuptools import setup, find_packages


setup(
    name='mamba-runner',
    version='0.0.1',
    description='Measure time execution for unittest tests',
    url='https://github.com/mattack108/mamba-runner',
    author='Maciek Lenc',
    author_email='matt.lenc@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=['blessings'],
    keywords='unittest timing time mamba tests runner',
    packages=find_packages(),
)
