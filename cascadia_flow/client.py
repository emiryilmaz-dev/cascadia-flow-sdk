from cascadia_flow import Workflow, Step

flow = Workflow(name="incident-triage")

@flow.step(retries=3)
def classify_ticket(payload: dict) -> dict:
    return {"severity": "high", "summary": payload.get("title", "")}

@flow.step()
def notify_oncall(context: dict) -> str:
    return f"Dispatched alert for: {context['summary']}"

if __name__ == "__main__":
    result = flow.run({"title": "API latency spike in us-west-2"})
    print(result)
