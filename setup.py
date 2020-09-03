import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
]


setuptools.setup(
    name='requests-fda',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Lukasz Fundakowski',
    author_email='fundakol@yahoo.com',
    description="Form Digest Authentication for SharePoint site",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='requests form-digest http authentication SharePoint',
    url='',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['requests', 'requests_ntlm'],
    classifiers=classifiers
)
