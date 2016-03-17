import pytest
from conftest import PLUGIN_CLASS, PLUGIN_NAME


def test_bigchain_class_file_initialization(plugin_config):
    from bigchaindb.core import Bigchain
    bigchain = Bigchain()
    assert bigchain.consensus == PLUGIN_CLASS


def test_bigchain_class_initialization_with_parameters(default_config):
    from bigchaindb.core import Bigchain
    bigchain = Bigchain()
    assert bigchain.consensus != PLUGIN_CLASS

    bigchain = Bigchain(**{'consensus_plugin': PLUGIN_NAME})
    assert bigchain.consensus == PLUGIN_CLASS
