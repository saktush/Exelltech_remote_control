# exelltech-remote-control

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)

[English version](README.md)

Типизированная Python-библиотека для управления аудио DSP/матричными процессорами **Exelltech ELT404(D) / ELT808(D) / ELT1616(D)** по их протоколу управления UDP + ASCII.

## Зачем это нужно

DSP/матричные устройства Exelltech используют собственный протокол управления на базе UDP с ASCII-командами — публичного SDK или клиентской библиотеки производитель не предоставляет. Проект появился в ходе реальной эксплуатации парка таких устройств: библиотека оборачивает протокол в типизированный, тестируемый Python API, чтобы интеграция с этим оборудованием не сводилась к ручному формированию ASCII-команд, управлению UDP-сокетами и таймаутами, а также ручному отслеживанию состояния каналов и матрицы.

Библиотека может быть полезна другим инженерам, которым нужно автоматизировать работу с оборудованием Exelltech или интегрировать его в свои системы, а также как референс подхода к обёртыванию похожего вендорского протокола.

## Что предоставляет библиотека

- **`ASCII`** — типизированный конструктор командных строк, покрывающий весь набор `get`/`set` команд протокола (входы, выходы, матрица микшера, сцены, система).
- **`UDP`** — транспортный примитив: отправка/приём ASCII-команд через UDP-сокет.
- **`Driver`** — операции более высокого уровня (чтение/запись гейна, mute, уровня каналов, матрицы коммутации) поверх `ASCII` + `UDP`.
- **`Channel` / `InputChannel` / `OutputChannel` / `Matrix`** — типизированная объектная модель каналов и матрицы коммутации устройства с валидацией, соответствующей реальным ограничениям оборудования (диапазоны гейна, длина имени и т.д.).
- **`ELTProcessor`** — единый фасад, объединяющий всё перечисленное для конкретного устройства.

## Установка

```bash
pip install git+https://github.com/saktush/Exelltech_remote_control.git
```

Для локальной разработки:

```bash
pip install -e ".[dev]"
```

## Быстрый старт

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

## Запуск примеров

Скрипты в `examples/` работают с реальным оборудованием по UDP. Установите extra `examples` (для поддержки `.env`), затем скопируйте `.env.example` в `.env` и укажите адрес своего устройства:

```bash
pip install -e ".[examples]"
cp .env.example .env
python examples/processor_live_pulling.py
```

## Архитектура

| Модуль | Ответственность |
|---|---|
| `api.py` | Чистые конструкторы ASCII-команд (`ASCII.get.*` / `ASCII.set.*`), без I/O |
| `system.py` | `UDP.send` — единственный транспортный примитив, кодирование/декодирование ASCII через UDP |
| `driver.py` | `Driver` — объединяет `api` + `system` в операции более высокого уровня |
| `abstract.py` | Абстрактные классы `Channel` / `Processor`, задающие контракт объектной модели |
| `channel.py`, `matrix.py`, `processor.py` | Конкретная объектная модель: `InputChannel`, `OutputChannel`, `Matrix`, `ELTProcessor` |
| `exceptions.py` | `ExelltechError`, `CommunicationError` |
| `enums.py` | `ChannelSource`, `SwitchState` |

## Известные ограничения

- `Driver` пока умеет читать гейн/mute/уровень каналов и состояние коммутации матрицы, но не читает имя/фазу/линковку/чувствительность/тип канала (соответствующие конструкторы команд в `ASCII` уже есть, но пока не подключены к `Driver`).
- В CI нет интеграционных тестов против реального оборудования — `tests/` тестируется юнит-тестами с замоканным транспортом. `examples/udp_api_ASCII_check.py` — это ручной набор для проверки протокола на живом устройстве.

## Лицензия

MIT — см. [LICENSE](LICENSE).
