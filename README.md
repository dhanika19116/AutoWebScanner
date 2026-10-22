# AutoWebScannerAutomated Web Security Scanner

Author: Dhanika
Domain: Cybersecurity
Language: Python

1. Project Overview

The Automated Web Security Scanner is a Python-based tool that checks a website's HTTP security headers and identifies potentially permissive Cross-Origin Resource Sharing (CORS) configurations.

The tool generates a simple terminal report showing security headers that are present or missing and provides basic recommendations for further review.

2. Objectives

- Automate the checking of common HTTP security headers.
- Identify missing security-related response headers.
- Highlight potentially permissive CORS configurations.
- Generate a readable security assessment report.
- Demonstrate basic Python scripting and web security concepts.

3. Technologies Used

- Python 3
- Requests library
- HTTP/HTTPS
- HTTP security headers
- Cross-Origin Resource Sharing (CORS)
- Git and GitHub

4. Security Checks

The scanner checks the following headers:

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

It also reviews the "Access-Control-Allow-Origin" and "Access-Control-Allow-Credentials" response headers.

5. Installation

Install Python 3 on your computer.

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Open the project folder:

cd YOUR_REPOSITORY_NAME

Install the required dependency:

pip install -r requirements.txt

6. Execution

Run the scanner:

python Dhanika_AutomatedWebScanner.py

Enter the URL of a website you own or have permission to assess when prompted.

Example:

Enter an authorized website URL: https://example.com

7. Expected Output

The scanner displays:

- HTTP response status
- Whether HTTPS is used
- Security headers present
- Security headers missing
- Basic CORS configuration observations
- A scan summary

Results depend on the target website's actual HTTP response.

8. Limitations

- The scanner checks response headers rather than performing a complete penetration test.
- A missing header does not necessarily mean that a website is vulnerable.
- The tool does not test every possible CORS exploit or application security flaw.
- Findings require manual verification and security context.

9. Ethical Use

Use this tool only on websites you own or have explicit permission to assess. Do not use it to disrupt services or access unauthorized systems.

10. Future Enhancements

- Export reports to JSON or CSV.
- Add severity classifications.
- Support batch scanning of authorized targets.
- Integrate additional passive security checks.
- Add automated unit tests.

