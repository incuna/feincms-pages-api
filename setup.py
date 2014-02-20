from setuptools import find_packages, setup


version = '0.0.2'


install_requires = (
    'djangorestframework>=2.3.10,<3',
    'FeinCMS>=1.9,<1.10',
    'django-orderable>=2.0.1,<3',
)


setup(
    name='feincms-pages-api',
    version=version,
    author='Incuna Ltd',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/feincms-pages-api/',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
)
