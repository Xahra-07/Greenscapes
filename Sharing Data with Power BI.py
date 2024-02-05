import requests
import json

# Power BI API endpoint
POWER_BI_API_ENDPOINT = "https://api.powerbi.com/beta/myorg/datasets/{dataset_id}/tables/{table_name}/rows?key={api_key}"

def push_data_to_powerbi(data):
    # Prepare data payload
    payload = {
        "rows": [data]
    }

    # Power BI API parameters
    dataset_id = "dataset_id"
    table_name = "table_name"
    api_key = "powerbi_api_key"

    # Construct API URL
    api_url = POWER_BI_API_ENDPOINT.format(dataset_id=dataset_id, table_name=table_name, api_key=api_key)

    # Send data to Power BI
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        print("Data successfully pushed to Power BI.")
    else:
        print("Failed to push data to Power BI:", response.text)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        push_data_to_powerbi(req_body)
        return func.HttpResponse("Data successfully pushed to Power BI.", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
```
