# 04. Three consoles that took a vertical off Google Sheets

**Where.** Chainlabs, Regional Operations Team Lead, London. 2026.

## Context

The vertical ran on a shared Google workbook and Apps Script: contractor sheets, four client sheets, two schemas and two date formats, with scripts stitching them together. Forty-three contributors, three delivery leads and finance all worked from the same tabs.

## The problem

- Apps Script quotas, timeouts and slow runs as volume grew.
- No per-client isolation: one workbook could not keep client data and freelancer access apart.
- Manual copying between sheets, broken formulas, two schemas and two date formats.
- No audit trail of who changed what, and freelancers lost in tabs. Nothing was built for the job.

## What I did

**The decision.** One data layer, and a console for each kind of user, designed around that person's job rather than around the data.

- Built three consoles on Supabase, Postgres and Node, shipped through the same reviewed pull-request workflow as the rest of the team.
- **Ad hoc console**, for the delivery leads: intake of single requests or CSV batches against a regional brief, then triage, assign, QC and deliver.
- **Cost console**, for me and finance: contractor spend against output per person and per client, so the margin is visible, plus the AI spend ledger.
- **Freelancer console**, for the network: each contributor's own queue, status and payout history, replacing the shared sheets.

The views below are rebuilt with generated sample data, so the layouts can be seen without any real entity, person or figure. They are not screenshots.

| Ad hoc console | Cost console | Freelancer console |
|---|---|---|
| ![Ad hoc console, rebuilt with sample data](https://mally-cv.vercel.app/assets/consoles/adhoc.webp) | ![Cost console, rebuilt with sample data](https://mally-cv.vercel.app/assets/consoles/cost.webp) | ![Freelancer console, rebuilt with sample data](https://mally-cv.vercel.app/assets/consoles/freelancer.webp) |

## Result

- Delivery leads triage and assign from one intake.
- Costs sit against output per person and per client, so the margin is visible.
- Each of the 43 contributors works from their own queue and sees their own payout history.
- Client data stays isolated per client.

## Also in this role

- Client delivery for the vertical, told with the numbers in [case 03](03-output-above-contract.md).
- The payout pipeline and the helper chat bot the network runs on, built with the engineering team.
- The Git, code review and CI/CD workflow the team develops on, which I set up.

## Evidence and limits

- **Internal systems**, described at role level. The code belongs to the employer and is not reproduced.
- **The pictures are rebuilds** with invented entities, people, counts and figures, rendered from a mock. Nothing in them is real data.
- **Not measured.** Time saved per request against the Sheets process; the migration off Apps Script is still going, in reviewed pull requests.
- **Still running.** The full decision record follows when it can be published.

[Back to all cases](README.md)
