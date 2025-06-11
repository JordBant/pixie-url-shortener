from datetime import date
from hashlib import sha256
from string import ascii_letters, digits
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, SecretBytes, SecretStr

# ________________________| Data Classes |________________________

class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    date_of_birth: date
    password: SecretStr
    password_hash: SecretBytes = ""

    # Hash Password
    @classmethod
    def hash_password(cls): 



class IShortURLInitPayload(BaseModel):
    new_url: str


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
        new_url: str,
    ):
        uuid = uuid4()
        temp = uuid

        # Sha256 hashed into hexadecimals and base62 encoded, then first 5 chars taken
        slug = self._int_to_base(int(sha256(str(temp).encode()).hexdigest(), 16))[:5]

        self.slug = slug
        self.uuid = uuid
        self.original_url = new_url
        self.short_url = f"customdomain.com/{slug}"

    def _int_to_base(self, n, len: int = 0):
        chars = []
        while n > 0:
            n, rem = divmod(n, 62)
            chars.append(self._ALPHA_NUMS[rem])
        return "".join(reversed(chars)).zfill(len)


#  __________________________| User |__________________________


class User:
    # all_short_urls: dict[str, ShortURL] = {}
    # all_original_urls: list[str] = []
    id: str
    first_name: str
    last_name: str
    username: str
    date_of_birth: date
    email: EmailStr
    _password_hash: SecretStr

    # def __init__(self, user_info: IUser):

    # Call DB on username to check if exists

    # def add_url(self, user_infor: IUser) -> None:
    #     if url in self.all_original_urls:
    #         raise Exception("This url already exists")

    #     new_short_url = ShortURL({"new_url": url, "created_at": ""})
    #     self.shortened_urls[new_short_url.short_url] = new_short_url

    # def delete_url(self, short_url: str) -> None:
    #     if self.all_short_urls[short_url]:
    #         del self.all_short_urls[short_url]
    #     else:
    #         raise KeyError(f"The key '{short_url}' doesn't exist on your account.")

    # def edit_url(self, short_url_key, payload: IShortURLInitPayload):
    #     if not self.all_short_urls[short_url_key]:
    #         raise KeyError(f"The key '{short_url_key}' doesn't exist on your account.")
    #     for item in payload:
    #         self.all_short_urls[short_url_key] = payload[item]
