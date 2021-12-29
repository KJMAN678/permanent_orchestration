import azure.functions as func
import azure.durable_functions as df
from datetime import datetime, timedelta

def orchestrator_function(context: df.DurableOrchestrationContext):
  
    activity_task = context.call_activity("durable-activity")
  
    # 間隔をかけて実行
    yield activity_task
    td = timedelta(minutes=1)
    next_cleanup = context.current_utc_datetime + timedelta(minutes=1)
    yield context.create_timer(next_cleanup)
    context.continue_as_new(None)
    
    # タイムアウト
    deadline = context.current_utc_datetime + timedelta(minutes=10)
    timeout_task = context.create_timer(deadline)
    winner = yield context.task_any([activity_task, timeout_task])
    if winner == activity_task:
        timeout_task.cancel()
        return True
    elif winner == timeout_task:
        return False

main = df.Orchestrator.create(orchestrator_function)