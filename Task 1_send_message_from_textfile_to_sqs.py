import boto3

AWS_ID_VLORJAN = 'your-aws-id'
AWS_SECRETID_VLORJAN = 'your-aws-key'

ConnectTosqs = boto3.resource('sqs', aws_access_key_id=AWS_ID_VLORJAN,
    aws_secret_access_key=AWS_SECRETID_VLORJAN,
    region_name='your-region'
)

NameOfQueue = ('Vlorjan_Queue.fifo')

response = ConnectTosqs.create_queue(QueueName=NameOfQueue,
Attributes={'FifoQueue': 'true',
'ContentBasedDeduplication': 'true'})

queueResponse = ConnectTosqs.get_queue_by_name(QueueName='Vlorjan_Queue.fifo')

#Opens the text file "Messages.txt".
with open("Messages.txt",'r') as textFile:

    '''For each loop that iterates through the file and 
    sends the different lines in to the queue, 
    these messages are stored together in "group1"'''
    for lines in textFile:
        queueResponse.send_message(MessageBody=lines, MessageGroupId='Group1')