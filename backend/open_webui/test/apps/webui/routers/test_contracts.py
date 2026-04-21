from test.util.abstract_integration_test import AbstractPostgresTest
from test.util.mock_user import mock_webui_user


class TestApiContracts(AbstractPostgresTest):
    BASE_PATH = '/api/v1'

    def setup_class(cls):
        super().setup_class()
        from open_webui.models.auths import Auths

        cls.auths = Auths

    def test_auth_signin_response_contract(self):
        from open_webui.utils.auth import get_password_hash

        self.auths.insert_new_auth(
            email='contract.user@openwebui.com',
            password=get_password_hash('password'),
            name='Contract User',
            profile_image_url='/contract.png',
            role='user',
        )

        response = self.fast_api_client.post(
            self.create_url('/auths/signin'),
            json={'email': 'contract.user@openwebui.com', 'password': 'password'},
        )
        assert response.status_code == 200

        payload = response.json()
        assert set(payload.keys()) >= {
            'id',
            'email',
            'name',
            'role',
            'token',
            'token_type',
            'profile_image_url',
        }
        assert payload['token_type'] == 'Bearer'

    def test_models_list_response_contract(self):
        with mock_webui_user(id='contract-admin', role='admin'):
            response = self.fast_api_client.get(self.create_url('/models/list'))

        assert response.status_code == 200
        payload = response.json()
        assert set(payload.keys()) == {'items', 'total'}
        assert isinstance(payload['items'], list)
        assert isinstance(payload['total'], int)
