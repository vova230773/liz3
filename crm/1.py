import uuid

def generate_guid():
    return str(uuid.uuid4())

print(generate_guid())