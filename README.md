<div align="center">

# Awesome OpAMP

A curated list of awesome resources, implementations, libraries, and tools for the
**OpAMP (Open Agent Management Protocol)** — the OpenTelemetry protocol for remotely
managing fleets of agents and collectors.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Check links](https://github.com/agardnerIT/awesome-opamp/actions/workflows/links.yml/badge.svg)](https://github.com/agardnerIT/awesome-opamp/actions/workflows/links.yml)

</div>

OpAMP defines how a management server discovers, configures, upgrades, and reports
on a fleet of telemetry agents (OpenTelemetry Collectors, and other agents) over
HTTP or WebSocket, using protobuf messages. It complements OTLP, which carries the
telemetry itself — OpAMP manages the agents that produce it.

Only standard-OpAMP implementations are listed. Tools that speak a vendor's own
proprietary management API are out of scope — if a product has no standard-OpAMP
path, the answer is to open an issue on *their* repository.

See [Contributing](CONTRIBUTING.md).

--------------------

## Contents

- [Specifications & Documentation](#specifications--documentation)
- [Client Libraries](#client-libraries)
  - [Go](#go)
  - [Python](#python)
  - [Rust](#rust)
  - [JavaScript / TypeScript](#javascript--typescript)
  - [Other Languages](#other-languages)
- [Server Implementations](#server-implementations)
- [Supervisors](#supervisors)
- [Agents with OpAMP Support](#agents-with-opamp-support)
- [Tools & Utilities](#tools--utilities)
- [Tutorials, Talks & Articles](#tutorials-talks--articles)
- [Community](#community)
- [Related Projects](#related-projects)

--------------------

## Specifications & Documentation

*The canonical specification and supporting documentation.*

- [OpAMP Specification](https://opentelemetry.io/docs/specs/opamp/) - The official OpenTelemetry OpAMP specification.
- [opamp-spec](https://github.com/open-telemetry/opamp-spec) - Source repository for the OpAMP specification, including the protobuf definitions.

## Client Libraries

*Libraries for implementing OpAMP clients (the managed agent side).*

### Go

- [opamp extension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/opampextension) - OpAMP client extension for the OpenTelemetry Collector, allowing a Collector to be managed directly over OpAMP.
- [opamp-go](https://github.com/open-telemetry/opamp-go) - Official OpAMP protocol implementation in Go, with both client and server libraries.

### Python

<!-- Example entry:
- [Example Client](https://example.com) - One-line description of what it does and why it is great.
-->

_Nothing here yet — please [contribute](CONTRIBUTING.md)!_

### Rust

<!-- Example entry:
- [Example Client](https://example.com) - One-line description of what it does and why it is great.
-->

_Nothing here yet — please [contribute](CONTRIBUTING.md)!_

### JavaScript / TypeScript

- [@elastic/opamp-client-node](https://github.com/elastic/elastic-otel-node/tree/main/packages/opamp-client-node) - Lets Node.js apps get settings from an OpAMP server over HTTP and report whether the changes took effect.

### Other Languages

<!-- Example entry:
- [Example Client](https://example.com) - One-line description of what it does and why it is great.
-->

_Nothing here yet — please [contribute](CONTRIBUTING.md)!_

## Server Implementations

*OpAMP server / fleet-management implementations — the side that manages agents.*

- [Bindplane](https://bindplane.com) - OpAMP-based fleet management platform for telemetry agents; free tier available, commercial and not open source.
- [opamp-elixir](https://github.com/jaronoff97/opamp-elixir) - OpAMP protocol implementation in Elixir.
- [opamp-go](https://github.com/open-telemetry/opamp-go) - Official OpAMP protocol implementation in Go, with both client and server libraries.
- [opamp-server-py](https://github.com/agardnerIT/opamp-server-py) - OpAMP server in Python (FastAPI + Streamlit UI) with SQL-based agent selection, staged config rollouts, and OPA compliance.

## Supervisors

*Agents that run alongside and manage other agents over OpAMP — e.g. managing an OpenTelemetry Collector instance.*

- [opampsupervisor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/cmd/opampsupervisor) - Official OpAMP supervisor for the OpenTelemetry Collector; manages a Collector instance as its OpAMP agent.

## Agents with OpAMP Support

*Telemetry agents and collectors that can be remotely managed via standard OpAMP.*

- [Grafana Alloy](https://grafana.com/docs/grafana-cloud/send-data/fleet-management/get-started/opentelemetry-collector/) - Grafana Alloy can be managed via standard OpAMP; this page covers connecting it to Grafana Cloud Fleet Management.
- [opamp-falco](https://github.com/agardnerIT/opamp-falco) - OpAMP agent for Falco: the generic opamp-agent bridge plus a driver that applies pushed config and rules files and verifies them through Falco's reload-control API.
- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/management/) - The vendor-neutral collector, remotely manageable via OpAMP through the opampsupervisor or the opamp extension.
- [osquery-opamp](https://github.com/agardnerIT/osquery-opamp) - OpAMP extension for osquery, enabling remote fleet management of osquery deployments.

## Tools & Utilities

*Test harnesses, mock servers, dashboards, protocol debuggers, bridges and other OpAMP tooling.*

- [opamp-agent](https://github.com/agardnerIT/opamp-agent) - Generic OpAMP bridge that makes a third-party tool manageable over standard OpAMP through a small driver, without changing the tool.

## Tutorials, Talks & Articles

*Guides, conference talks, blog posts, and deep dives about OpAMP.*

- [OpenTelemetry At Scale 101: Intro to OpAMP](https://www.youtube.com/watch?v=zlGkhvhE-KQ) - NDC conference talk by Aakansha Priya and Adriana Villela introducing OpAMP.
- [OpenTelemetry at Scale: Controlling your Fleet with OpAMP](https://dev.to/agardnerit/opentelemetry-at-scale-controlling-your-fleet-49m2) - Article on using OpAMP to manage a fleet of agents at scale.
- [OpenTelemetry OpAMP: Everything you need to know (theory + hands-on)](https://www.youtube.com/watch?v=WRLODv2xBLM) - Video covering OpAMP theory followed by a hands-on demo.
- [Operating OpenTelemetry at Scale with OpAMP](https://www.youtube.com/watch?v=Z0HR7lClIBQ) - OpenObservability Talks episode on operating agent fleets with OpAMP.

More talks and videos: [YouTube search for "OpAMP"](https://www.youtube.com/results?search_query=opentelemetry+opamp).

## Community

*Where OpAMP development and discussion happens.*

<!-- Example entry:
- [#opamp on OpenTelemetry Slack](https://cloud-native.slack.com/archives/C02JCPPS51G) - The official OpAMP channel on the CNCF OpenTelemetry Slack.
-->

_Nothing here yet — please [contribute](CONTRIBUTING.md)!_

## Related Projects

*Adjacent OpenTelemetry projects and protocols that pair well with OpAMP.*

<!-- Example entry:
- [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) - The vendor-neutral collector that OpAMP commonly manages.
-->

_Nothing here yet — please [contribute](CONTRIBUTING.md)!_

--------------------

## Contributing

Contributions are welcome! Read the [contributing guide](CONTRIBUTING.md) to get started,
and open a PR to add your project or resource.

## License

[Apache License 2.0](LICENSE)
