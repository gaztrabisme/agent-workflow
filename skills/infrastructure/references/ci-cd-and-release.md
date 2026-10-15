# Deployment pipeline and release

How code and infrastructure changes reach each environment, how a release is prepared, and how it is undone. Application tests and container image checks belong to `../../dev/modes/build.md`; this module covers the path between environments.

## Pipeline design

- **Build once; deploy the same artifact everywhere.** Separate configuration from binaries so the same binaries run in every environment; the only technical difference between a test deployment and a release is environment configuration. [book:continuous-delivery], Implementing a Deployment Pipeline (part 1)
- **Deploy the same way to every environment.** Production is deployed least often and matters most, so the deployment process must already have been exercised many times on the other environments. [book:continuous-delivery], Deployment Pipeline Practices (part 1)
- Starting from a manual process: first make it the same for every environment, then automate it step by step until a deployment needs only the target environment and the version. [book:continuous-delivery], Deployment Pipeline Practices (part 2)
- Set up the pipeline and a production-like environment before feature work starts, in the first iteration. [book:continuous-delivery], Implementing a Deployment Pipeline (part 1)
- **Infrastructure changes go through a pipeline too.** Rolling a change across the path to production catches problems in the change and in the process of applying it, and keeps every environment on that path configured the same. [book:infrastructure-as-code], Delivering Infrastructure Code
- Where the pipeline runs checks that a reviewer would otherwise run by hand, let it run them; check by hand only what the pipeline does not cover (`../../dev/modes/build.md`).

## Production change control

- **The pipeline is the only way to change a shared environment**, including operating system and third-party configuration. The pipeline then records which version is where, who authorised it, and what changed since the last deployment. [book:continuous-delivery], Introduction
- Production is locked down: configuration, software stack, network topology and state change only through automated processes, so they can be audited, diagnosed and repaired. [book:continuous-delivery], Preparing to Release (part 1)

## Release plan

For each release, write down before it starts:

| Item | Content |
|---|---|
| Version and environment | Which build goes where; the pipeline run that produced it |
| Pre-release checks | Tests passed, smoke test on the target, capacity check if load changes |
| Backup | State of databases and stored files taken before the release |
| Rollout method | All at once, blue-green, or canary to a small set of users first |
| Rollback trigger | The measured condition that starts a rollback, and who decides |
| Rollback steps | How the previous version and its data are restored |
| Data changes | Schema or data migrations, and whether they can be reversed |

- Use a launch checklist: questions with an action and a pointer for each (do you store persistent data — then implement backups). Keep it short enough to be used. [book:site-reliability-engineering], The Launch Checklist
- **Plan the rollback before the release.** Back up production state first. Data changes and releases that span several systems are what make rollback hard. [book:continuous-delivery], Rolling Back Deployments and Zero-Downtime Releases (part 1)
- Canary release: deploy the new version where no users are routed, run smoke tests and, if needed, capacity tests, then route a selected set of users to it. [book:continuous-delivery], Rolling Back Deployments and Zero-Downtime Releases (part 2)
- "Planned downtime" still costs the business for every hour it lasts. During a rolling deployment, version N and N+1 run side by side; anything they share (data, interfaces) must work with both. [book:release-it], Part IV—Operations (part 23)

## Plan rows

Send `project` rows for: pipeline setup, environment configuration per environment, the deployment of each release to each environment, release rehearsal on a production-like environment, and rollback rehearsal where data changes. Release work with no row has no effort or week behind it, the same gap as an environment with no provisioning row. (derived: EVOLUTION case 3)
