#!/usr/bin/env python
import sys
from financial_agent_investment_recommendation_chat.crew import FinancialAgentInvestmentRecommendationChatCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'company_name': 'ITC Limited',
        'target_website_url': 'https://www.screener.in/company/ITC/consolidated/',
        'peer_list': 'GODPHI,GTCIND,HUL,NESTLEIND,PGHH,RELIANCE'
    }
    FinancialAgentInvestmentRecommendationChatCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_name': 'Coal India',
        'target_website_url': 'https://www.screener.in/company/COALINDIA/consolidated/',
        'peer_list': 'VEDL,LLOYDSME,NMDC,KIOCL,GMDCLTD'
    }
    try:
        FinancialAgentInvestmentRecommendationChatCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FinancialAgentInvestmentRecommendationChatCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'company_name': 'TATAMOTORS',
        'target_website_url': 'https://www.screener.in/company/TATAMOTORS/consolidated/',
        'peer_list': 'ASHOKLEY,EICHERMOT,HEROMOTOCO,MAHINDRA,MARUTI'
    }
    try:
        FinancialAgentInvestmentRecommendationChatCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
