from boto3_mfa import MfaSession
from boto3_mfa.otp import TotpSettings
from logging import getLogger, DEBUG, basicConfig

basicConfig()
# getLogger("botocore").setLevel(DEBUG)

settings = TotpSettings()
session = MfaSession()

s3 = session.client("s3")

response = s3.list_buckets()

print("Buckets")
for bucket in response["Buckets"]:
    print(f"  {bucket['Name']}")
