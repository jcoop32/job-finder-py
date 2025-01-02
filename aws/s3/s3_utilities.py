import boto3
import os
import tempfile

s3 = boto3.client("s3")
bucket_name = "job-finder-py"
# file_path = "/Users/joshcooper/job-finder-py/resume_uploads/jjmc-resume-2024-fs.pdf"


# def upload_file_to_s3(file_path):
#     """Uploads a file to an S3 bucket."""

#     filename = os.path.basename(file_path)
#     try:
#         s3.upload_file(file_path, bucket_name, filename)
#         print(f"File uploaded successfully to s3://{bucket_name}/{filename}")
#     except Exception as e:
#         print(f"Error uploading file: {e}")


def upload_file_to_s3(file_obj):
    """Uploads a file object to an S3 bucket."""
    filename = os.path.basename(file_obj)
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file_obj.save(
                temp_file.name
            )  # Save the uploaded file to the temporary file
            temp_file_path = temp_file.name

        # Upload the temporary file to S3
        s3.upload_file(temp_file_path, bucket_name, filename)
        print(f"File uploaded successfully to s3://{bucket_name}/{filename}")

        # Remove the temporary file
        os.remove(temp_file_path)

        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False


# upload_file_to_s3(file_path, bucket_name)


def get_presigned_url(s3_key, expiration=3600):
    """Generates a pre-signed URL for an S3 object.

    Args:
        bucket_name: The name of the S3 bucket.
        s3_key: The key of the S3 object.
        expiration: The expiration time of the URL in seconds (default: 3600 seconds).

    Returns:
        A pre-signed URL as a string.
    """
    try:
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": s3_key},
            ExpiresIn=expiration,
        )
        return url
    except Exception as e:
        print(f"Error generating pre-signed URL: {e}")
        return None


# print(get_presigned_url("jjmc-resume-2024-fs.pdf"))

# print(get_s3_object_data("jjmc-resume-2024-fs.pdf"))
