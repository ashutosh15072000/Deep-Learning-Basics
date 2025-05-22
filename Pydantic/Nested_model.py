from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    zip_code: str
class Patient(BaseModel):
    name: str
    gender:  str
    age: int
    address: Address

Address_dict={"city":"lucknow","state":"uttar pradesh","zip_code":"226010"}

address_1=Address(**Address_dict)

paitent_dict={'name':"ashu",'gender':"male","age":25,"address":address_1}

patient_1=Patient(**paitent_dict)

print(patient_1)