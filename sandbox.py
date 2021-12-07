from budget import Budget
from configuration import Configuration
from referential import Referential

class Sandbox:
	def __init__(self, socle_credentials, config: Configuration, budget: Budget, referential: Referential, account_id = None):
		self.budget  = budget
		self.config = config
		self.referential = referential
		self.socle_credentials = socle_credentials
		if not account_id:
			self.account_id = self.get_available_id()
		else:
			self.account_id = account_id
		self.props = {"key": "value"}

	def set_budget(self):
		self.budget.deploy_budget()
		self.referential.update_account_info(self.account_id, self.props)

	def get_available_id(self):
		return "42"