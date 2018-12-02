from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='ineq',
      version='0.1',
      description='Package to calculate and plot income distribution indexes',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Economics :: Inequality :: Income distribution',
      ],
      keywords='Income distribution',
      url='http://github.com/gpetrini/ineq',
      author='Gabriel Petrini da Silveira',
      author_email='gpetrinidasilveira@gmail.com',
      license='MIT',
      packages=['ineq'],
      install_requires=[
          'numpy',
	  'matplotlib',
      ],
      include_package_data=True,
      zip_safe=False)

