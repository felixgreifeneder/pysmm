from setuptools import setup
from setuptools import find_packages

setup(name='pysmm',
      version='0.6',
      description='Python Sentinel Soil-Moisture Mapping',
      long_description='For detailed documentation go-to http://pysmm.readthedocs.io/en/latest/',
      classifiers=[
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3.7',
      ],
      url='https://gitlab.inf.unibz.it/Felix.Greifeneder/pysmm',
      author='Felix Greifeneder',
      author_email='felix.greifeneder@eurac.edu',
      license='GPLv3',
      packages=find_packages(),
      install_requires=['earthengine-api',
                        'google-api-python-client',
                        'google-api-python-client',
                        'google-auth-httplib2',
                        'google-auth-oauthlib',
                        'matplotlib',
                        'numpy',
                        'pandas',
                        'pytesmo',
                        'scikit-learn',
                        'scipy'],
      python_requires='>=3.7',
      include_package_data=True,
      zip_safe=False)