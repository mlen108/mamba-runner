from setuptools import setup, find_packages


setup(
    name='pymamba',
    version='0.0.1',
    description='Timing for unittest tests',
    url='https://github.com/mattack108/pymamba',
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
    keywords='unittest timing time',
    packages=find_packages(),
)
