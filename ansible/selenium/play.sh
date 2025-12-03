ENV="${ENV:-115}"
CODE="${CODE:-rke2}"
VER="${VER:-latest}"

echo "Deploying with env=$ENV, code=$CODE, ver=$VER"

ansible-playbook deploy.yml -e "env=$ENV code=$CODE ver=$VER"
