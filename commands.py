def tradeoff(topic) :
    return f"""
    I'm trying to decide if I should {topic}.
    Give me a list of pros and cons to help me decide
    why should I take or not this decision.
    """

def lessons(topic) :
    return f"""
    Analyse the best performances for {topic}.
    Give me a list of most important lessons 
    I can learn from these best performances to
    leverage my productivity.
    """

def learning(topic) :
    return f"""
    I'm currently learning about {topic}.
    Give me a list of questions that can test my knowledge.
    Identify knowledge gaps on my answers and give me
    better answers to fulfill those gaps.
    """

def report(topic, result) :
    return f"""
    I'm writing a report about {topic}.
    Research and write a detailed report with a
    step by step guides that will help readers 
    to understand how to {result}.
    """

def skills(topic) :
    return f"""
    I wan to learn {topic}.
    Create a 30 days plan that would help a beginners
    like me  to learn this skill from zero.
    """

def speech(topic):
    return f"""
    Topic: {topic}
    Public: Business Executives
    Format: Speech
    Tone: Educational and Inspiring
    Additional instructions: The speech must be less than 15 minutes long
    """

def paretto(topic):
    return f"""
    I want to learn about {topic}.
    Identify and share the 20% most important 
    lessons from the topic and help me 
    understand 80% of them
    """

def summary(text):
    return f"""
    Summarize the text below in less than 500 words.
    Create a list of topics of most important lessons
    with brief explanation of each topic
    
    {text}
    """