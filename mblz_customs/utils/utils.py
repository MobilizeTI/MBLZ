import requests
import json
from odoo.exceptions import UserError

class Api():
    
    def send_to_api(self, args):
        url = self.env.user.company_id.mblz_api_url
        endpoint = '/{}'.format(args.get('endpoint'))
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(args)
        response = requests.post(url + endpoint, headers=headers, data=data)
        if response.status_code == 200:
            return json.loads(response.text)
        return False