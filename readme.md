# scraping web finding the best product based on custom data

This project is only of education purpose not for realtime

- the main intension of this project is working with realtime data for custom usecases for maintaing good result and making decisions for best result

- we are using selenium for data grabing in python language
- finding the result for better understand for accuracy and decission making for budget case studies

# OpenRouter LLM Model Runner

A Python script to run multiple LLM models via OpenRouter API with reasoning capabilities for product review analysis.

## Features

- Supports 9+ different LLM models (NVIDIA, Google, DeepSeek, Meta, OpenAI, etc.)
- Reasoning-enabled API calls for better outputs
- Automatic JSON saving of model responses
- Product rating extraction from text files

## Supported Models

| Model                                                | Provider |
| ---------------------------------------------------- | -------- |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | NVIDIA   |
| `google/gemma-4-26b-a4b-it:free`                     | Google   |
| `deepseek/deepseek-v4-flash:free`                    | DeepSeek |
| `nvidia/nemotron-3-super-120b-a12b:free`             | NVIDIA   |
| `qwen/qwen3-next-80b-a3b-instruct:free`              | Alibaba  |
| `meta-llama/llama-3.2-3b-instruct:free`              | Meta     |
| `openai/gpt-oss-120b:free`                           | OpenAI   |
| `z-ai/glm-4.5-air:free`                              | Z.ai     |

## Prerequisites

- Python 3.8+
- OpenRouter API key
- Input text file with product data

## Installation

```bash
pip install requests,json,pprint,selenium
```

## prompt data for llm

find the best one product based on rating

# Project File Structure

## Directory Details

| Path                 | Type      | Description                           |
| -------------------- | --------- | ------------------------------------- |
| `run_model.py`       | File      | Main Python script                    |
| `runtimetest/`       | Directory | Contains input text files             |
| `*.txt`              | File      | Product data with ratings and reviews |
| `sample_data_*.json` | File      | Model response output (timestamped)   |
| `README.md`          | File      | Project documentation                 |
| `requirements.txt`   | File      | Python dependencies                   |

## File Naming Convention

- **Input**: `sample_*.txt`
- **Output**: `sample_data_*.json`
