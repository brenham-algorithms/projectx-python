# projectx-python

Python client for the ProjectX/TopstepX API. Provides authentication, market data retrieval, and order management.

Used as a shared dependency by [level-farmer](https://github.com/brenham-algorithms/level-farmer) and [distributor](https://github.com/brenham-algorithms/distributor).

## Installation

```bash
# From source (development)
pip install -e .

# From git
pip install git+ssh://git@github.com/brenham-algorithms/projectx-python.git
```

Requires Python 3.12+.

## Usage

### Authentication

```python
from projectx_client import Auth

auth = Auth(
    base_url="https://api.topstepx.com",
    username="your_username",
    api_key="your_api_key",
)
jwt_token = auth.login()
```

### Market Data

```python
from projectx_client import MarketData

md = MarketData(base_url="https://api.topstepx.com", jwt_token=jwt_token)

bars = md.bars(
    contractId="CON.F.US.MNQ.U26",
    live=False,
    startTime="2026-06-01T00:00:00Z",
    endTime="2026-06-02T00:00:00Z",
    unit="Minute",
    unitNumber=1,
)
```

### Orders

```python
from projectx_client import Orders

orders = Orders(base_url="https://api.topstepx.com", jwt_token=jwt_token)

# Place an order
order_id = orders.place(
    accountId="your_account_id",
    contractId="CON.F.US.MNQ.U26",
    type="Market",
    side="Buy",
    size=1,
)

# Search open orders
open_orders = orders.search_open(accountId="your_account_id")

# Cancel an order
orders.cancel(orderId=order_id)
```
