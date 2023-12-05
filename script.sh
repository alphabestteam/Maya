ALL_PODS=$(kubectl get pods -n my-first-namespace) #Gets all the pods from the command get pods.
RUNNING_PODS=$(echo "$ALL_PODS" | awk '$3 == "Running" {print $1}') 
#echo "$ALL_PODS" ---> prints the result of the filter
# | ---> takes the output of the left side and pass it as the input of the right side
#awk '$3 == "Running" {print $1}')  ---> takes all the pods given by the echo command, and runs on them and with $3, 
#the awk command checks the third column (STATUS column), if the value in each row in the column is equqal to Running, if yes
# it prints in that row the first column (NAME column), which is the name of the running pod.
echo "$RUNNING_PODS" #prints all the running pods.

