from basic2_pb2 import Person, AddressBook


# person = Person()

address_book = AddressBook()

person = address_book.people.add()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = Person.HOME

person = address_book.people.add()
person.id = 555
person.name = "Homer Simpson"
person.email = "js@simpsons.org"
phone = person.phones.add()
phone.number = "111-222-99997733"
phone.type = Person.HOME


# address_book.ParseFromString(f.read())

with open('basic2.dat.pb', 'wb') as f:
    pb_data = address_book.SerializeToString()
    f.write(pb_data)

from google.protobuf import json_format

#  message = json_format.Parse(json_string, my_proto_pb2.MyMessage())

import json

with open('basic2.dat.json', 'wb') as f:
    json_data = json_format.MessageToJson(address_book).encode('utf8')
    f.write(json_data)

json_obj = None
with open('basic2.dat.json', 'rb') as f:
    json_obj = json.load(f)
    print(json_obj)

import cbor

with open('basic2.dat.cbor', 'wb') as f:
    cbor_data = cbor.dumps(json_obj)
    f.write(cbor_data)


