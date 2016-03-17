"""
BigchainDB Consensus Template: A template for consensus rules plugins for BigchainDB
"""
from setuptools import setup

tests_require = [
    'pytest',
    'pep8',
    'pylint',
    'pytest',
]

dev_require = [
    'ipdb',
    'ipython',
]

docs_require = [
]

setup(
    name='BigchainDB Consensus Template',
    version='0.0.1',
    description='BigchainDB consensus plugin for permissioned document chains',
    long_description=__doc__,
    url='https://github.com/GemHQ/bigchaindb-consensus-template/',
    author='Matt Smith',
    author_email='matt@gem.co',
    zip_safe=False,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Software Development',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
    ],

    packages=[
        'consensus_template'
    ],

    # Replace `PLUGIN_NAME` with a unique, unambiguous name to identify your
    # rules. You can also add multiple entry_points for different rules sets.
    entry_points={
        'bigchaindb.consensus': [
            'PLUGIN_NAME=consensus_template.consensus:ConsensusRulesTemplate'
        ]
    },

    install_requires=[
        'bigchaindb==0.1.4'
    ],
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'dev':  dev_require + tests_require + docs_require,
        'docs':  docs_require,
    },
)
