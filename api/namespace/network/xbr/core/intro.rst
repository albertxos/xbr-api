
API UUID
Data Provider UUID
Data Provider Public Key (Ethereum address)
Data Service UUID
Data Service Public Key (Ed25519)
Data Service Instance Public Key (Ed25519)



For Carrier-Markets: Crossbar.io Fabric
For Consumers-Providers: Autobahn


Usage for Consumers
-------------------

The global XBR network is structured into public (open access) and private (permissioned access) XBR based data markets.

Both types of XBR data markets are cleared over a global blockchain (Ethereum).

Public open markets will need global discovery of markets itself, as well as APIs and service providers.

We will first discuss APIs required for private markets (which cannot use global discovery services).

Data consumers in private data markets need ways to:

* search for APIs in the global XBR network API catalog
* search for (possibly private) APIs available in the market
* list data providers implementing a given API in the market
* query for data provider metadata
* query for a data providers' pricing of a specific API

and for user and community ratings:

* query for data provider ratings and comments
* query for data provider API ratings and comments
* submit data provider ratings and comments
* submit data provider API ratings and comments

These acitivities are conducted by developer of the data consumer or the WAMP client that subscribes to events, and calls procedures described in the XBR API used.

When that data consumer WAMP client runs, it will (programatically) want to:

* list service instances (ID, public key) for a (API, data provider) in the market

* (market_uuid, api_uuid, provider_uuid) -> [(service_uuid, service_key)]
