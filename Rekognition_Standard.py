# Python code to call with AWS Rekognition API and ask it to classify an image
import boto3

def show_labels(bucket,photo, min_confidence):
     

    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MinConfidence=min_confidence)
     
    print('Detected custom labels for ' + photo)    
    for Label in response['Labels']:
        print('Label ' + str(Label['Name'])) 
        print('Confidence ' + str(Label['Confidence'])) 

    return len(response['Labels'])

def main():

    bucket="my-bird-bucket-new"
    photo="010.Red_winged_Blackbird/Red_Winged_Blackbird_0011_5845.jpg"
    min_confidence=90
    
    label_count=show_labels(bucket,photo, min_confidence)
    print("Custom labels detected: " + str(label_count))

if __name__ == "__main__":
    main()
