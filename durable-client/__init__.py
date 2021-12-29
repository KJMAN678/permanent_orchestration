import logging

from azure.durable_functions import DurableOrchestrationClient
import azure.functions as func

async def main(req: func.HttpRequest, starter: str, message):

    logging.info(starter)
    client = DurableOrchestrationClient(starter)

    # Orchestratorの開始
    instance_id = await client.start_new('durable-orchestrator')
    response = client.create_check_status_response(req, instance_id)
    message.set(response)