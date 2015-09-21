from setuptools import find_packages, setup


version = '1.2.0'


install_requires = (
    'djangorestframework>=3.0.5,<3.3',
    'FeinCMS>=1.9,<1.11',
    'django-orderable>=2.0.1,<4',
    'feincms-extensions>=0.1.0,<1',
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
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
