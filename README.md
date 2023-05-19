# PoC using Semantic Kernel 

PoC project to help myself learning with the power of AI using [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel) :)
Created reusable prompts to ask commons questions.

# Usage

## Install the latest package:

```sh
  python -m pip install --upgrade semantic-kernel
```

## Create .env file 

Create an `.env` file with 
[Open AI API Key](https://openai.com/api/) or
[Azure Open AI service key](https://learn.microsoft.com/azure/cognitive-services/openai/quickstart?pivots=rest-api)

```
OPENAI_API_KEY=""
OPENAI_ORG_ID=""
AZURE_OPENAI_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
```

## Call the prompt command with a topic

At the root folder of this project, run the `prompt.py` script and pass a command and a topic as arguments
```sh
# python ./prompt <COMMAND> "<TOPIC>"
# Example:
  python ./prompt tradeoff "use microservices or monolith"
```

## Available commands
Commands can be seen in the `command.py` file. YOu can create and add your own commands as you wish :)
|Command|Description|
|--|--|
| tradeoff | I'm trying to decide if I should {topic}. Give me a list of pros and cons to help me decide why should I take or not this decision. |
| lessons | Analyse the best performances for {topic}. Give me a list of most important lessons I can learn from these best performances to leverage my productivity.  |
| learning | I'm currently learning about {topic}. Give me a list of questions that can test my knowledge. Identify knowledge gaps on my answers and give me better answers to fulfill those gaps. |
| report |  I'm writing a report about {topic}. Research and write a detailed report with a step by step guides that will help readers to understand how to {result}. |
| skills | I wan to learn {topic}. Create a 30 days plan that would help a beginners like me  to learn this skill from zero. |
| speech | Topic: {topic}<br> Public: Business Executives<br> Format: Speech\n Tone: Educational and Inspiring<br> Additional instructions: The speech must be less than 15 minutes long |
| paretto | I want to learn about {topic}. Identify and share the 20% most important lessons from the topic and help me understand 80% of them |
| summary | Summarize the text below in less than 500 words. Create a list of topics of most important lessons with brief explanation of each topic\n {text} |
