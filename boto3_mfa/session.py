from boto3 import Session
from pyotp import TOTP

from boto3_mfa.otp import TotpSettings


class MfaSession(Session):
    totp_settings: TotpSettings

    def __init__(self, /, totp_settings: TotpSettings | None = None, *args, **kwargs):
        self.totp_settings = (
            totp_settings if totp_settings is not None else TotpSettings()
        )
        super().__init__(*args, **kwargs)

    def client(
        self,
        service_name,
        region_name=None,
        api_version=None,
        use_ssl=True,
        verify=None,
        endpoint_url=None,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        aws_session_token=None,
        config=None,
    ):
        if aws_session_token is None:
            sts = super().client(
                "sts",
                region_name,
                api_version,
                use_ssl,
                verify,
                endpoint_url,
                aws_access_key_id,
                aws_secret_access_key,
                None,
                config,
            )

            totp = TOTP(self.totp_settings.totp_secret)
            response = sts.get_session_token(
                DurationSeconds=900,
                SerialNumber=self.totp_settings.totp_serial_number,
                TokenCode=totp.now(),
            )
            aws_session_token = response["Credentials"]["SessionToken"]

        return super().client(
            service_name,
            region_name,
            api_version,
            use_ssl,
            verify,
            endpoint_url,
            aws_access_key_id,
            aws_secret_access_key,
            aws_session_token,
            config,
        )
