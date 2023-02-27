from airflow.operators.bash_operator import BashOperator

cleanup = BashOperator(
    task_id = 'cleanup_task',
    bash_command = 'cleanup.sh',
    dag=analytics_dag
)

consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command='consolidate_data.sh',
    dag=analytics_dag
)

push_data = BashOperator(
    task_id='pushdata_task',
    bash_command='push_data.sh',
    dag=analytics_dag
)