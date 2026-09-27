# Operations case studies

**Mally Kisubi** · Operations and delivery lead · London

[mally-cv.vercel.app](https://mally-cv.vercel.app) · [LinkedIn](https://www.linkedin.com/in/malcolm-k)

This repo holds operating decisions, written up one page each so they can be read and checked rather than taken on trust. It is not a portfolio of code. Each case sets out the situation, the problem, what I decided and did, what happened, and what I can and cannot show for it. Every figure comes from my own career record. Where something was not measured, the case says so, and nothing that belongs to an employer or a client is reproduced.

## Cases

| # | Case | Where | Result |
|---|---|---|---|
| 01 | [Grants operations for 500+ organisations](01-grants-operations-500-organisations.md) | Starknet Foundation, 2024 to 2025 | Onboarding and reporting cycle times cut by 33%; the Foundation's first AML/KYB framework; the programmes still open |
| 02 | [150+ subscriptions into one register](02-150-subscriptions-one-register.md) | Parity Technologies, 2022 to 2024 | 150+ subscriptions, €3M in annual billings, in one register in Asana |
| 03 | [From volume complaints to delivery above contract](03-output-above-contract.md) | Chainlabs, 2026 | 275 entities in August 2026 against a floor of 200, 35 to 50% above contract, month after month |
| 04 | [Three consoles that took a vertical off Google Sheets](04-three-consoles-off-google-sheets.md) | Chainlabs, 2026 | 43 people off shared sheets into their own queues; four client sheets in one data layer |

More cases will follow. Newer ones are written at role level while the work is live; each says what it leaves out.

## How each case is laid out

Every case has the same shape, so they can be compared side by side.

- **Where.** Role, employer and dates.
- **Context.** The situation and my remit.
- **The problem.** What had to change.
- **What I did.** The decision, then the actions.
- **Result.** Numbers where they exist.
- **Also in this role.** Three lines on the rest of the job, so the page reads whole.
- **Evidence and limits.** What is public, what belongs to the employer or a client, and what was not measured.

## How I work with AI agents and code review

At my current employer I build most of the tooling my part of the business runs on, and I build it with AI coding agents. I build, deploy and maintain the vertical's production web applications myself, and I set up the workflow the team develops on: Git branching, code review through pull requests, and CI/CD. I run Claude Code as an orchestrator with specialist subagents, about 20 in the employer's repo. Agents that are safe to run in the background are kept apart from the ones that must run in the main session, and a fact-checker agent is the final gate. These are Claude Code agent definitions, not a custom agent runtime.

It is easy to prompt your way to something that works without understanding it. I do not want to be that person, so I work two ways, and the point of both is to understand what is happening under the hood. For production tooling, agents write and I review, and it ships through the pull-request workflow and CI/CD I set up. When the point is to own the code, I type and the AI explains, reviews and fixes; every session ends with a five-minute teach-back in my words that becomes the decision record; and once something works I break it on purpose and find the fault without help. I do not have a computer science degree or engineering certifications, and I would like both. Until I can, this is how I keep hold of what gets built and understand it, rather than letting the models run the whole thing.

## Checks

Every push runs [`scripts/check.py`](scripts/check.py) in GitHub Actions. It fails the build on an em or en dash, an invisible character, a phrase from the banned list (client names, internal codenames, figures that were later corrected), a link or heading fragment that does not resolve, or a case file missing one of the seven sections above. It reports; it never rewrites.

## Licence

The text in this repo is licensed under [CC BY 4.0](LICENSE). You may share and adapt it with credit.

## Contact

- Site: [mally-cv.vercel.app](https://mally-cv.vercel.app)
- LinkedIn: [linkedin.com/in/malcolm-k](https://www.linkedin.com/in/malcolm-k)
