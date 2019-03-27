from setuptools import setup

REQUIREMENTS = [
    'requests'
]

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-cov'
]

setup(
    name='yadummy',
    version='0.0.1',
    description="Yet Another Dummy Project",
    author="Madh93",
    author_email='mhdez@protonmail.com',
    url='https://github.com/Madh93/yadummy',
    packages=['yadummy'],
    install_requires=REQUIREMENTS,
    extras_require={'test': TEST_REQUIREMENTS},
    scripts=['bin/yadummy'],
    keywords=['dummy'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='pytest',
)
