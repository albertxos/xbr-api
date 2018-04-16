com.example.basic2
==================

A couple of very basic interface examples.

.. code-block:: protobuf

    syntax = "proto3";

    message SearchRequest {
        string query = 1;
        int32 page_number = 2;
        int32 result_per_page = 3;
    }


# namespace com.example.cm.machine

# procedure get_model

.. xbr:namespace:: com.example.cm.machine

    Machine API for Condition Monitoring.

.. xbr:procedure:: get_model

    Get machine model information.

    @params 