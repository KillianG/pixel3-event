from web3 import Web3
import json
import asyncio
from contract import ADDRESS, ABI

bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(bsc))

contract_abi = ABI
contract_address = Web3.toChecksumAddress(ADDRESS)
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

event_filter = contract.events.colorChanged.createFilter(fromBlock='latest')
loop = asyncio.get_event_loop()


def handle_event(event):
    ev = json.loads(Web3.toJSON(event))
    print(ev)


async def log_loop(event_filter, poll_interval):
    while True:
        try:
            for PairCreated in event_filter.get_new_entries():
                handle_event(PairCreated)
            await asyncio.sleep(poll_interval)
        except ValueError as e:
            print(e)
            await asyncio.sleep(poll_interval)


try:
    loop.run_until_complete(asyncio.gather(log_loop(event_filter, 2)))
finally:
    print("finally")
