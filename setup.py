from setuptools import setup
import os
import sys

if sys.version_info[0] < 3:
    from codecs import open

with open(os.path.join(os.path.dirname(__file__), 'README.md'),
          'r', encoding='utf-8') as f:
    long_description = f.read()
    try:
        import pypandoc
        long_description = pypandoc.convert(
                long_description, 'rst', format='md')
    except BaseException as e:
        print(("DEBUG: README in Markdown format. It's OK if you're only "
               "installing this program. (%s)") % e)

setup(
    name='underline',
    py_modules=['underline'],
    package_data={
        '': [
            'README.md',
            'LICENSE',
        ]
    },
    version='0.0.1',
    author='TylerTemp',
    author_email='tylertempdev@gmail.com',
    url='https://github.com/TylerTemp/md-underline',
    download_url='http://github.com/TylerTemp/md-underline/zipball/master/',
    license='MIT',
    description='Markdown Underline',
    keywords='markdown underline',
    long_description=long_description,
    install_requires=[
        'markdown'
    ],
    platforms='any',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        ],
)