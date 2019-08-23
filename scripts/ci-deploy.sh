#! /bin/bash
# exit script when any command ran here returns with non-zero exit code
set -e

#envsubst < nginx.yml > nginx.yml.out
#mv nginx.yml.out nginx.yml

echo "$KUBERNETES_CLUSTER_CERTIFICATE" | base64 --decode > cert.crt

./kubectl --kubeconfig=/dev/null --server=https://$KUBERNETES_SERVER:6443 --certificate-authority=cert.crt --token=$KUBERNETES_TOKEN apply -f nginx.yml
