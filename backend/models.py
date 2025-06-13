from datetime import date
from hashlib import sha256
from string import ascii_letters, digits
from uuid import UUID, uuid4

from pydantic import BaseModel, SecretBytes

from auth.password_manager import PasswordManager

class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    username: str
    # email: EmailStr
    email: str
    date_of_birth: date
    password: str
    # password: SecretStr
    password_hash: SecretBytes = ""

    # Hash Password
    @classmethod
    def _hash_password(cls):
        cls.password_hash = PasswordManager.hash_password(cls.password)


#  ________________________| Short URL |________________________


class ShortURL:
    _ALPHA_NUMS = ascii_letters + digits

    original_url: str
    metrics: dict = {}
    created_at: str = ""
    short_url: str
    uuid: UUID
    slug: str

    def __init__(
        self,
        url: str,
    ):
        uuid = uuid4()
        temp = uuid

        # Sha256 hashed into hexadecimals and base62 encoded, then first 5 chars taken
        slug = self._int_to_base(int(sha256(str(temp).encode()).hexdigest(), 16))[:5]

        self.slug = slug
        self.uuid = uuid
        self.original_url = url
        self.short_url = f"customdomain.com/{slug}"

    def _int_to_base(self, n, len: int = 0):
        chars = []
        while n > 0:
            n, rem = divmod(n, 62)
            chars.append(self._ALPHA_NUMS[rem])
        return "".join(reversed(chars)).zfill(len)
