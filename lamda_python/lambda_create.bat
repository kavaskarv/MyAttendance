aws lambda create-function \
   --function-name  "helloworld"\
   --runtime "python2.7" \
   --role "arn:aws:iam::368567762574:role/service-role/lambda_s3-role-c7j1he10" \
   --handler "/lambda_python/index.hanlder" \
   --timeout  5 \
   --region "us-west2"
