import boto3
client = boto3.client('ec2')
response= client.run_instances(
   ImageId='ami-0150ccaf51ab55a51',
   InstanceType='t2.micro',
   KeyName='test',
   MaxCount='1',
   MinCount='2'
)



