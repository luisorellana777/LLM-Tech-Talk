import re
from google.cloud import aiplatform
from app.config import PROJECT_ID, REGION, ENDPOINT_ID

aiplatform.init(
    project = PROJECT_ID,
    location = REGION
)

ENDPOINT = aiplatform.Endpoint(
    endpoint_name=(
        f"projects/{PROJECT_ID}"
        f"/locations/{REGION}"
        f"/endpoints/{ENDPOINT_ID}"
    )
)

def get_diagnosis(question: str) -> str:

    prompt = ["[INST]", question, "[/INST]"]

    prediction = ENDPOINT.predict(
        instances=["".join(prompt)],
        parameters={
            "temperature": 1.0,
            "max_new_tokens": 512,
            "top_k": 50,
            "top_p": 1.0,
            "repetition_penalty": 1.0
        }
    )

    question_and_diagnosis = prediction.predictions[0][0]['generated_text']
    diagnosis = re.sub(r'^\[INST\].*?\[/INST\]\s*', '', question_and_diagnosis, flags=re.DOTALL)
    return diagnosis