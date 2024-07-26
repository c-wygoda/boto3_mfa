from pydantic_settings import BaseSettings
from pyotp import TOTP


class TotpSettings(BaseSettings):
    totp_secret: str
    totp_serial_number: str


def cli():
    settings = TotpSettings()
    totp = TOTP(settings.totp_secret)
    print(totp.now())
