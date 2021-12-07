from cloudformation import CloudFormation
from configuration import Configuration


class Budget:
	def __init__(self, config: Configuration, cfn: CloudFormation, amount: str, recipient:str):
		self.amount = amount
		self.recipient = recipient
		self.cfn = cfn
		self.config = config

	def deploy_budget(self):
		self.cfn.deploy_stack()