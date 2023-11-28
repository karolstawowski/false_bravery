import os
import ssl


def verify_ssl_certificate():
    if not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(
        ssl, "_create_unverified_context", None
    ):
        ssl._create_default_https_context = ssl._create_unverified_context
