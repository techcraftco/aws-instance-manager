from common import *

import clipboard
		
config = load_config()
cf = cf_client(config)

stack_name = config[CFG_STACK_NAME]
stack = find_stack(cf, stack_name)

if not stack:
	print("Stack not running. Use manage.py to create it.")
else:
	outputs = stack['Outputs']
	dnsName = [o['OutputValue'] for o in outputs if o['OutputKey'] == 'instanceDnsName'][0]
	print(dnsName)
	clipboard.set(dnsName)
