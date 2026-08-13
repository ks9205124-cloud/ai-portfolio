# Candidate: Shaurya

## Background
Second-year Computer Science student at Manipal University Jaipur (MUJ), 
focused on backend software engineering. Primary stack is Java and Spring 
Boot. Actively self-studying AI engineering (LLM APIs, prompt engineering, 
Pydantic structured outputs) as a secondary track. Goal is to secure a 
software engineering internship by the end of second year.

## Skills
- Languages: Java, Python, JavaScript
- Backend: Spring Boot, Spring Security, Spring Data JPA, REST APIs, 
  OAuth 2 (self-hosted authorization server + resource server), JWT
- Databases: MySQL, H2
- Frontend: React (Vite, Tailwind CSS), basic JS/DOM fundamentals
- Tools: Git (branching, conventional commits, credential management), 
  Docker, IntelliJ IDEA, VS Code, WebStorm
- AI/LLM: Groq API, prompt engineering, prompt chaining, ReAct looping, 
  structured output validation with Pydantic, LLM API streaming

## Projects

### Time Complexity Analyzer (Flagship Project)
A tool that analyzes source code and determines its Big O time complexity 
using a hand-written lexer and recursive-descent parser — not a simple 
heuristic. The parser builds a real Abstract Syntax Tree (AST) with typed 
nodes (ForNode, WhileNode, BlockNode), and a ComplexityAnalyzer walks that 
tree to compute complexity, including detecting logarithmic patterns in 
loop variables. Built with a Spring Boot backend, MySQL database, REST 
API, and a vanilla JavaScript frontend. Deployed live on Render with 
MySQL hosted on filess.io. This project involved a deliberate 
architectural upgrade from an earlier stack-based heuristic approach to 
a proper parser-based design, reflecting real compiler-adjacent design 
thinking rather than a shortcut solution.

### Expense Tracker
A full-stack expense tracking application built with a Spring Boot 
backend and a React frontend, used both to learn React properly and to 
practice building secure, production-style APIs. The standout feature is 
a self-hosted OAuth 2 implementation (built as both an authorization 
server and a resource server, following Spring Security in Action) 
rather than a simple hand-rolled JWT filter or an external provider like 
Auth0 — this was a deliberate choice to be able to explain the OAuth 2 
flow in depth during interviews. Implements the full OAuth2 Authorization 
Code + PKCE flow end-to-end, BCrypt password hashing, category-based 
expense tracking with deletion safeguards, and centralized exception 
handling (a global exception handler returning consistent error 
responses, paired with a React-side toast notification system). 
Deployed on Render with MySQL on filess.io, and also fully containerized 
locally with Docker Compose (Spring Boot + React + MySQL).

### Sudoku Solver
A vanilla Java/Swing desktop application that solves Sudoku puzzles of 
dynamic size (not fixed to the standard 9x9 grid), using a solve-first, 
then-hide-cells approach to generate puzzles. The dynamic n×n sizing was 
an original design decision beyond a typical Sudoku solver implementation.

## Currently Building
An AI-powered chatbot for this very portfolio site, built in Python using 
the Groq API, with structured, schema-validated responses (via Pydantic) 
so answers stay grounded in this resume content and scoped to 
recruiter-relevant questions.

## Contact
- Email: [placeholder — add later]
- LinkedIn: [placeholder — add later]
- GitHub: github.com/ks9205124-cloud