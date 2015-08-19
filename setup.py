from setuptools import setup, find_packages


setup(
    name='django-rest-filter',
    version='0.1',
    url='http://github.com/sauramirez/django-rest-filter',
    license='MIT',
    description='Filters for Django REST Framework',
    author='Sau Ramirez',
    author_email='saumotions@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'djangorestframework'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='runtests'
)
