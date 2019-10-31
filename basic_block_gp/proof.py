import hashlib
import json
from time import time
from uuid import uuid4



def proof_of_work(block):
    """
    Simple Proof of Work Algorithm
    Stringify the block and look for a proof.
    Loop through possibilities, checking each one against `valid_proof`
    in an effort to find a number that is a valid proof
    :return: A valid proof for the provided block
    """
    # Proof is a SHA256 hash with 3 leading zeroes
    block_string = json.dumps(block, sort_keys=True).encode()
    proof = 0
    while not valid_proof(block_string, proof):
        proof += 1
    return proof


def valid_proof(block_string, proof):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 3
    leading zeroes?  Return true if the proof is valid
    :param block_string: <string> The stringified block to use to
    check in combination with `proof`
    :param proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.
    :return: True if the resulting hash is a valid proof, False otherwise
    """
    guess = f'{block_string}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    if guess_hash[:3] == "000":
        print(guess)
    return guess_hash[:3] == "000"


if __name__ == "__main__":
    proof = proof_of_work("abc")
    print(proof)

    print(hashlib.sha256(b'b\'"abc"\'1423').hexdigest())