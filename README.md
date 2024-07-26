# AWS+MFA boto3 Example

## Setup

- register a virtual MFA device for your account
- set the MFA secret as `TOTP_SECRET` env var
- set the MFA device ARN as `TOTP_SERIAL_NUMBER` env var
- run `poetry run totp` to generate MFA codes to register device

## Demo

- run `poetry run python3 demo.py`

The `boto3_mfa.session.MfaSession` class subclasses `boto3.Session` and makes sure calls
to `session.client(...)` contain a AWS session token, obtained from STS and the virtual
TOTP device.
