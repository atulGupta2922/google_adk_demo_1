from google.adk.agents.llm_agent import Agent
from google.adk.planners import BuiltInPlanner
from google.genai import types

USER_DATA = {
    "user_21": {
        'credit_score': 751,
        'number_of_applications': 6
    },
    "user_22": {
        'credit_score': 680,
        'number_of_applications': 7
    },
    "user_23": {
        'credit_score': 720,
        'number_of_applications': 4
    },
    "user_24": {
        'credit_score': 805,
        'number_of_applications': 1
    },
    "user_25": {
        'credit_score': 690,
        'number_of_applications': 3
    },
    "user_26": {
        'credit_score': 640,
        'number_of_applications': 5
    },
    "user_27": {
        'credit_score': 775,
        'number_of_applications': 2
    },
    "user_28": {
        'credit_score': 710,
        'number_of_applications': 6
    },
    "user_29": {
        'credit_score': 760,
        'number_of_applications': 1
    },
    "user_30": {
        'credit_score': 695,
        'number_of_applications': 3
    },
    "user_31": {
        'credit_score': 730,
        'number_of_applications': 4
    },
    "user_32": {
        'credit_score': 800,
        'number_of_applications': 2
    },
    "user_33": {
        'credit_score': 670,
        'number_of_applications': 5
    },
    "user_34": {
        'credit_score': 785,
        'number_of_applications': 1
    },
    "user_35": {
        'credit_score': 715,
        'number_of_applications': 3
    },
    "user_36": {
        'credit_score': 660,
        'number_of_applications': 4
    },
    "user_37": {
        'credit_score': 790,
        'number_of_applications': 2
    },
    "user_38": {
        'credit_score': 705,
        'number_of_applications': 6
    },
    "user_39": {
        'credit_score': 750,
        'number_of_applications': 1
    },
    "user_40": {
        'credit_score': 680,
        'number_of_applications': 3
    }
}

def get_credit_score(user_id: str) -> int:
    """
    Return user's credit score associated with user_id
    
    :param user_id: user_id of the user queried for
    :type user_id: str
    :return: credit score of the user
    :rtype: int
    """
    return USER_DATA[user_id]['credit_score'] if USER_DATA[user_id] is not None else 0

def get_number_of_applications(user_id: str) -> int:
    """
    Returns number of credit-card applications in last three months for the provided user_id
    
    :param user_id: user_id of the user queried for
    :type user_id: str
    :return: number of credit-card applications
    :rtype: int
    """
    return USER_DATA[user_id]['number_of_applications'] if USER_DATA[user_id] is not None else 0

planner = BuiltInPlanner(
    thinking_config= types.ThinkingConfig(
        include_thoughts=True,
        thinking_budget=1024
    )
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A professional financial analyst who analyzes user credit-score and number of credit card applications in last 3 months and approves or denies the applications.',
    instruction='A professional financial analyst who analyzes user credit-score and number of credit card applications in last 3 months and approves or denies the applications. Use tools like get_credit_score and get_number_of_applications to get the credit score and number of credit-card applications in last 3 months.',
    tools=[get_credit_score, get_number_of_applications],
    planner=planner
)
