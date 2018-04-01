import os
import json

from pprint import pprint

import jinja2
import stringcase

#
# map VSS types to simplified, WAMP standard types (JSON + binaries)
#
TYPES_MAP = {
    'UInt8': 'int',
    'Int8': 'int',
    'UInt16': 'int',
    'Int16': 'int',
    'UInt32': 'int',
    'Int32': 'int',
    'UInt64': 'int',
    'Int64': 'int',
    'Boolean': 'bool',
    'Float': 'float',
    'Double': 'float',
    'String': 'str',
    'ByteBuffer': 'bytes',
    'Undefined': 'undefined',
}


#
# Jinja2 template to render the header of a generated RST file for a VSS namespace
#
NS_TMPL = """{{ title }}
{{ title_underline }}

{{ description }}

.. note::

    The XBR interface description here was auto-generated
    `using a script <https://github.com/xbr/xbr-api/tree/master/extern/vss>`_
    from the
    `Vehicle Signaling Specification (VSS) <https://github.com/GENIVI/vehicle_signal_specification>`_.
    The VSS is
    `licensed <https://raw.githubusercontent.com/GENIVI/vehicle_signal_specification/master/LICENSE>`_
    under the Mozilla Public License 2.0, and the auto-generated files in this
    repository should be considered derived works.
    If you have improvements for or have found a bug in the APIs of namespace
    ``org.genivi.vss``, please head over to
    `GENIVIs issue tracker <https://github.com/GENIVI/vehicle_signal_specification/issues>`_.

.. xbr:namespace:: {{ namespace }}

"""

NS_TMPL_jenv = jinja2.Environment().from_string(NS_TMPL)


#
# Jinja2 template to render an XBR interface Sphinx xbr directive
#
IFC_TMPL = """
{{ title }}
{{ title_underline }}

{{ description }}.

.. xbr:interface:: {{ title }}

    {{ description }}

"""

IFC_TMPL_jenv = jinja2.Environment().from_string(IFC_TMPL)


#
# Jinja2 template to render a XBR event Sphinx directive
#
EVT_TMPL = """

    .. xbr:event:: {{ evt_name }}(new_value)

        :param new_value: {{ value_desc }}
        :type new_value: {{ value_type }}
        {% if value_att_id %}:vss_id: {{ value_att_id }} {% endif %}
        {% if value_att_enum %}:vss_enum: {{ value_att_enum }} {% endif %}
        {% if value_att_type %}:vss_type: {{ value_att_type }} {% endif %}
        {% if value_att_unit %}:vss_unit: {{ value_att_unit }} {% endif %}
        {% if value_att_sensor %}:vss_sensor: {{ value_att_sensor }} {% endif %}
        {% if value_att_actuator %}:vss_actuator: {{ value_att_actuator }} {% endif %}

"""

EVT_TMPL_jenv = jinja2.Environment().from_string(EVT_TMPL)


URI_PREFIX = 'org.genivi.vss'
INPUT_SPEC = './extern/vss/vss_rel_1.0.json'
OUTPUT_DIR = './api/namespace/org/genivi/vss/'

CNT_NAMESPACES = 0
CNT_INTERFACES = 0
CNT_EVENTS = 0

data = None
with open(INPUT_SPEC) as fd:
    data = json.load(fd)

nss = data['Signal']['children']
for ns, ns_data in sorted(nss.items()):
    CNT_NAMESPACES += 1
    ns_name = ns.lower()
    ns_file = os.path.join(OUTPUT_DIR, '{}.rst'.format(ns_name))
    with open(ns_file, 'w') as ns_fd:
        ns_fqn = '{}.{}'.format(URI_PREFIX, ns_name)

        rst_output = NS_TMPL_jenv.render(title=ns_fqn,
                                         title_underline='='*len(ns_fqn),
                                         description=ns_data.get('description', 'FIXME'),
                                         namespace=ns_fqn)
        ns_fd.write(rst_output)

        #
        # FIXME: this is a total hack, as the two namespaces below
        # are NOT nested further - so we nest them articifically.
        #
        ifcs = ns_data['children']
        if ns in ['OBD', 'Vehicle']:
            ifcs = {ns: {'children': ifcs}}

        for ifc, ifc_data in sorted(ifcs.items()):
            CNT_INTERFACES += 1
            if True:
                #
                # prefix all interfaces with "I"
                #
                ifc_name = 'I{}'.format(ifc)
            else:
                ifc_name = ifc

            rst_output = IFC_TMPL_jenv.render(title=ifc_name,
                                              title_underline='-'*len(ifc_name),
                                              description=ifc_data.get('description', 'FIXME'))
            ns_fd.write(rst_output)

            def recurse(prefix, data, result):
                if type(data) == dict and 'children' in data:
                    for _key, _data in data['children'].items():
                        recurse(prefix + [_key], _data, result)
                else:
                    res = ('.'.join(prefix), data)
                    result.append(res)

            evts = []
            recurse([], ifc_data, evts)

            for evt, evt_data in sorted(evts):
                CNT_EVENTS += 1

                #
                # convert all event names to snake case, and prefix
                # all events with "on_"
                #
                ep = evt.split('.')

                # FIXME: hack, otherwise stringcase.snakecase will convert
                # ABC => a_b_c
                if ep[-1].isupper():
                    ep[-1] = ep[-1].lower()
                ep = [stringcase.snakecase(x) for x in ep]

                if False:
                    ep[-1] = 'on_{}'.format(ep[-1])
                    evt_name = '.'.join(ep)
                else:
                    evt_name = 'on_' + '_'.join(ep)

                print(evt_name)

                value_att_id = evt_data.get('id', None)
                value_att_sensor = evt_data.get('sensor', None)
                value_att_actuator = evt_data.get('actuator', None)
                value_att_type = evt_data.get('type', None)
                value_att_unit = evt_data.get('unit', None)
                value_att_enum = evt_data.get('enum', None)

                value_desc = evt_data.get('description', 'FIXME')
                value_type = TYPES_MAP.get(evt_data.get('type', 'Undefined'), 'undefined')

                rst_output = EVT_TMPL_jenv.render(evt_name=evt_name,
                                                  value_desc=value_desc,
                                                  value_type=value_type,
                                                  value_att_id=value_att_id,
                                                  value_att_enum=value_att_enum,
                                                  value_att_type=value_att_type,
                                                  value_att_unit=value_att_unit,
                                                  value_att_sensor=value_att_sensor,
                                                  value_att_actuator=value_att_actuator)
                ns_fd.write(rst_output)

DONE = """

Namespaces:   {namespaces}
Interfaces:   {interfaces}
Events:       {events}

""".format(namespaces=CNT_NAMESPACES, interfaces=CNT_INTERFACES, events=CNT_EVENTS)

print(DONE)
