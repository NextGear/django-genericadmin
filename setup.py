#!/usr/bin/env python

from setuptools import setup
from subprocess import call

def convert_readme():
    try:
        call(["pandoc", "-f", "markdown_github", "-t",  "rst", "-o",  "README.txt", "README.markdown"])
    except OSError:
        pass
    return open('README.txt').read()

setup(
    name='nextgear-django-genericadmin',
    version='0.8.2',
    description="Adds support for generic relations within Django's admin interface.",
    author='Stefan van der Woude',
    author_email='stefan@nextgear.nl',
    url='https://github.com/NextGear/django-genericadmin/',
    packages = ['genericadmin'],
#    package_data={'genericadmin': ['static/genericadmin/js/genericadmin.js']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    long_description=convert_readme(),
    include_package_data=True,
    zip_safe=False,
)
