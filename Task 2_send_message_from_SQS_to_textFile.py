import boto3

#connect to AWS SQS
AWS_ID_VLORJAN = 'your-aws-id'
AWS_SECRETID_VLORJAN = 'aws-secret-key'

ConnectToSqs = boto3.resource('sqs', aws_access_key_id=AWS_ID_VLORJAN,
    aws_secret_access_key=AWS_SECRETID_VLORJAN,
    region_name='your region'
)

#checks and verifies that the name of the queue below is the same as the on inside AWS SQS
GetNameOfQueue = 'Vlorjan_Queue.fifo'
collect = ConnectToSqs.get_queue_by_name(QueueName=GetNameOfQueue)

#a for each loop which says that we iterate over the message list once.
for i in range(0, 1):
    message_list = collect.receive_messages(VisibilityTimeout=1, MaxNumberOfMessages=10, WaitTimeSeconds=5)
    for messages in message_list:
        #now we open the empty_text_file.txt and write into it.
        with open("empty_text_file.txt", 'a') as newTextFile:
            newTextFile.write(format(messages.body))