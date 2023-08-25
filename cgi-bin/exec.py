import os
import subprocess

# Define the environment variables
env_variables = {
    "SERVER_PROTOCOL": "HTTP/1.1",
    "REQUEST_METHOD": "POST",
    "PATH_INFO": "/Users/ayassin/Documents/git_files/WebServe_42_Abu_Dhabi/project_code/intra/YoupiBanane/youpi.bla",
    "X-Secret-Header-For-Test": "1"
}

# Set the environment variables
for key, value in env_variables.items():
    os.environ[key] = value

# Define the message to be sent to the CGI script
message = "hello wofgjvbhklmfb djgshjbv jdfbkbsdckjbsDKJhbvkSdfbgnhgflzdjkfvnlkdnsflvkndfljknldfjknlkjdf jkfd kjdflkj ljkdf lfdz  fdzlkj lkj dzlkblj  j jzl z  zlf lzj zbvxlc bcvblcvbl cvbcv blvcb\ndzfbvbdfdfdfzbdzf\nsdfgsdfgdsfdf\ndfgngfdhgnghgfnHBDKhcbKSHDBchBSDKHdcbkhSBCkh SDLKdvlkjSDLVbzdfbxfgcnxfgnrld"

# Execute the CGI script using subprocess with input from a pipe
with subprocess.Popen(['./cgi_tester'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
    stdout, _ = process.communicate(input=message)

# Print the output from the CGI script
print(stdout)

