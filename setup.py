import os

from setuptools import setup, find_packages

setup(
    name='django-rj-utils',
    version='0.1',
    description='This is a personal app for utilities that I use for my daily work.',
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.rst')).read(),
    author='Raphael Jasjukaitis',
    author_email='webmaster@raphaa.de',
    url='https://github.com/raphaa/django-rj-utils',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False
)
