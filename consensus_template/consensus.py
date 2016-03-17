from bigchaindb.consensus import BaseConsensusRules

# Unbound super requires both arguments to get the correct behavior with
# staticmethods
def sup():
    return super(ConsensusRulesTemplate,
                 ConsensusRulesTemplate)

class ConsensusRulesTemplate(BaseConsensusRules):


    @staticmethod
    def validate_transaction(bigchain, transaction):
        """Validate a transaction.

        Args:
            bigchain (Bigchain): an instantiated ``bigchaindb.Bigchain`` object.
            transaction (dict): transaction to validate.

        Returns:
            The transaction if the transaction is valid else it raises an
            exception describing the reason why the transaction is invalid.

        Raises:
            Descriptive exceptions indicating the reason the transaction failed.
            See the `exceptions` module for bigchain-native error classes.
        """
        print("Hey! You're using validate_transaction from your own consensus "
              "rules now!")
        return sup().validate_transaction(bigchain, transaction)

    @staticmethod
    def validate_block(bigchain, block):
        """Validate a block.

        Args:
            bigchain (Bigchain): an instantiated ``bigchaindb.Bigchain`` object.
            block (dict): block to validate.

        Returns:
            The block if the block is valid else it raises an exception
            describing the reason why the block is invalid.

        Raises:
            Descriptive exceptions indicating the reason the block failed.
            See the `exceptions` module for bigchain-native error classes.
        """
        print("Hey! You're using validate_block from your own consensus "
              "rules now!")
        return sup().validate_block(bigchain, block)

    @staticmethod
    def create_transaction(*args, **kwargs):
        """Create a new transaction.

        Args:
            The signature of this method is left to plugin authors to decide.

        Returns:
            dict: newly constructed transaction.
        """
        print("Hey! You're using create_transaction from your own consensus "
              "rules now!")
        return sup().create_transaction(*args, **kwargs)

    @staticmethod
    def sign_transaction(transaction, *args, **kwargs):
        """Sign a transaction.

        Args:
            transaction (dict): transaction to sign.
            any other arguments are left to plugin authors to decide.

        Returns:
            dict: transaction with any signatures applied.
        """
        print("Hey! You're using sign_transaction from your own consensus "
              "rules now!")
        return sup().sign_transaction(transaction, *args, **kwargs)

    @staticmethod
    def verify_signature(signed_transaction):
        """Verify the signature of a transaction.

        Args:
            signed_transaction (dict): signed transaction to verify

        Returns:
            bool: True if the transaction's required signature data is present
                and correct, False otherwise.
        """
        print("Hey! You're using validate_signature from your own consensus "
              "rules now!")
        return sup().verify_signature(signed_transaction)
