from typing import List

from pydantic import BaseModel

class llmOutputSchema(BaseModel):
    output_list : List[str]