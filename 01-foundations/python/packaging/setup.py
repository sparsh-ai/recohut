from setuptools import setup, find_packages

setup(
    name='templatepackage',
    version='0.0.1',
    description='Standards for Python',
    author='Sparsh Agarwal',
    author_email='sprsag@gmail.com',
    url='https://github.com/sparsh-ai/standards',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'PyYAML',
        'pandas>=0.23.3',
        'numpy>=1.14.5'
    ],
    extras_require={'plotting': ['matplotlib>=2.2.0', 'jupyter']},
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Machine Learning',
      ]
)