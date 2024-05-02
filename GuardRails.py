from guardrails import Guard, OnFailAction
from guardrails.hub import RegexMatch

guard = Guard().use(
    RegexMatch, regex="\(?\d{3}\)?-? *\d{3}-? *-?\d{4}", on_fail=OnFailAction.EXCEPTION
)

guard.validate("123-456-7890")  # Guardrail passes

try:
    guard.validate("1234-789-0000")  # Guardrail fails
except Exception as e:
    print(e)