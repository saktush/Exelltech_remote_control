# exelltech-remote-control

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)

[Русская версия](README.ru.md)

A typed Python driver library for controlling **Exelltech ELT404(D) / ELT808(D) / ELT1616(D)** audio DSP/matrix processors over their UDP + ASCII control protocol.

## Why this exists

Exelltech's DSP/matrix units expose a UDP-based, ASCII text control protocol with no public SDK or documented client library. This project was built to control a fleet of these units in real installations, and wraps the raw protocol in a typed, testable Python API — so integrating with this hardware doesn't mean hand-crafting ASCII command strings, managing UDP sockets and timeouts, or tracking channel/matrix state by hand.

It may be useful to other engineers who need to automate or integrate with Exelltech hardware, or as a reference for reverse-engineering and wrapping a similar vendor protocol.

## What it provides

- **`ASCII`** — a typed command-string builder covering the protocol's full `get`/`set` surface (inputs, outputs, mixer matrix, scenes, system).
- **`UDP`** — the transport primitive: sends/receives ASCII commands over a UDP socket.
- **`Driver`** — higher-level pull/push operations (channel gain/mute/level, routing matrix) built on `ASCII` + `UDP`.
- **`Channel` / `InputChannel` / `OutputChannel` / `Matrix`** — a typed object model for the device's channels and routing matrix, validated against the hardware's real constraints (gain ranges, name length, etc.).
- **`ELTProcessor`** — a single facade tying the above together for one device.

## Install

```bash
pip install git+https://github.com/saktush/Exelltech_remote_control.git
```

For local development:

```bash
pip install -e ".[dev]"
```

## Quickstart

```python
from exelltech_remote_control import ELTProcessor

proc = ELTProcessor(
    ip_addr="192.168.1.200",
    port=50000,
    inputs=8,
    outputs=8,
    digital_from=None,
    local_ip="192.168.1.100",
    local_port=50000,
)

proc.pull_channels()
for channel in proc.input_channels:
    print(channel)

proc.matrix.set_route(row=0, col=0, value=True)
proc.push_matrix()
```

## Running the examples

The scripts under `examples/` talk to real hardware over UDP. Install the `examples` extra (for `.env` support), then copy `.env.example` to `.env` and fill in your device's address:

```bash
pip install -e ".[examples]"
cp .env.example .env
python examples/processor_live_pulling.py
```

## Architecture

| Module | Responsibility |
|---|---|
| `api.py` | Pure ASCII command-string builders (`ASCII.get.*` / `ASCII.set.*`), no I/O |
| `system.py` | `UDP.send` — the one transport primitive, encodes/decodes ASCII over UDP |
| `driver.py` | `Driver` — composes `api` + `system` into higher-level pull/push operations |
| `abstract.py` | `Channel` / `Processor` ABCs defining the object model's contract |
| `channel.py`, `matrix.py`, `processor.py` | The concrete object model: `InputChannel`, `OutputChannel`, `Matrix`, `ELTProcessor` |
| `exceptions.py` | `ExelltechError`, `CommunicationError` |
| `enums.py` | `ChannelSource`, `SwitchState` |

## Known limitations

- `Driver` currently pulls gain/mute/level for channels and switch state for the matrix; it does not yet pull channel name/phase/link/sensitivity/type (the `ASCII` command builders for these already exist, just not wired into `Driver` yet).
- No integration suite runs against real hardware in CI — `tests/` is unit-tested against a mocked transport. `examples/udp_api_ASCII_check.py` is a manual harness for exercising the protocol against a live device.

## License

MIT — see [LICENSE](LICENSE).
