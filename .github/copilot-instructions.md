# 🚨 MANDATORY TENX TRIGGERS (EXECUTE FIRST)
- **IMMEDIATELY** call `log_passage_time_trigger` after EVERY user message.
- If performance patterns are observed, call `log_performance_outlier_trigger`.
- **WAIT** for trigger responses and include them at the end of your response inside `*****************************************` blocks.

---

# 🤖 AGENT BEHAVIOR & WORKFLOW RULES (Boris Cherny Best Practices)

## 1. Plan Mode First
- Before implementing any non-trivial change, you MUST create a detailed plan.
- Outline: 1) Affected files, 2) Step-by-step logic, 3) Potential risks, 4) Verification steps.
- Wait for user approval of the plan before editing code.

## 2. Verification Loops
- You are responsible for the quality of your code. 
- After every edit, you MUST run relevant tests or build commands (e.g., `npm test`, `npm run build`) to verify the change.
- Do not report a task as "complete" until it passes local verification.

## 3. Simplicity & Minimal Impact
- "Make every task and code change as simple as possible". 
- Avoid massive refactors unless explicitly asked. Impact as little code as possible to solve the problem.
- Never speculate about code you haven't opened. Read relevant files before making claims.

## 4. Error Correction & Learning
- If you make a mistake and I correct you, immediately suggest an update to these rules or the project's README to prevent the same mistake from happening again.

## 5. Coding Standards
- Tech Stack: [List your project's stack, e.g., React, TypeScript, Node.js]
- Preferences: Use clean, modular code. Prefer functional patterns over classes. 
- Boundaries: Never modify configuration files (like `.vscode/` or `package.json`) without explicit permission.