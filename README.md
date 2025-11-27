# Railway Management System
🚂 Comprehensive Project Overview: Railway Reservation System
1. Executive Summary
  This project develops a Command-Line Interface (CLI) application to simulate a simplified Railway Reservation System (RRS),       leveraging Python for application logic and MySQL for persistent data management. The system's primary function is to           manage user accounts and facilitate core transactional services like ticket booking and cancellation. It serves as a           foundational exercise in database-backed application development, highlighting basic security practices and data integrity       challenges.

2. Architecture and Technology Stack
   
    2.1. System Architecture
    The system follows a rudimentary Two-Tier Monolithic Architecture.
       Tier 1 (Client/Logic): The Python application handles all user interaction via the CLI (Presentation) and contains all           business rules (Logic) in procedural functions.
        Tier 2 (Data): The MySQL database is hosted locally and is directly queried by the Python application.
   

3. Security and Development Strategy (Phase II Plan)
The project's current state has critical security vulnerabilities. The solution approach includes a planned Phase II to address these issues, making the system robust:

      3.1. Security Implementation
        SQL Injection Mitigation: Refactor all SQL execution to utilize Parameterized Queries (cursor.execute(sql,(values,)))       instead of string concatenation.

      Password Hashing: Integrate a strong hashing library (e.g., bcrypt or hashlib with salting) to store password digests         instead of plain text.

    3.2. Integrity and Robustness
      Seat Management: Introduce new tables (Trains, Schedules, Availability) and update the buy_ticket() and cancel_ticket()       functions to perform transactional updates (using explicit COMMIT/ROLLBACK) to reliably manage seating counts.

      Input Validation: Implement comprehensive try...except blocks and validation checks for user input (e.g., checking if         IDs are numeric, dates are in the correct format) to prevent application crashes.

      Flow Refactoring: Replace the current recursive function calls for menus with robust while loops to prevent stack             overflow issues in deep navigation.
