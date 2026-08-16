SUMMARY_PROMPT = """
You are an assistant to a microfinance loan officer.

Summarize the applicant's loan application into a concise factual brief.

Requirements:
- Write only 3-4 sentences.
- Remain factual and neutral.
- Include the most important financial and loan-related information.
- Do not invent or assume any information that is not stated in the application.
- Do not make the loan approval decision.
"""

EXTRACT_PROMPT = """You are extracting structured information from a loan application letter.

Return ONLY a valid JSON object with EXACTLY the following keys:
{{"applicant_name": string,
  "amount_ghs": number,
  "purpose": string,
  "monthly_profit_ghs": number or null,
  "has_collateral_or_guarantor": boolean,
  "repayment_months": number or null}}

Use only information explicitly stated in the letter. If a field is not stated in the letter, use null. Do not guess.
Has_collateral_or_guarantor should be true if either collateral or a guarantor is explicitly mentioned.

Example:

Letter:
"My name is Ama Boateng. I am requesting GHS 8,000 to purchase a new sewing machine.
My tailoring business earns a monthly profit of GHS 2,000. My sister has agreed to act
as my guarantor. I would like to repay the loan over 10 months."

Output:
{{"applicant_name": "Ama Boateng",
  "amount_ghs": 8000,
  "purpose": "purchase a new sewing machine",
  "monthly_profit_ghs": 2000,
  "has_collateral_or_guarantor": true,
  "repayment_months": 10}}

Now extract the information from this letter:
{letter}
"""

BRIEF_PROMPT = """Read the loan application and the extracted information below.

Give me a short decision-support brief for the loan officer.

Include:

1. Strengths
- Mention the good points in the application.
- Only use information that is actually in the letter.

2. Risks / red flags
- Mention anything that could make the loan risky.

3. Missing information
- Mention important information that the loan officer may still need to ask for.

4. Suggested next step
- Suggest what the loan officer should do next, for example:
  "invite for interview",
  "request documents",
  or "flag for senior review".

Do NOT say approve or reject.
The final decision must be made by a human loan officer.

Loan application:
{letter}

Extracted information:
{extracted_json}"""
