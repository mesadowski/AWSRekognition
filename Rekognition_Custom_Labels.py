
#Code to call AWS Rekognition Custom Labels with an image, and ask it to classify it

import boto3

def show_custom_labels(model,bucket,photo, min_confidence):
     

    client=boto3.client('rekognition')

    s3_connection = boto3.resource('s3')

    s3_object = s3_connection.Object(bucket,photo)
    s3_response = s3_object.get()

    response = client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MinConfidence=min_confidence,
        ProjectVersionArn=model)
     
    print('Detected custom labels for ' + photo)    
    for customLabel in response['CustomLabels']:
        print('Label ' + str(customLabel['Name'])) 
        print('Confidence ' + str(customLabel['Confidence'])) 

    return len(response['CustomLabels'])

def main():

    bucket="my-bird-bucket-new"
    photo="010.Red_winged_Blackbird/Red_Winged_Blackbird_0011_5845.jpg"
    model='arn:aws:rekognition:us-east-1:153104479668:project/Birds/version/Birds.2020-11-02T20.47.06/1604368026648'
    min_confidence=90
    
    label_count=show_custom_labels(model,bucket,photo, min_confidence)
    print("Custom labels detected: " + str(label_count))


if __name__ == "__main__":
    main()
