from setuptools import setup, find_packages

__version__ = '3.2.3'

setup(
    name='reportportal-client',
    packages=find_packages(),
    version=__version__,
    description='Python client for Report Portal',
    author='Artsiom Tkachou',
    author_email='SupportEPMC-TSTReportPortal@epam.com',
    url='https://github.com/reportportal/client-Python',
    download_url=('https://github.com/reportportal/client-Python/'
                  'tarball/%s' % __version__),
    license='Apache 2.0.',
    keywords=['testing', 'reporting', 'reportportal'],
    classifiers=[],
    install_requires=['requests>=2.4.2', 'six'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
