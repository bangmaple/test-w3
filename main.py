from fastapi import FastAPI
import web3
import json
from hexbytes import HexBytes


#test get contract address https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7



app = FastAPI()
w3 = web3.Web3(web3.HTTPProvider('https://mainnet.infura.io/v3/6ff607b0891447e8a23ad05f4f10add2'))


@app.get("/transaction/{hash}")
async def get_transaction_hash(hash: str):
    tx = w3.eth.get_transaction(hash)
    tx_dict = dict(tx)
    print(w3.to_json(tx_dict))
    return w3.to_json(tx_dict)


@app.get("/filter/{address}")
async def root(address: str):
    print(address)
    ff = w3.eth.filter({
        "address": address,
    })
    return w3.to_json(ff.get_all_entries())
