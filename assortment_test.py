import sys, os
sys.path.insert(0, os.path.expanduser('~/Galaxy_Box_Integration/'))
from galaxy_api_class import gx_api

gx = gx_api(database='PRODUCT',production = True)
params =  params = {
            'query':[{
            'c_WA_Launch_Date_Earliest':'8/14/2023',
            'omit': "false"
            }]
        }
gx.find_records(params = params, layout = 'Product_Assortment-Detail_View')
