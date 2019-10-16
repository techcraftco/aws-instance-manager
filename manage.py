from common import *

config = load_config()
stack_name = config[CFG_STACK_NAME]
	
cf = cf_client(config)
		
# see if the stack already exists
stack = find_stack(cf, stack_name)

# create the stack parameters
p = {'AmiId': config['ami_id'], 'KeyPair': config['key_pair']}
params = [{'ParameterKey': k, 'ParameterValue': p[k]} for k in p]

# read the CloudFormation template body
with open("cf.yml", "r") as f:
	template = f.read()
	
if stack:
	print("Stack already exists, updating...")
	cf.update_stack(StackName = stack_name, TemplateBody = template, Parameters = params)
	waiter = cf.get_waiter('stack_update_complete')
else:
	print("No existing stack, creating...")
	cf.create_stack(StackName = stack_name, TemplateBody = template, Parameters = params)
	waiter = cf.get_waiter('stack_create_complete')
	
waiter.wait(StackName = stack_name)
print("Done.")
