# (c) 2022 @mdjoerg

# 1. import required libaries
from pydeen.auth import AuthBasic
from pydeen.sap_abap import SAPAbapHttpBackend, SAPAbapODataConnector

# 2. enter your sap backend connection details
# Example - SAP CAL Demo
sap_host = "http://10.17.30.19:50000"
sap_client = "110" 
sap_name = "S4H110"

# 3. load authentification or open menu for interaction
auth = AuthBasic()
auth.set_menu_context(sap_name)
if not auth.load_config(auth.get_menu_filename()):
    auth.menu()

# 4. open a SAP backend with OData connector
backend = SAPAbapHttpBackend(sap_name, sap_host, sap_client, auth=auth)
connector = SAPAbapODataConnector(backend)

# 5. open the sap OData connector menu for interaction: select endpoint + entity, select, get as pandas dataframe
connector.menu()

# 6. get the last selection as raw result
result = connector.get_current_result()
print(result)

# 7. get the last selection as pandas dataframe object
df = connector.get_current_result_as_pandas_df()
df.head()
df.info()

# 8. start step 5..7 again...