# Operations case studies

**Mally Kisubi** · Operations and delivery lead · London

[mally-cv.vercel.app](https://mally-cv.vercel.app) · [LinkedIn](https://www.linkedin.com/in/malcolm-k)

This repo holds operating decisions, written up one page each so they can be read and checked rather than taken on trust. It is not a portfolio of code. Each case sets out the situation, the problem, what I decided and did, what happened, and what I can and cannot show for it. Every figure comes from my own career record. Where something was not measured, the case says so, and nothing that belongs to a former employer is reproduced.

## Cases

| # | Case | Where | Result |
|---|---|---|---|
| 01 | [Grants operations for 500+ organisations](01-grants-operations-500-organisations.md) | Starknet Foundation, 2024 to 2025 | Onboarding and reporting cycle times cut by 33%; the Foundation's first AML/KYB framework |
| 02 | [150+ subscriptions into one register](02-150-subscriptions-one-register.md) | Parity Technologies, 2022 to 2024 | 150+ subscriptions, around £3M, in one register in Asana |

More cases will be added.

## How each case is laid out

Every case has the same shape, so they can be compared side by side.

- **Where.** Role, employer and dates.
- **Context.** The situation and my remit.
- **The problem.** What had to change.
- **What I did.** The decision, then the actions.
- **Result.** Numbers where they exist.
- **Also in this role.** Three lines on the rest of the job, so the page reads whole.
- **Evidence and limits.** What is public, what belongs to the former employer, and what was not measured.

## How I work with AI agents and code review

At my current employer I build most of the tooling my part of the business runs on, and I build it with AI coding agents. The code ships through a reviewed pull-request workflow in a team repo. I run Claude Code as an orchestrator with specialist subagents, about 20 in the employer's repo. Agents that are safe to run in the background are kept apart from the ones that must run in the main session, and a fact-checker agent is the final gate. These are Claude Code agent definitions, not a custom agent runtime.

## Licence

The text in this repo is licensed under [CC BY 4.0](LICENSE). You may share and adapt it with credit.

## Contact

- Site: [mally-cv.vercel.app](https://mally-cv.vercel.app)
- LinkedIn: [linkedin.com/in/malcolm-k](https://www.linkedin.com/in/malcolm-k)
