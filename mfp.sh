#! /bin/sh

case $1 in
  "start")
    echo "Starting myFlaskProject ..."
    . venv/bin/activate
    touch log
    echo "Start signal received at `date`" >> log
    cd web
    ./myFlaskProject.py >> ../log 2>&1&
    disown %./myFlaskProject.py 
    echo "Done"
    ;;
  "stop")
    echo "Killing myFlaskProject ..."
    kill `pgrep -f "python3 ./myFlaskProject.py"`
    if [[ $? ]]; then
      echo "Stop signal received at `date`" >> log
      echo "Done"
    else
      echo "Failed. Please use kill -9 manually"
    fi
    ;;
  *)
    echo "Usage: $0 start|stop"
    ;;
esac
