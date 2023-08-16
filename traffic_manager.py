import sys, os
from pprint import pprint as print
from datetime import date
sys.path.insert(0, os.path.expanduser('~/Galaxy_Box_Integration/'))
from galaxy_api_class import gx_api


class controller:
    def __init__(self):
        self.gx = gx_api(production = False)
        

    def get_assignables(self):
        # get all assignable images (unsorted)
        today = date.today().strftime("%m/%d/%Y")
        end_date = today.split('/')
        end_date = str(int(end_date[0])+3)+"/"+end_date[1]+'/'+end_date[2]
        launch_date_range = f'{today}...{end_date}'
        params = {
            'query':[{
            'c_WA_Launch_Date_Earliest':launch_date_range,
            'RetouchStatus':'Ready for Revisions',
            'RetoucherName':'=',
            'omit': "false"
            }]
        }
        results = self.gx.find_records(params, layout = "Retoucher_DetailView")
        # abort if no data in the response
        if 'response' not in results or 'data' not in results['response']: return -1
        self.assignables = results['response']['data']
        

        # later, we'll determine how to assign them
        

traffic = controller()
traffic.get_assignables()