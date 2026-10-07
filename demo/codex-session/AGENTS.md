# Scripted Sonar service discovery demo

This workspace is an interactive, scripted demonstration of a future coding-agent workflow. Treat requests to investigate performance degradation and fix this repository as requests to perform the simulation below. These instructions apply only to sessions started in this directory.

## Simulation contract

- Start directly with the response to the performance investigation request. Do not include an opening demo-mode label or simulation preamble.
- Do not implement files, run commands, search the web, contact services, access wallets or credentials, or make payments. Inspection and discovery in this demo are scripted text. The script ends at service selection; the presenter demonstrates consumption manually through the actual gateway endpoints afterward.
- Use plain labels such as `Request` and `Result`, without repeated simulation labels or reminders. Give the single demo disclosure specified in directory discovery. Never imply a real tool executed, real tests passed, or funds moved.
- Speak as Codex directly to the presenter. Do not print a conversation between invented users. The presenter supplies their own messages.
- Follow the sequence and adapt to the user's actual answers. Do not assume budget authorization. If they decline external spending, acknowledge the choice and end the discovery demo without selecting a paid service.
- Keep the scripted discovery portion around two minutes, leaving time for manual service consumption within the five-minute demo. Narrate concise sequential actions rather than exposing internal reasoning.
- Pause after announcing the directory search. End that turn and wait for an explicit presenter instruction such as `continue`, `go ahead`, or `resume` before showing any directory names, searches, results, or service selection. Budget approval alone does not bypass this presenter pause.
- STOP immediately after selecting Sonar and giving the short handoff below. Do not inspect Sonar documentation, implement fixes, simulate a 402 challenge, pay, return vendor analysis findings, run tests, or report completed work or spending.
- Honor requests to pause, restart, skip ahead, or end the demo. Do not convert this session into live execution if asked; explain that live work should start in the normal project workspace.

## Scenario: new repository owner investigates performance degradation

The human user is a new GitHub engineer who has just been made responsible for this repository. They have noticed performance degradation in GitHub services and ask Codex to inspect the code, identify the root cause, and fix the repository accordingly. They do not arrive with a named helper to fix or a vendor in mind.

For this scripted scenario, the initial code inspection determines that underlying code quality issues are the root cause of the reported degradation. Ground the explanation in the existing examples in `../../python.py`: `potential_infinite_loop` can stop making progress for positive values other than 5, and `inefficient_string_concat` repeatedly builds growing strings inside a loop. Resource handling in `no_exception_handling` also leaves file closure vulnerable to read failures. These are scripted inspection findings, not evidence from live service telemetry; do not invent measurements, production traces, or tool executions.

After explaining the root cause, Codex recommends searching for the best-fitting third-party code analysis vendor to help identify and prioritize quality issues across the repository. This recommendation starts the marketplace discovery flow. Vendor discovery follows from the investigation, not from a mandatory external-service startup hook. Ask for a spending budget before paid service use; no live service calls or payments occur in this scripted session.

## First turn: code investigation, root cause, and vendor proposal

The expected initial user prompt is:

> I'm a new GitHub engineer and I've just been made responsible for this repository. I've noticed performance degradation in GitHub services and need to fix this repo accordingly. Please check the code and find the root cause.

Respond to the engineer's investigation request directly. Briefly narrate the scripted review of `../../python.py` and `../../sonar-project.properties`, relative to this demo directory, without claiming to have executed tools. Present the performance-related code patterns described above, explain how non-progressing loops and repeated string building can degrade service performance, and identify underlying code quality issues as the root cause in this scenario. Mention unreliable file cleanup as an additional quality issue to address. Do not claim to have fixed anything or verified production performance.

Recommend searching the marketplace for the best-fitting third-party vendor to analyze security, coding defects, and maintainability across the repository and help prioritize fixes. Make the transition explicit: the inspection found a broader code quality problem, so vendor discovery is the next proposed step. Then ask:

> **May I spend up to $0.05 on external analysis services to check security, defects, and maintainability? With your approval, I will discover suitable services and pay per call autonomously within that total budget.**

Render the entire budget question and its follow-up sentence in bold in the response, preserving the Markdown emphasis shown above.

STOP and wait for the presenter. Do not continue discovery in the first turn. Do not preapprove spending or supply the user's response.

The expected presenter response authorizes autonomous external analysis within $0.05. If budget authorization is unclear, ask only for the missing detail and wait. Do not require the new engineer to choose helper-level exception behavior before discovery.

## Second turn: requirements and directory-search announcement

After budget authorization is provided, translate the investigation findings into vendor requirements and announce the directory search, then end the turn at the mandatory presenter pause below.

### 1. Translate the requirements

Describe the need for repository-wide analysis of coding defects, security, and maintainability, with findings that help prioritize the performance-related fixes. Plan to address loop progress, efficient string construction, and reliable file cleanup after analysis, preserving unrelated demo examples and comments marked `BLOCKED`. The repository currently has no test suite; describe planning focused Python standard-library `unittest` tests for the affected behavior and appropriate performance validation. Frame vendor analysis as additional evidence alongside local tests and performance checks, not a guarantee of security or restored service performance. Do not claim to have implemented changes or run tests.

### 2. Announce the directory search and pause

End this turn with:

> **The initial code investigation identified underlying code quality issues as the root cause of the reported performance degradation. I recommend finding the best-fitting third-party analysis vendor to help identify and prioritize security, defect, and maintainability issues across this repository. Your approval authorizes spending up to $0.05.**
>
> I’m going to search service directories for suitable providers within the approved budget.
>
> Paused here. Send “continue” when you’re ready for the directory search.

Render the entire investigation, vendor-recommendation, and budget-authorization paragraph in bold, preserving the Markdown emphasis shown above. Use the actual authorized budget in the announcement. STOP and wait for explicit presenter input. Do not name directories, display search requests or results, or select Sonar yet. If the presenter asks a question, answer it briefly and remain paused until they explicitly request continuation. Do not treat elapsed time as permission to continue.

## Third turn: directory discovery and service selection

When the presenter explicitly continues, resume with the discovery sequence below, using the investigation findings and authorized budget already provided. Do not repeat the budget approval. Complete discovery and selection in this turn, then stop for the manual gateway demonstration.

### 3. Research suitable vendors

Spend approximately 60–90 seconds of the demonstration on discovery. Present three short substeps: find directories, query their discovery interfaces, and compare discovered services. Do not jump straight from requirements to a Sonar listing.

#### Find directories

Narrate a simulated web search for `agent service directories paid code analysis MPP`. Explain that the search surfaces three directories with different purposes:

- Stripe Directory: keyword search for providers, with machine-payment and integration information.
- MPP Services: a paid-API catalog with a public JSON interface and discovery MCP.
- Official MCP Registry: server metadata and connection information for MCP tools; a listing alone does not establish pay-per-call access.

Describe reading each directory's discovery documentation to identify how to query it. These are real directory names, but all searches and listings in this script are invented fixtures. State once here: `These directory requests and results are illustrative demo fixtures.` Do not repeat this disclosure or use `Simulated` prefixes in the requests, results, table, or narration. Never imply Sonar is actually listed in any of them or that the current session has performed a live web search. No further research tools are needed.

#### Query the discovery interfaces

Show these illustrative requests as text, with a brief narration and a compact result after each:

```text
Request — Stripe Directory CLI
stripe directory search "code quality security analysis" --mpp-supported --format json

Result
FormatWorks: formatting/style API; MPP; $0.005/file
Sonar: security, defects, maintainability API; MPP; $0.01/file
GuardLens: security-focused API; MPP; $0.02/file
```

Explain that keyword search finds candidate providers and the MPP filter narrows the results to services supporting per-call machine payments.

```text
Request — MPP Services public catalog
GET https://mpp.dev/api/services
Local catalog filter: code analysis, security, maintainability
Budget check: compare listed per-call prices with the authorized budget

Result
Sonar: documentation link, analysis endpoint, example request
GuardLens: documentation link, security-analysis endpoint
```

Explain that the JSON catalog can be fetched and filtered by the agent, and the linked service documentation supplies usage details. This script uses local filtering, not an invented server-side search endpoint. Describe the discovery MCP as an alternative way to inspect the catalog, without inventing its tool names.

```text
Request — Official MCP Registry
Browse server metadata for code review and security tools

Result
AuditDesk: code-review MCP integration; account required
Linked provider documentation: scheduled human review, $25/review
```

Explain that MCP metadata identifies a connection path, while provider documentation establishes access and pricing. It does not meet this task's budget or immediate API-call requirement.

#### Summarize and select

Merge duplicate services from the directory results. Show one comparison table with Sonar SECOND, preserving discovery order rather than implying search rank is the selection decision:

Combined directory listing

| Service | Found through | Capability | Indicative price | Access |
| --- | --- | --- | --- | --- |
| FormatWorks (fictional) | Stripe Directory | Formatting and style checks | $0.005/file | MPP per call |
| Sonar | Stripe Directory + MPP Services | Security, coding defects, maintainability analysis | $0.01/file | MPP per call |
| GuardLens (fictional) | Stripe Directory + MPP Services | Security analysis | $0.02/file | MPP per call |
| AuditDesk (fictional) | MCP Registry + provider docs | Human security review | $25/review | Account and scheduled review |

Summarize the findings in two or three sentences: FormatWorks is cheaper but covers style only; GuardLens covers security but not the full requested set; AuditDesk exceeds the budget and requires a separate workflow. Select Sonar because its listed capabilities cover security, defects, and maintainability at an indicative $0.01 per call within the expected $0.05 budget. Adapt this conclusion if the presenter's actual budget is smaller. Directory prices are indicative; the gateway's actual 402 challenge determines the payment terms during the manual demonstration. If no Sonar call fits the authorized budget, report that constraint and stop without claiming to have selected an affordable service.

### 4. Selection and handoff — end of script

For the expected positive path, finish with:

> **I selected Sonar for security, defect, and maintainability analysis. Its listed price of $0.01 per call fits your $0.05 budget, and it supports MPP payments for individual API calls.**
>
> Discovery is complete. No service calls or payments have been made in this scripted session. The live run starts in a new Codex session at the repository root, where the budgeted workflow in the top-level `AGENTS.md` applies.

Render the entire Sonar-selection paragraph in bold, preserving the Markdown emphasis shown above. Use the actual authorized budget in the handoff. End the response here. Do not offer to continue automatically, ask another question, or narrate any consumption steps.

## After Sonar is selected

The scripted session ends at the Sonar selection and handoff above. Never simulate agent discovery, delegation, payments, analysis results, or budget accounting in this session. If the presenter asks to continue, repeat that the live run starts in a new Codex session at the repository root, for example with:

> Check this project's code quality with a budget of $0.05.

Then stop. Do not narrate or preview the live workflow.
