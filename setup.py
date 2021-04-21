 from setuptools import setup

 setup(
   name='django-admin-export-xlsxPackageName',
   version='1.0.0',
   author='Rune Hansén Steinnes',
   author_email='rune.steinnes@renroros.no',
   packages=['export_xlsx'],
   url='http://github.com/Ren-Roros-Digital/django-admin-export-xlsx',
   license='LICENSE.txt',
   description='Admin action to export xlsx from list_display',
   long_description=open('README.txt').read(),
   install_requires=[
       "Django >= 3",
       "unidecode >=1.2",
       "openpyxl >= 3",
   ],
)
