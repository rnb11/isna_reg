class URLHandler:
    def __init__(self, is_test):
        self.is_test = is_test
        if is_test:
            self.base_url = "adamants"
            self.db_config = {
                "host": "172.158.0.15",
                "port": "5432",
                "database": "isna_reg",
                "user": "isna",
                "password": "123456"
            }
        else:
            self.base_url = "isna"
            self.db_config = {
                "host": "172.158.0.12",
                "port": "5438",
                "database": "isna_reg",
                "user": "isna",
                "password": "WC9tJWMVUxUMvm85"
            }

    def get_url(self):
        return "https://arm." + self.base_url + ".kz"

    def get_url_for_esb(self, is_sync):
        if is_sync:
            return "https://esb." + self.base_url + ".kz/sync/eis"
        return "https://esb." + self.base_url + ".kz/async/eis"

    def get_url_for_authorization(self):
        if self.is_test:
            return "https://keycloak-isna." + self.base_url + ".kz/auth/realms/jhipster/protocol/openid-connect/token"
        return "https://keycloak-arm." + self.base_url + ".kz/auth/realms/jhipster/protocol/openid-connect/token"