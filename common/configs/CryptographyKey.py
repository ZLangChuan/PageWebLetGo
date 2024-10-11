from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class CryptographyKey:

    def __init__(self) -> None:
        self.file_path = "common/configs/"
        self.private_key_name = "private_key.pem"
        self.public_key_name = "public_key.pem"

    def create_key(self):

        # call rsa.generate_private_key
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )
        public_key = private_key.public_key()

        # store private key
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        with open(f"{self.file_path}{self.private_key_name}", "wb") as f:
            f.write(pem)

        # stroe public key
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        with open(f"{self.file_path}{self.public_key_name}", "wb") as f:
            f.write(pem)

        print("Key generated successfully!!!!!!!!!!!!!")

    def get_key(self, key_type="public"):
        if key_type == "private":
            with open(f"{self.file_path}{self.private_key_name}", "rb") as key_file:
                key = serialization.load_pem_private_key(
                    key_file.read(), password=None, backend=default_backend()
                )
                return key
        elif key_type == "public":
            with open(f"{self.file_path}{self.public_key_name}", "rb") as key_file:
                key = serialization.load_pem_public_key(
                    key_file.read(), backend=default_backend()
                )
                return key


if __name__ == "__main__":
    import jwt

    cryptography_key = CryptographyKey()
    # cryptography_key.create_key()

    data = {
        "avater": "string",
        "create_time": 1724998842035,
        "create_user_id": 0,
        "delete_time": None,
        "delete_user_id": None,
        "email": "user@example.com",
        "has_activate": 0,
        "has_delete": 0,
        "id": 0,
        "password": "string",
        "r_password": "string",
        "role_id": 0,
        "update_time": 1724998842035,
        "username": "string",
    }

    encoded_jwt = jwt.encode(
        data, cryptography_key.get_key(key_type="private"), algorithm="RS256"
    )

    decoded_jwt = jwt.decode(
        encoded_jwt, cryptography_key.get_key(key_type="public"), algorithms=["RS256"]
    )
    print(decoded_jwt)
