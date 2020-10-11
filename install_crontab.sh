cmd="0 0 * * * cd ${PWD} && python3 lastbye.py" 
echo "${cmd}" > /etc/cron.d/lastbye
