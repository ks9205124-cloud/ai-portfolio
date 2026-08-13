from pydantic import BaseModel

class UserOutputSchema(BaseModel):
    output_text : str