import requests,json
import json,pprint as pp
from datetime import datetime as dt

def models():
    model= ["nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        "google/gemma-4-26b-a4b-it:free",
        "deepseek/deepseek-v4-flash:free",
        "nvidia/nemotron-3-super-120b-a12b:free",
        "qwen/qwen3-next-80b-a3b-instruct:free",
        "meta-llama/llama-3.2-3b-instruct:free",
        "openai/gpt-oss-120b:free",
        "z-ai/glm-4.5-air:free"
        ]
    return model


def file_data():
  data = open("../runtimetest/sample_20260523185724892675.txt","r",encoding='utf-8')
  return data

    
    
# data = open("../runtimetest/sample_20260523185724892675.txt","r",encoding='utf-8')
# model= ["nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
#         "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
#         "google/gemma-4-26b-a4b-it:free",
#         "deepseek/deepseek-v4-flash:free",
#         "nvidia/nemotron-3-super-120b-a12b:free",
#         "qwen/qwen3-next-80b-a3b-instruct:free",
#         "meta-llama/llama-3.2-3b-instruct:free",
#         "openai/gpt-oss-120b:free",
#         "z-ai/glm-4.5-air:free"
#         ]



#files calling 
def promptconstruct(buffer):
  """
    prompt template is mixing with data ....
  """
  buffer = file_data()
  prompt = f'{buffer.read()}\n\n find the best one product  based on rating '
  buffer.close()
  return prompt



def enginworking():

# First API call with reasoning
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": "key",
      "Content-Type": "application/json",
    },
    data=json.dumps({
      "model":models()[-1] ,
      "messages": [
          {
            "role": "user",
            "content": promptconstruct(file_data)
          }
        ],
      "reasoning": {"enabled": True,}
    })
  )

# Extract the assistant message with reasoning_details
# response = response.json()
  return response.json()
# response = response['choices'][0]['message']


def model_output(engin):
  enginworking =engin()
  pp.pprint(enginworking)
  with open(f'sample_data_{dt.now().strftime("%Y%m%d%H%M%S%f")}.json',"w") as fileobj:
      json.dump(enginworking,fileobj,indent=5)

model_output(enginworking)
