declare -i counter=0
declare -i n_clients=2          #n
declare -i limit_requests=10  #l
declare -i max_holded_files=40  #m
request_time_offset="4.0"       #s

# Parse options
while [[ $# -gt 0 ]]; do
  case $1 in
    -n)
      n_clients="$2"
      shift
      shift
      ;;
    -l)
      limit_requests="$2"
      shift
      shift
      ;;
    -m)
      max_holded_files="$2"
      shift
      shift
      ;;
    -s)
      request_time_offset="$2"
      shift 
      shift
      ;;
    *)
      echo "Unknown arg: $(opt)"
      exit 1
  esac
done

# Print out the values of the options
echo "Launching ($n_clients) clients with parameters:"
echo "> limit_requests : $limit_requests"
echo "> max_holded_files : $max_holded_files"
echo "> request_time_offset : $request_time_offset"

while [[ counter -lt $n_clients ]]; do
  echo "launching client " $counter
  python3 auto_client.py $limit_requests $max_holded_files $request_time_offset
  ((counter++))
done