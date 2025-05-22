# 🔍 What is Pydantic?

**Pydantic** is a Python library used for **data validation** and **settings management** using Python type annotations. It helps ensure that data inputs to your Python programs are correct and well-structured, especially when dealing with complex data types like nested dictionaries, lists, or JSON data.


Pydantic provides:

- **Data parsing:** Converts input data (e.g. JSON or dicts) into Python objects.

- **Data validation:** Automatically validates types and constraints (like `int`, `str`, `email`, etc.).

- **Error reporting:** Gives clear and structured error messages if validation fails.

- **Type hints enforcement:** Uses Python type hints (annotations) to enforce correct types.

It is widely used in FastAPI, which depends on Pydantic for request/response models and input validation

## ✅ Why Use Pydantic?
Here are key benefits:


- `Validation:`	Validates fields based on types and custom rules.

- `Parsing` :	Converts incoming data into correct types.

- `Auto error messages :`	Clear and structured validation errors.
- `Easy JSON serialization :`	Built-in .dict() and .json() methods.

- `Immutable/Mutable models` -	Choose if data should be read-only or modifiable.

- `Nested models:`	Supports deeply nested schemas.

- `Fast:`	Built with performance in mind, uses dataclasses under the hood (in Pydantic v2)

# 📦 Example

```
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int = 18  # default value

# Valid input
user = User(id=1, name="Alice", email="alice@example.com")
print(user.dict())

# Invalid input
User(id='abc', name="Bob", email="not-an-email")

```

The second instantiation will raise a ValidationError with details about what's wrong.


## ✅ Field Validator?

A field validator is defined using the @field_validator decorator (in **Pydantic v2**), or @validator (in **Pydantic v1**), and is used to:

- Enforce custom rules for a single field.

- Normalize or transform values (e.g. trim whitespace, format phone numbers).

- Raise errors if the input is invalid.

## **Syntax (Pydantic v2)**

```
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v.lower()  # convert to lowercase
```

## 🔍 What Happens Here?

- Validates the username field.

- Ensures it is alphanumeric.

- Converts it to lowercase before storing.

## **✅ Model Validator**

- It runs **after all fields are validated individually**.

- It can access and validate the **entire model instance.**

- It’s useful for logic like: “if `a` is set, then `b` must be greater than `x`”.

## **✅ Nested Model**

A nested model lets you compose complex schemas by reusing smaller models. Pydantic will automatically validate the nested structure.

## **🔄 Automatic Parsing and Validation**

Pydantic will:

- Automatically create Address and Order objects from dictionaries.

- Validate types at all levels.

- Raise errors if any nested fields are missing or invalid.

## **✅Computed Filed**

A computed field in Pydantic is a property on a model that is calculated dynamically from other fields, rather than being part of the input data. It does not get passed in, but is automatically computed when you access it.

**Key Features of Computed Fields**

- `Derived value`	Computed from other fields in the model.

- `Read-only`	Cannot be set manually.

- `Optional in output`	Not included in .model_dump() unless explicitly requested.

- `Marked with @computed_field`	In Pydantic v2, this decorator tells Pydantic it's a computed property.

## **🧱 Example (Pydantic v2)**

```
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

```

## **✅ Usage:**

```
r = Rectangle(width=5, height=4)
print(r.area)  # Output: 20.0

# Include computed field in output
print(r.model_dump(include_computed=True))
# {'width': 5, 'height': 4, 'area': 20.0}


```

## **🧠 When to Use Computed Fields  Use computed fields for:**

- Calculated values like total_price = unit_price * quantity

- Read-only indicators like is_expired = datetime.now() > expiry

- Formatting or combining data like full_name = first + last

## **Serialization**


Serialization is the process of converting a Python object (like a dict, class instance, or list) into a format that can be stored or transmitted, such as:

- `JSON`

- `YAML`

- `XML`

- `Bytes` (e.g. for sending over a network)

In contrast, `deserialization` is the reverse process: turning that format back into a usable Python object.

## **📦 Why Is Serialization Important?**

Serialization is used when you want to:

- Send data over a network (e.g., in an API).

- Save data to a file or database.

- Cache or queue data (e.g., in Redis or message queues).

- Log structured data

## **🔧 Example in Python (Using json)**

```
import json

data = {"name": "Alice", "age": 30}

# Serialize to JSON string
json_str = json.dumps(data)

# Deserialize back to Python dict
parsed = json.loads(json_str)

```