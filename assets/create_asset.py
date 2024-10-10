from algosdk import algod, mnemonic, transaction
from algosdk.future import transaction

# Replace with your Algorand account's mnemonic
mnemonic_phrase = "YOUR_MNEMONIC_HERE"
account = mnemonic.to_private_key(mnemonic_phrase)

# Connect to Algorand network
algod_address = "http://localhost:4001"  # Algod API Address
algod_token = "YOUR_ALGOD_TOKEN"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Function to create asset
def create_asset():
    params = algod_client.suggested_params()
    txn = transaction.AssetCreateTxn(
        sender=account,
        sp=params,
        total=10000,  # Total supply
        default_frozen=False,
        unit_name="DAIRY",
        asset_name="Dairy Product Token",
        manager=None,
        reserve=None,
        freeze=None,
        clawback=None,
        url="http://example.com",  # URL for more information
        metadata_hash=None
    )
    signed_txn = txn.sign(account)
    txn_id = algod_client.send_transaction(signed_txn)
    transaction.wait_for_confirmation(algod_client, txn_id)
    print(f"Asset created with ID: {txn_id}")

create_asset()
