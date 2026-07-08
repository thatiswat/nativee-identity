# ADR-001

## Title

Nativee Identity Architecture

## Status

Accepted

## Context

Nativee Identity is the centralized identity provider for the Nativee Platform.

Every Nativee product authenticates through this service.

Identity is the single source of truth for authentication and user identity.

Business resources belong to their owning services.

## Decision

Nativee Identity owns:

- Authentication
- Sessions
- JWT Issuance
- JWT Verification
- OAuth
- MFA
- Passkeys
- Device Management
- Email Verification
- Password Reset
- Audit Logs

Nativee Identity never owns:

- Projects
- API Keys
- Billing
- Analytics
- AI Models
- Conversations
- Usage

Those belong to Nativee API or future services.

## Consequences

Identity remains independent.

Applications remain independent.

Authentication scales independently.

Authorization belongs to application services.

Identity issues tokens.

Applications verify tokens.