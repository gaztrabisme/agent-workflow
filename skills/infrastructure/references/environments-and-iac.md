# Environments and infrastructure code

How to decide which environments a project runs, how they are defined, and which plan rows provision them. The cost of each environment is in [cost-estimate.md](cost-estimate.md); the pipeline that deploys into them is in [ci-cd-and-release.md](ci-cd-and-release.md).

## Environment plan

Write the environment plan before any cost or provisioning row. One row per environment:

| Column | Content |
|---|---|
| Name and purpose | Development, test, staging/acceptance, production, demo; what each is for |
| Start and end | Plan weeks, or "after go-live, N months" for run environments |
| Sizing | The service tiers and capacities it runs, and why they differ from production |
| Running hours | Always on, or paused outside working hours (affects pay-as-you-go cost) |
| Where it lives | Subscription or account, tenant, region; who owns it |
| Plan rows | The WBS rows that provision, configure and remove it |
| Counted in | Which cost total includes it, or the reason it is excluded |

- **The environment count comes from what the work needs and from the plan, not from a template.** An environment with no provisioning row in the plan is either unfunded or not intended; settle which before it is costed. Do not choose the count because of the cost total it produces. (derived: EVOLUTION case 3)
- Environments that support one release process should be nearly identical; differences between them are where software that worked in testing fails in production. [book:infrastructure-as-code], Environments, Consistency, and Configuration
- Smaller sizing in non-production is a parameter value, not a different definition: for example fewer servers in development than in production. [book:infrastructure-as-code], Chapter 7. Configuring Stack Instances
- A separate demonstration or proof-of-concept environment on public data, hosted where the team controls it, can run before the client's environment exists. State what it does not prove (integration with the client's systems). (derived: EVOLUTION case 5)
- Provisioning inside a client's tenant waits on the client's approvals and security reviews. Plan those as dependencies with their owner, not as team effort; `../../project/references/estimating.md` treats an outside input as a dependency. (derived: EVOLUTION case 5)

## Infrastructure as code

- **Define configuration, versions and dependencies as code**, so rebuilding an environment is a yes/no decision rather than a set of choices. This is what makes test environments consistent with production and lets an environment be recreated after failure. [book:infrastructure-as-code], Principle: Make Everything Reproducible
- **Use one reusable definition per stack and apply it once per environment.** Copy-paste environments drift: each change has to be copied to every copy, each copy needs separate testing, and variations creep in. [book:infrastructure-as-code], Antipattern: Copy-Paste Environments
- Declarative code suits environments meant to be nearly identical. [book:infrastructure-as-code], Declarative Versus Imperative Languages for Infrastructure
- **Pass per-environment values as parameters** (command line, file or key-value store), and make sure the values are defined and applied consistently to each environment. Keep the parameter list in one place per environment. [book:infrastructure-as-code], Chapter 7. Configuring Stack Instances; the same approach in a general-purpose language: per-stack configuration values (region, domain name) read by the code. [book:python-for-devops], Provisioning a Route 53 Zone and DNS Records
- Treat the environment like code: change it incrementally, keep the changes in version control, and test that each change does not break what runs on it. [book:continuous-delivery], Managing Your Environments (part 1)

## Secrets and configuration

- Keep configuration separate from code, and keep secrets in a store built for secrets with access narrower than the access to configuration. [book:practical-cloud-security], Types of Cloud Assets (part 4) (part 1)
- Credentials are never in the infrastructure code, the pipeline definition or an image. For container images, follow `../../dev/modes/build.md`.

## Cost-relevant decisions

These choices change the cost estimate; record each in the environment plan and carry it to [cost-estimate.md](cost-estimate.md).

- Running hours: a capacity billed pay-as-you-go can be paused outside working hours; a reserved one bills whether used or not. [book:llms-in-production], 6.2.1 Provisioning clusters; [book:designing-distributed-systems], Patterns for FaaS
- Storage keeps billing while compute is paused. (derived: EVOLUTION case 4)
- Shared resources (one container registry, one network hub, one capacity pool) serve several environments; state how their cost is split, and recheck the split when an environment is added or removed. (derived: EVOLUTION case 4)
- Region: price and deploy in the same region; data residency may fix the region. (derived: EVOLUTION case 2)

## Provisioning rows for the plan

Send `project` one row per provisioning deliverable, effort blank for its lead to fill: subscription or account setup, network and access restrictions, identity and secrets store, each environment's stacks, pipeline setup, monitoring and alerts, and environment removal at the end. A row that provisions "the environments" in one line hides how many there are. (derived: EVOLUTION case 3)
