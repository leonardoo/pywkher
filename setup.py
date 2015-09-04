from setuptools import setup
import sys


scripts = [] if sys.version_info.major == 3 else ['bin/wkhtmltopdf-heroku']


setup(
    name='pywkher',
    version='2.12.2.1',
    url='https://github.com/codetalkrs/pywkher',
    author='Jason Mayfield',
    author_email='jason@codetalk.rs',
    packages=['pywkher', ],
    scripts=scripts,
    description='wkhtmltopdf for Python on Heroku',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    install_requires=[
        'Mock==1.0b1',
        ],
    test_suite='tests',
    zip_safe=False
)
