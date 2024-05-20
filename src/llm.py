import os
import requests

class Llm:
    url = 'https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct'
    hf_api_key = os.getenv('HF_API_KEY')    

    def query(self, query: str):
        response = requests.post(
            self.url,
            headers={'Authorization': f'Bearer {self.hf_api_key}'},
            json={'inputs': query})
        return response.json()[0]['generated_text']

    def filter_relevant_elements(self, category, elements, stringify_fn):
        assistant = 'Assistant: '
        prompt = '\n'.join([
            f'User: Print out the items relating to {category}. Only print out the headlines, no additional explanations.',
            '\n'.join([f'- {stringify_fn(x)}' for x in elements]),
            assistant,
        ])
        response = self.query(prompt)[len(prompt):]
        return [x for x in elements if stringify_fn(x) in response]