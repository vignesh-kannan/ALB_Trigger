# rean-lambda-detect-create-delete-ALBs
CloudWatch Event Triggers the lambda when ALB is created or deleted 

Primary Usage

Triggers a Lambda when ALB is created or delete

-	Monitors the creation and deletion of ALBs using CloudWatch Event Logs
-	Triggers the lambda when created or deleted
-	Lambda will fetch the account id and AWS region when ALB is created
-	Lambda will figure out whether this is the last ALB or not when ALB is deleted

components & Libraries

-	CloudWatch
-	Application Load Balancer
-	Lambda
-	Python(Boto3)

Permissions:

- Permission given to lambda to monitor Cloudwatch Events and to read the logs in cloudwatch

Procedure

- once the ALB is created Lambda function fetches the Account id and AWS Region and write the logs in Cloudwatch
- if the ALB is deleted Lambda function checks whether this is the last ALB or not  
