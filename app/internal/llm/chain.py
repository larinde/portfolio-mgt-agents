from langchain_core.messages import HumanMessage

from .prompt import get_prompt

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def invoke_chain(message: HumanMessage):
    """
    Invoke the chain.

    Args:
        message (HumanMessage): The input message to respond to.

    Returns:
        str: The response from the chain.
    """
    from .model import llmModel
    
    prompt = get_prompt(message)
    logger.info(f" --- Invoking chain with prompt: {prompt}")
    return llmModel.invoke(prompt)