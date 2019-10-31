import hashlib
import json
from time import time
from uuid import uuid4



def proof_of_work(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    proof = 0
    while not valid_proof(block_string, proof):
        proof += 1
    return proof


def valid_proof(block_string, proof):
    guess = f'{block_string}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    if guess_hash[:3] == "000":
        print(guess)
    return guess_hash[:3] == "000"


if __name__ == "__main__":
    proof = proof_of_work("abc")
    print(proof)
    print(hashlib.sha256(b'b\'"abc"\'1423').hexdigest())