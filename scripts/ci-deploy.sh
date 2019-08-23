#! /bin/bash
# exit script when any command ran here returns with non-zero exit code
set -e

echo "$KUBERNETES_CLUSTER_CERTIFICATE" | base64 --decode > cert.crt

./kubectl --kubeconfig=".kune/config" --server=https://$KUBERNETES_SERVER:6443 --certificate-authority=cert.crt --token=$KUBERNETES_TOKEN apply -f webservice.yml
