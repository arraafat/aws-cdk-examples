from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_s3_notifications,
    core
)


class S3TriggerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create lambda function
        function = _lambda.Function(self, "lambda_function",
                                    function_name="<Optional to define your function name>",
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    handler="lambda-handler.main",
                                    code=_lambda.Code.asset("./lambda"))
        # create s3 bucket
        s3 = _s3.Bucket(self, "s3bucket")

        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)

        # assign notification for the s3 event type (ex: OBJECT_CREATED)for specific prefix and suffix 
        s3.add_event_notification(_s3.EventType.OBJECT_CREATED, notification,_s3.NotificationKeyFilter(prefix='/rowdata', suffix='.csv'))
