from setuptools import setup, find_packages
import os

version = open(os.path.join("Products", "ATGoogleVideo", "version.txt")).read().strip()

setup(name='Products.ATGoogleVideo',
      version=version,
      description="Use YouTube and Google Video on a Plone Site",
      long_description=open(os.path.join("Products", "ATGoogleVideo", "README.txt")).read().decode('UTF8').encode('ASCII', 'replace') + '\n' +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone ATGoogleVideo youtube video googlevideo',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='https://svn.plone.org/svn/collective/Products.ATGoogleVideo',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
