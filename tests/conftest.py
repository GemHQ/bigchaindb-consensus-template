import pytest

# PLUGIN_CLASS should be the class that inherits from
#   `bigchaindb.consensus.AbstractConsensusRules`
from consensus_template.consensus import ConsensusRulesTemplate
PLUGIN_CLASS = ConsensusRulesTemplate

# PLUGIN_NAME is the name (left of the equal-sign) of the entry_point you set
#   in setup.py
PLUGIN_NAME = 'PLUGIN_NAME'

@pytest.fixture
def default_config(monkeypatch):
    config = {
        'database': {
            'host': 'host',
            'port': 28015,
            'name': 'bigchain',
        },
        'keypair': {
            'public': 'pubkey',
            'private': 'privkey',
        },
        'keyring': [],
        'CONFIGURED': True,
        'consensus_plugin': 'default'
    }

    monkeypatch.setattr('bigchaindb.config', config)

    return config

@pytest.fixture
def plugin_config(default_config, monkeypatch):
    default_config.update({'consensus_plugin': PLUGIN_NAME})
    monkeypatch.setattr('bigchaindb.config', default_config)
    return default_config

@pytest.fixture
def restore_config(plugin_config):
    from bigchaindb import config_utils
    config_utils.dict_config(plugin_config)

@pytest.fixture
def b(restore_config):
    from bigchaindb import Bigchain
    return Bigchain()
