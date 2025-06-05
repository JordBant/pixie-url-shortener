import hashlib
from dataclasses import dataclass
from hashlib import sha256
from string import ascii_letters, digits
from uuid import UUID, uuid4

@dataclass
class LocationActivity:
    location: str
    clicks: int


@dataclass
class IShortURLInitPayload:
    new_url: str
    created_at: str


@dataclass
class URLActivity:
    total_clicks: int
    all_location_of_clicks: list[str]
    clicks_per_location: dict


#  ________________________ | Short URL | _______________________


class ShortURL:
    _ALPHA_NUMS = ascii_letters + digits

    original_url: str
    metrics: dict = {}
    created_at: str = ""
    short_url: str
    uuid: UUID
    slug: str

    def __init__(self, payload: IShortURLInitPayload = None):
        if payload is None:
            payload = {"new_url": "defaultthing.com", "created_at": "Some time UTC"}

        uuid = uuid4()
        temp = uuid

        # Sha256 hashed into hexadecimals and base62 encoded, then first 5 chars taken
        slug = self._int_to_base(
            int(hashlib.sha256(str(temp).encode()).hexdigest(), 16)
        )[:5]

        self.slug = slug
        self.uuid = uuid
        self.original_url = payload.new_url
        self.short_url = f"customdomain.com/{slug}"

    def _int_to_base(self, n, len: int = 0):
        chars = []
        while n > 0:
            n, rem = divmod(n, 62)
            chars.append(self._ALPHA_NUMS[rem])
        return "".join(reversed(chars)).zfill(len)


#  __________________________ | User | __________________________
class User:
    all_short_urls = {}
    all_original_urls = list[str]
    name: str
    email: str
    __password: str

    def __init__(self):
        pass

    def add_url(self, url: str) -> None:
        if url in self.all_original_urls:
        
        new_short_url = ShortURL({"new_url": url, "created_at": ""})
        
        self.shortened_urls[new_short_url.short_url] = new_short_url

    def delete_url(self, short_url: str) -> None:
        if self.all_short_urls[short_url]:
            del self.all_short_urls[short_url]
        else:
            raise KeyError(f"The key '{short_url}' doesn't exist on your account.")
    
    def edit_url(self, short_url_key, value: IShortURLInitPayload):
        url_to_edit = self.all_short_urls[short_url_key]
        if not url_to_edit:
            raise KeyError(f"The key '{short_url_key}' doesn't exist on your account.")
        


"""

the urls will be stored with the user as an object for quick access

key,value pair of it will be  {[uuid]: ShortURL}

"""
