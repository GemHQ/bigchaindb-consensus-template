import pytest
from conftest import PLUGIN_NAME, PLUGIN_CLASS

@pytest.fixture
def mock_valid_transaction():
    pass

@pytest.fixture
def mock_invalid_transaction():
    pass

@pytest.fixture
def mock_unsigned_transaction():
    pass

@pytest.fixture
def mock_valid_block():
    pass

@pytest.fixture
def mock_invalid_block():
    pass

@pytest.mark.xfail(reason='no test fixtures yet')
class TestConsensusRules:
    def test_valid_transactions_validate(b, mock_valid_transaction):
        assert PLUGIN_CLASS.validate_transaction(b, mock_valid_transaction) == \
            mock_valid_transaction

    def test_invalid_transactions_raise_errors(b, mock_invalid_transaction):
        with pytest.raises(Exception):
            PLUGIN_CLASS.validate_transaction(b, mock_invalid_transaction)

    def test_unsigned_transactions_can_be_signed(b, mock_unsigned_transaction):
        assert PLUGIN_CLASS.verify_signature(mock_unsigned_transaction) == False
        assert PLUGIN_CLASS.verify_signature(
            PLUGIN_CLASS.sign_transaction(b, mock_unsigned_transaction)) == True

    def test_valid_blocks_validate(b, mock_valid_block):
        assert PLUGIN_CLASS.validate_block(b, mock_valid_block) == mock_valid_block

    def test_invalid_blocks_raise_errors(b, mock_invalid_block):
        with pytest.raises(Exception):
            PLUGIN_CLASS.validate_block(b, mock_invalid_block)

    def test_verify_signature_returns_true_for_valid(mock_valid_transaction):
        assert PLUGIN_CLASS.verify_signature(mock_valid_transaction) == True

    def test_verify_signature_returns_false_for_invalid(mock_unsigned_transaction):
        assert PLUGIN_CLASS.verify_signature(mock_unsigned_transaction) == False
