import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

class ChatBot():

    def __init__(self):
        kernel = sk.Kernel()
        api_key, org_id = sk.openai_settings_from_dot_env()
        kernel.add_text_completion_service("dv", OpenAIChatCompletion("gpt-3.5-turbo-16k", api_key, org_id))

        sk_prompt = """
        ChatBot can have a conversation with you about any topic.
        It can give conscise answers or say 'I don't know' if it does not have an answer.

        {{$history}}
        User: {{$user_input}}
        ChatBot: """


        self.chat_function = kernel.create_semantic_function(sk_prompt, "ChatBot", max_tokens=2000, temperature=0.7, top_p=0.5)
        self.context = kernel.create_new_context()
        self.context["history"] = ""

    def chat(self, input_text: str) -> None:
        self.context["user_input"] = input_text
        answer = self.chat_function(context=self.context)
        print(answer)
        self.context["history"] += f"\nUser: {input_text}\nChatBot: {answer}\n"