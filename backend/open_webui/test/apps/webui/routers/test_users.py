from test.util.abstract_integration_test import AbstractPostgresTest
from test.util.mock_user import mock_webui_user


def _get_user_by_id(data, user_id):
    return next((item for item in data if item["id"] == user_id), None)


class TestUsers(AbstractPostgresTest):
    BASE_PATH = "/api/v1/users"

    def setup_class(cls):
        super().setup_class()
        from open_webui.models.users import Users

        cls.users = Users

    def setup_method(self):
        super().setup_method()
        self.users.insert_new_user(
            id="1",
            name="user 1",
            email="user1@openwebui.com",
            profile_image_url="/user1.png",
            role="user",
        )
        self.users.insert_new_user(
            id="2",
            name="user 2",
            email="user2@openwebui.com",
            profile_image_url="/user2.png",
            role="user",
        )

    def test_users_admin_and_profile_flows(self):
        with mock_webui_user(id="3", role="admin"):
            response = self.fast_api_client.get(self.create_url(""))
        assert response.status_code == 200
        payload = response.json()
        assert payload["total"] == 2
        assert _get_user_by_id(payload["users"], "1") is not None
        assert _get_user_by_id(payload["users"], "2") is not None

        with mock_webui_user(id="3", role="admin"):
            response = self.fast_api_client.post(
                self.create_url("/2/update"),
                json={
                    "role": "admin",
                    "name": "user 2 updated",
                    "email": "user2-updated@openwebui.com",
                    "profile_image_url": "/user2-updated.png",
                },
            )
        assert response.status_code == 200
        assert response.json()["role"] == "admin"

        with mock_webui_user(id="2", role="admin"):
            response = self.fast_api_client.get(self.create_url("/user/settings"))
        assert response.status_code == 200
        assert response.json() is None

        with mock_webui_user(id="2", role="admin"):
            response = self.fast_api_client.post(
                self.create_url("/user/settings/update"),
                json={
                    "ui": {"attr1": "value1", "attr2": "value2"},
                    "model_config": {"attr3": "value3", "attr4": "value4"},
                },
            )
        assert response.status_code == 200

        with mock_webui_user(id="2", role="admin"):
            response = self.fast_api_client.get(self.create_url("/user/settings"))
        assert response.status_code == 200
        assert response.json() == {
            "ui": {"attr1": "value1", "attr2": "value2"},
            "model_config": {"attr3": "value3", "attr4": "value4"},
        }

        with mock_webui_user(id="1", role="user"):
            response = self.fast_api_client.get(self.create_url("/user/info"))
        assert response.status_code == 200
        assert response.json() is None

        with mock_webui_user(id="1", role="user"):
            response = self.fast_api_client.post(
                self.create_url("/user/info/update"),
                json={"attr1": "value1", "attr2": "value2"},
            )
        assert response.status_code == 200

        with mock_webui_user(id="1", role="user"):
            response = self.fast_api_client.get(self.create_url("/user/info"))
        assert response.status_code == 200
        assert response.json() == {"attr1": "value1", "attr2": "value2"}

        with mock_webui_user(id="3", role="admin"):
            response = self.fast_api_client.get(self.create_url("/2"))
        assert response.status_code == 200
        assert response.json()["name"] == "user 2 updated"

        with mock_webui_user(id="3", role="admin"):
            response = self.fast_api_client.delete(self.create_url("/2"))
        assert response.status_code == 200
        assert response.json() is True

        with mock_webui_user(id="3", role="admin"):
            response = self.fast_api_client.get(self.create_url(""))
        assert response.status_code == 200
        assert response.json()["total"] == 1
