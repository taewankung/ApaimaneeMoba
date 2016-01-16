import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'jinja2',
    'wtforms',
    ]

SCRIPT_NAME = 'apaimanee-moba'
setup(name='apaimanee-moba',
      version='0.0',
      description='apaimanee-game',
      long_description=README,
      classifiers=[
        "Programming Language :: Python :: 3",
        ],
      author='',
      author_email='',
      scripts = ['bin/%s' % SCRIPT_NAME],
      license = 'xxx License',
      packages = find_packages(),
      url='https://github.com/taewankung/ApaimaneeMoba',
      keywords='Apaimanee Moba',
#      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
#      tests_require=requires,
#      test_suite="nokkhum-controller",
      )

