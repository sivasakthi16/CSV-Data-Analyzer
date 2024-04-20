import os
import pandas as pd
from pandasai import SmartDatalake
from pandasai.responses.streamlit_response import StreamlitResponse
class pandasAi:
    key = "$2a$10$u/o98vFaHhUlkJeMbpkXveiQ//7Gn6aA4P9hhCUp9E.z9zp3RH7vG"
    def __init__(self):
        os.environ["PANDASAI_API_KEY"] = self.key
    def createAgent(self, file):
        csv = pd.read_csv(file)
        self.agent = SmartDatalake(
        [csv],
            config={"verbose": True, "response_parser": StreamlitResponse},
        )

    def query(self, query):
        result = self.agent.chat(query)
        return result
