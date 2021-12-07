from sandbox import Sandbox
from budget import Budget
from cloudformation import CloudFormation
from configuration import Configuration
from authentication import Authentication
from referential import Referential

amount = '500'
recipient = 'someone@socgen.com'
env = 'local'
account_id = "1234"

if __name__ == '__main__':
	conf = Configuration(env)
	auth = Authentication()
	scl_creds = auth.authenticate()
	sbx_creds = auth.authenticate()
	sandbox = Sandbox(
				account_id = account_id,
				socle_credentials = scl_creds,
				config = conf,
				budget = Budget(
								config = conf,
								cfn = CloudFormation(sbx_creds),
								amount = amount, 
								recipient = recipient
								),
				referential = Referential(scl_creds)
			 )
	sandbox.set_budget()