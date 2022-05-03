from setuptools import find_packages
from setuptools import setup

setup(name='movs-kmymoney',
      version='0.0.1',
      author='Vito De Tullio',
      author_email='vito.detullio@gmail.com',
      description='bridge to kmymoney',
      url='https://github.com/ZeeD/movs-kmymoney',
      packages=find_packages(),
      python_requires='>=3.8',
      entry_points={
          'gui_scripts': [
              'movs-kmymoney = movskmymoney:main'
          ]
      },
      install_requires=[
          'movs'
      ])
