# (c) 2022 @mdjoerg
# New fetaures in version 0.8.0
# - more object menu usage
# - pick single records
# - transfer results via datahub feature 

# 1. import required libaries
from pydeen.auth import AuthBasic
from pydeen.sap_abap import SAPAbapHttpBackend, SAPAbapODataConnector
from pydeen.types import Factory
from pydeen.pandas import PandasResultDataframe


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
# use the new features for single record selection, open specific menus, export data to datahub
# use "test1" .. "testx" as key for datahub
connector.menu()


# 6. get access to datahub and open menu
datahub = Factory.get_datahub()
datahub.menu()


# 7. use the datahub for get extraction results
if datahub.get_count() == 0:
    print("no objects found in datahub")
else:
# 8. check given objects
    keys = datahub.get_key_list()
    print("Objects found in Datahub:")
    for key in keys:
        print(key, datahub.get_object(key))    

# 9. get an object via key and open menu
    entered_key = ""
    while not entered_key is None:
        entered_key = input("Enter datahub key (enter for quit): ")
        if entered_key == "" or entered_key == None:
            break
        else:
            # get datahub object
            object = datahub.get_object(entered_key)
            print("Open menu for object: ", object)
            # open object menu
            object.menu()

