POD_NAME=$1

while true; do
    POD_STATUS=$(kubectl get pods $POD_NAME -o 'jsonpath={..status.conditions[?(@.type=="Ready")].status}')
    echo "$POD_NAME is ready: $POD_STATUS" 
    [ $POD_STATUS != "True" ] || break
    sleep 0.5
done	