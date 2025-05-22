from pydantic import BaseModel,EmailStr,Anyurl,Field,field_validator
from typing import Optional,List,Dict,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,description="Give the name of the patient less length of 50",title="Name of the Patient",examples=['ashutosh',"lavanya","ayush","pooja"])]
    email: EmailStr
    linkedin_url: Anyurl
    age: int
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default=None,description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5) ]
    contact_details: Dict[str,str]

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com',"icici.com"]
        domain_name=value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a Valid domain")
        return value
    

    @field_validator("name")
    @classmethod
    def transform(cls,value):
        return value.upper()
    

    
def upadate_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("updated in the database")

patient_info={
    'name':"ashu",
    "emial":"ashutoshs019@gmail.com",
    "linkedin_url":"https://www.linkedin.com/in/ashutoshsingh19",
    "age":25,
    "weight":60.5,
    "married":False,
    "allergies":["peanuts","milk"],
    "contact_details":{"phone_number":"1234567890","address":"delhi"}

}

patient_1=Patient(**patient_info)

upadate_patient_data(patient_1)