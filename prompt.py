import sys
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion
import commands

command = sys.argv[1]
topic = sys.argv[2]

kernel = sk.Kernel()
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_text_completion_service("dv", OpenAITextCompletion("text-davinci-003", api_key, org_id))

if (command == '?'):
    command_text = topic
else:
    command_text = getattr(commands, command)(topic)

print(command_text)

command_prompt = kernel.create_semantic_function(command_text)

print(command_prompt())