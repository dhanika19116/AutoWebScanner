"""
Project: Automated Web Scanner
Author: Dhanika S

Description:
Scans a website for common HTTP security headers
and checks whether Cross-Origin Resource Sharing (CORS)
is configured permissively.

Use only on websites you own or have permission to test.
"""

import requests
from urllib.parse import urlparse


SECURITY_HEADERS = {
    "Content-Security-Policy":
        "Helps prevent certain content injection attacks.",

    "Strict-Transport-Security":
        "Encourages HTTPS connections.",

    "X-Content-Type-Options":
        "Helps prevent MIME-type sniffing.",

    "X-Frame-Options":
        "Helps protect against clickjacking.",

    "Referrer-Policy":
        "Controls referrer information.",

    "Permissions-Policy":
        "Controls access to browser features."
}


def validate_url(url):
    """Validate the URL before making a request."""
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("Enter a valid HTTP or HTTPS URL.")

    return url


def scan_website(url):
    """Check security headers and basic CORS configuration."""

    print("\n" + "=" * 55)
    print("       AUTOMATED WEB SECURITY SCANNER")
    print("=" * 55)
    print(f"Target: {url}\n")

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "Educational-Web-Scanner/1.0"
            }
        )

        print(f"HTTP Status Code: {response.status_code}")
        print(f"HTTPS Used: {response.url.startswith('https://')}")

        print("\n--- SECURITY HEADER ANALYSIS ---")

        headers = response.headers
        missing_headers = []

        for header, description in SECURITY_HEADERS.items():
            if header in headers:
                print(f"[PRESENT] {header}")
            else:
                print(f"[MISSING] {header} - {description}")
                missing_headers.append(header)

        print("\n--- CORS CONFIGURATION CHECK ---")

        allow_origin = headers.get(
            "Access-Control-Allow-Origin"
        )

        allow_credentials = headers.get(
            "Access-Control-Allow-Credentials", ""
        ).lower()

        if allow_origin == "*":
            print(
                "[WARNING] CORS allows requests from any origin."
            )

            if allow_credentials == "true":
                print(
                    "[REVIEW] Wildcard origin and credentials "
                    "setting should be investigated."
                )

        elif allow_origin:
            print(
                f"[INFO] Access-Control-Allow-Origin: "
                f"{allow_origin}"
            )
            print(
                "[INFO] Verify that allowed origins are trusted."
            )

        else:
            print(
                "[INFO] No Access-Control-Allow-Origin header found."
            )

        print("\n--- SCAN SUMMARY ---")

        print(
            f"Security headers present: "
            f"{len(SECURITY_HEADERS) - len(missing_headers)}"
        )

        print(
            f"Security headers missing: {len(missing_headers)}"
        )

        if missing_headers:
            print("\nRecommendation:")
            print(
                "Review missing headers and configure them "
                "where appropriate."
            )
        else:
            print(
                "\nAll checked security headers are present."
            )

        print(
            "\nNote: Missing headers do not automatically prove "
            "a vulnerability. Review the application's "
            "requirements."
        )

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")

    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    target_url = input(
        "Enter an authorized website URL: "
    ).strip()

    try:
        scan_website(validate_url(target_url))

    except ValueError as error:
        print(f"Invalid URL: {error}")