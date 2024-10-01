from dotenv import load_dotenv
import os
import requests
import json
from datetime import datetime

# load secrets
load_dotenv()

class LuccaAPI:
    def __init__(self, base_url, token, path_list=None, field_list=None):
        '''
        Initilisation de l'API avec l'URL de base et le token d'identifications
        '''
        self.base_url = base_url
        self.headers = {
            'Accept': "application/json",
            'Authorization': f"lucca application=\u007b{token}\u007d"
        }
        # define paths
        self.path_list = {
            'users': '/api/v3/users',
            'departments': '/api/v3/departments',
            'contracts': '/directory/api/4.0/work-contracts'
        }
        # and list of fields that would be extract from API
        self.field_list = {
            'users_fields': ['id', 'address', 'firstName', 'lastName', 'gender', 'login', 'mail', 'birthDate', 'employeeNumber', 'jobTitle', 'dtContractStart', 'dtContractEnd', 'legalEntity.name', 'department.id', 'department.name', 'manager.id', 'manager.name', 'applicationData', 'rolePrincipal.name', 'habilitedRoles.name'],
            'departments_fields': ['id', 'name', 'code', 'hierarchy', 'parentId', 'isActive', 'position', 'level', 'head.id', 'users.id', 'currentUsers.id'],
            'contracts_fields': ['id', 'ownerId', 'startsOn', 'endsOn', 'spc', 'type', 'lastModifierId', 'createdAt', 'lastModifiedAt']
        }

    def get(self, endpoint, **params):
        '''
        Initilisation de l'API avec l'URL de base et le token d'identifications
        '''
        url = f'{base_url}{self.path_list[endpoint]}'

        try:
            response = requests.get(url, headers=self.headers, params=params)

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_error:
            print(f"HTTP error: {http_error}")
        except Exception as error:
            print(f"Error: {error}")
        return None

    def export_data(self, entity, json_obj, **params):
        '''
        Initilisation de l'API avec l'URL de base et le token d'identifications
        '''
        with open(f'{entity}.json', 'w', encoding='utf-8') as f:
            json.dump(json_obj, f, ensure_ascii=False, indent=4)
        return None

    def get_users(self, all_users, **params):
        '''
        Initilisation de l'API avec l'URL de base et le token d'identifications
        '''
        params = {'fields': self.field_list['users_fields']}
        if all_users:
            params['formerEmployees'] = 'true'
        return self.get('users', **params)

    def get_departments(self, **params):
        '''
        Initilisation de l'API avec l'URL de base et le token d'identifications
        '''
        params = self.get_list_department_id()
        params['fields'] = self.field_list['departments_fields']
        return self.get('departments', **params)

    def get_contracts(self, **params):
        '''
        Initilisation de l'API avec l'URL de base et le token d'identifications
        '''
        params = self.get_list_owner_id()
        params['limit'] = len(self.get_users(all_users=True)['data']['items'])*2
        params['fields'] = self.field_list['contracts_fields']
        return self.get('contracts', **params)

    def get_list_owner_id(self, **params):
        '''
        Initilisation de l'API avec l'URL de base et le token d'identifications
        '''
        users = self.get_users(all_users=True, **params)
        owner_ids_values = ','.join(map(str, list(set([user['id'] for user in users['data']['items']]))))
        owner_ids = {"id": owner_ids_values}
        return owner_ids

    def get_list_department_id(self, **params):
        '''
        Initilisation de l'API avec l'URL de base et le token d'identifications
        '''
        users = self.get_users(all_users=True, **params)
        department_ids_values = ','.join(map(str, list(set([user['department']['id'] for user in users['data']['items']]))))
        department_ids = {"id": department_ids_values}
        return department_ids

if __name__ == "__main__":
    base_url = os.getenv("API_URL")
    token = os.getenv("API_TOKEN")

    api = LuccaAPI(base_url, token)

    users = api.get_users(all_users=True)
    departments = api.get_departments()
    contracts = api.get_contracts()

    api.export_data('users', users)
    api.export_data('departments', departments)
    api.export_data('contracts', contracts)
