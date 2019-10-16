import boto3
import yaml

CFG_STACK_NAME = 'stack_name'

def load_config():
		with open("config.yml", "r") as f:
			return yaml.safe_load(f)

def cf_client(config):
	session = boto3.Session(
		aws_access_key_id=config['aws_access_key_id'], aws_secret_access_key=config['aws_secret_access_key'], region_name=config['region_name'])
	return session.client('cloudformation')
	
def find_stack(client, stack_name):
	stacks = client.describe_stacks()['Stacks']
	stack = [s for s in stacks if s['StackName'] == stack_name]
	if stack:
		return stack[0]
	else:
			return None
