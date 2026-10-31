# Security and Privacy

## 1. Sensitive Data Redaction

QualityForge AI sanitizes failure logs before processing or storing them.

The current redaction logic covers:
- API keys
- Passwords
- Tokens and secrets
- Bearer authentication tokens
- Email addresses

## 2. Testing

Security tests verify:
- Email addresses are redacted.
- Multiple sensitive values are redacted together.
- Existing secret-redaction behavior is preserved.

## 3. Limitations

Regex-based redaction only detects known patterns.
It cannot guarantee detection of every possible secret format.

Production systems should combine redaction with:
- Secret-scanning controls
- Strict access policies
- Secure log storage
- Regular security reviews

## 4. Security Principle

Sensitive information should not be exposed in test reports,
application logs, or AI evaluation inputs.