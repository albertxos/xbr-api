network.xbr
===========

**XBR Services** are at the heart of XBR. They are software components run by a XBR Provider that expose data services via WAMP interfaces or APIs ("Application Programming Interfaces").
The "application" in this case is the XBR Consumer side software component that accesses the data service exposed via the WAMP interfaces of the service.

An XBR Service **must implement at least two interfaces**:

* the actual data service interface, eg registered at ``com.example.myapp.*``
* a standardized XBR service payment interface, registered at ``xbr.service.<service-id>.payment.*``

While the former can be chosen freely by the XBR Provider of the data service, the latter is defined by the XBR Network, and must always be implemented "as is".

.. toctree::
   :maxdepth: 2

   core/index.rst
   mobility/index.rst
   manufacturing/index.rst
   consumer/index.rst
   internet/index.rst
