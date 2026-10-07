import os
import json
import argparse
from google import genai
from google.genai import errors

if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("CRITICAL: GEMINI_API_KEY or GOOGLE_API_KEY is missing from environment context.")

client = genai.Client()

def parse_arguments():
    """CLI argument parser for decoupled pipeline targeting."""
    parser = argparse.ArgumentParser(description="Enterprise SaaS Spend Optimization & Access Governance Engine.")
    parser.add_argument("--src", type=str, help="Path to the corporate SaaS usage JSON payload.", default="corporate_saas_inventory.json")
    return parser.parse_args()

def ingest_saas_inventory(file_path):
    """Safely ingests external software usage datasets."""
    expanded_path = os.path.abspath(os.path.expanduser(file_path))
    if not os.path.exists(expanded_path):
        raise FileNotFoundError(f"Pipeline Failure: Target database file missing at {expanded_path}")
    with open(expanded_path, "r") as f:
        return json.load(f)

def run_spend_optimization_audit(saas_data):
    """Orchestrates Gemini 2.5 to analyze contract data, identify financial leakages, and build a runbook."""
    prompt = f"""
    You are an automated Enterprise SaaS Spend Optimization Specialist and IT Asset Governance Agent.
    Ingest the following application license usage report. Calculate financial waste, identify critical access vulnerabilities (like terminated employees holding active licenses), and recommend optimization actions.

    SaaS Usage Payload:
    {json.dumps(saas_data, indent=2)}

    Output your optimization assessment strictly in clean Markdown with this exact schema:
    # Enterprise SaaS Optimization & Spend Report
    ## 1. Executive Cost-Benefit Summary (Quantify immediate monthly/annualized savings)
    ## 2. Identified Access Vulnerabilities & Ghost Accounts (Highlight specific terminated or inactive users)
    ## 3. Contract Realignment & Deprovisioning Action Items (Clear task lists for helpdesk offboarding)
    """
    print("Analyzing contract data and running budget calculations via Gemini 2.5...")
    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
    return response.text

def publish_report(report_data):
    """Outputs the analytical payload flat to a markdown asset."""
    output_path = "saas_spend_optimization_report.md"
    with open(output_path, "w") as f:
        f.write(report_data)
    print(f"[Success] Budget optimization report written flat to: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    try:
        args = parse_arguments()
        inventory = ingest_saas_inventory(args.src)
        report = run_spend_optimization_audit(inventory)
        publish_report(report)
    except errors.APIError as api_err:
        print(f"Gemini Engine Failure: {api_err}")
    except Exception as error:
        print(f"\n[!] Pipeline Execution Failure: {str(error)}")
