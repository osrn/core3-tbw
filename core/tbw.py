#!/usr/bin/env python
from config.configure import Configure
from network.network import Network
from modules.allocate import Allocate
from modules.blocks import Blocks
from modules.initialize import Initialize
from modules.payments import Payments
from modules.stage import Stage
from modules.voters import Voters
from utility.database import Database
from utility.sql import Sql
from utility.utility import Utility


if __name__ == '__main__':
    print("Start Script")
    # get configuration
    config = Configure()
    #load network
    network = Network(config.network)
    #load utility
    utility = Utility(network)
    # connect to core and tbw script database
    database = Database(config, network)
    sql = Sql()
    # check if initialized
    Initialize(config, database, sql)
    # process blocks
    # Blocks(config, database, sql)
    sql.open_connection()
    database.open_connection()
    # get last block to start
    last_block = sql.last_block().fetchall()
    # use last block timestamp to get all new blocks
    new_blocks = database.get_limit_blocks(last_block[0][0])
    # store all new blocks
    sql.store_blocks(new_blocks)
    # get unprocessed blocks
    unprocessed_blocks = sql.unprocessed_blocks.fetchall()
    print(len(unprocessed_blocks))
    
    sql.close_connection()
    database.close_connection()    
    
    quit()
    # allocate block rewards
    Allocate(config, sql)
    quit()
    # stage payments
    Stage(config, sql)
    quit()
    # process payment
    Payments(config, sql)
    quit()
    
    print("End Script")
