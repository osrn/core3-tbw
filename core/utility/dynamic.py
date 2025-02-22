class Dynamic:
    def __init__(self, utility, config):
        self.client = utility.get_client()
        self.config = config
        
    
    def get_dynamic_fee(self):        
        try:
            node_configs = self.client.node.configuration()['data']['transactionPool']['dynamicFees']
            if node_configs['enabled'] == "False":
                transaction_fee = int(0.1 * self.config.atomic)
            else:
                dynamic_offset = node_configs['addonBytes']['transfer']
                fee_multiplier = node_configs['minFeePool']
                standard_tx = 230
                v_msg = len(self.config.message) 
                tx_size = standard_tx + v_msg
                #calculate transaction fee
                transaction_fee = self.calculate_dynamic_fee(dynamic_offset, tx_size, fee_multiplier)
        except:
            transaction_fee = int(0.1 * self.config.atomic)

        return transaction_fee
    
    
    def get_dynamic_fee_multi(self, numtx):
         try:
             node_configs = self.client.node.configuration()['data']['transactionPool']['dynamicFees']
             if (node_configs['enabled'] == "False"):
                 transaction_fee = int(0.1 * self.config.atomic)
             else:
                 dynamic_offset = node_configs['addonBytes']['multiPayment']
                 fee_multiplier = node_configs['minFeePool']

                 # get size of transaction
                 multi_tx = 125
                 second_sig = 64
                 per_tx_fee = 29
                 v_msg = len(self.config.msg) 
                 tx_size = multi_tx + v_msg + second_sig + (numtx * per_tx_fee)

                 # calculate transaction fee
                 transaction_fee = self.calculate_dynamic_multifee(dynamic_offset, tx_size, fee_multiplier)

         except:
             transaction_fee = int(0.1 * self.config.atomic)

         return transaction_fee
    
    
    def calculate_dynamic_fee(self, t, s, c):
        return int((t+s)*c)

    
    def calculate_dynamic_multifee(self, t, s, c):
         fee = int((t + (round(s/2) + 1)) * c)
         return fee
    
    
    def get_multipay_limit(self):
        try:
            limit = int(self.client.node.configuration()['data']['constants']['multiPaymentLimit'])
        except:
            limit = 20
        return limit
    
    
    def get_tx_request_limit(self):
        try:
            limit = self.client.node.configuration()['data']['transactionPool']['maxTransactionsPerRequest']
        except:
            limit = 20
        return limit
    
