from setuptools import find_namespace_packages, setup

setup(
    version='0.1.0',
    name='authomize-python-provider-template',
    author='Authomize inc.',
    author_email='info@authomize.com',
    description='Example provider',
    packages=find_namespace_packages(include=['authomize.*']),
    include_package_data=True,
    python_requires='>=3.10.*',
    install_requires=[
        'authomize-rest-api-client>=1.5.1',
        'more-itertools~=8.12',
        'pydantic>=1.9.1',
    ],
    extras_require={
        'onelogin': [
            'onelogin~=2.0.4',
        ],
        'test': [
            'coverage~=5.2',
            'flake8~=4.0',
            'flake8-isort~=4.0',
            'flake8-commas~=2.0',
            'pyhamcrest~=2.0',
            'pytest~=6.2',
            'pytest-html~=2.1',
            'pyhamcrest~=2.0',
            # 'flake8-docstrings>=1.0.0',
        ],
    },
)
