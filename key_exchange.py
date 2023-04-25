def generate_shared_key():
    alice = pyDH.DiffieHellman()
    alice_pubkey = alice.gen_public_key()

    bob = pyDH.DiffieHellman()
    bob_pubkey = bob.gen_public_key()

    alice_shared_key = alice.gen_shared_key(bob_pubkey)
    bob_shared_key = bob.gen_shared_key(alice_pubkey)

    assert alice_shared_key == bob_shared_key
    return alice_shared_key
