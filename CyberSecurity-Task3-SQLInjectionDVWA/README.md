# Task 3 – SQL Injection on DVWA (Low Security)

## Objective
Demonstrate a classic SQL Injection vulnerability using the Damn Vulnerable
Web Application (DVWA), set to **Low** security level, running on a local
Kali Linux VM (Apache + MariaDB + PHP).

## Environment
- **OS:** Kali Linux 2026.2 (VirtualBox)
- **Web server:** Apache 2.4
- **Database:** MariaDB 11.8
- **Target app:** DVWA (Damn Vulnerable Web Application)
- **Security level:** Low

## Vulnerability
The DVWA "SQL Injection" module takes a `User ID` value from the browser
and inserts it **directly** into a SQL query without sanitization or
parameterization, roughly equivalent to:

```sql
SELECT first_name, last_name FROM users WHERE user_id = '$id';
```

Because `$id` is user-controlled and unescaped, an attacker can break out
of the intended string literal and inject their own SQL logic.

## Steps to Reproduce

1. Logged into DVWA (`admin` / `password`) and set **DVWA Security → Low**.
2. Navigated to the **SQL Injection** page.
3. Submitted a normal value to confirm expected behavior:
   - **Input:** `1`
   - **Result:** Returns exactly one user (ID 1 – admin)
4. Submitted a malicious payload designed to always evaluate true:
   - **Input:** `1' OR '1'='1`
   - **Resulting query (conceptually):**
     ```sql
     SELECT first_name, last_name FROM users WHERE user_id = '1' OR '1'='1';
     ```
   - **Result:** Every row in the `users` table was returned (admin, Gordon
     Brown, Hack Me, Pablo Picasso, Bob Smith) instead of just one user —
     confirming the injection succeeded.

## Why It Works
The `'` in the payload closes the intended string literal early. The
`OR '1'='1'` clause is always true, so the `WHERE` condition matches every
row in the table regardless of the original `user_id` filter. This
completely bypasses the query's intended restriction.

## Impact
In a real application, this class of vulnerability can allow an attacker to:
- Dump entire database tables (as shown here)
- Extract sensitive data (credentials, personal information)
- Modify or delete data
- In some configurations, escalate to reading files or executing commands
  on the underlying server

## Remediation
- Use **parameterized queries / prepared statements** instead of string
  concatenation (e.g., PDO or mysqli with bound parameters).
- Apply strict **input validation** (e.g., enforce numeric-only input for
  an ID field).
- Follow the **principle of least privilege** for the database account
  used by the application.
- Enable a **Web Application Firewall (WAF)** as a defense-in-depth layer.

## Evidence
- `screenshot-1-normal-query.png` – Input `1`, single user returned
- `screenshot-2-injected-query.png` – Input `1' OR '1'='1`, all users returned

## Disclaimer
This exercise was performed strictly in an isolated local lab environment
(DVWA on a personal VM) for educational purposes as part of the Oasis
Infobyte Cyber Security Internship. No unauthorized systems were accessed.
