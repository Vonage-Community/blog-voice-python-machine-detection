# blog-voice-python-machine-detection

This repository shows you how to use the Vonage Voice API capabilities to detect Voicemail / human interaction with a real-world application with Python Flask. For more information, please see the blog post at [HERE](https://developer.vonage.com).

* [Requirements](#requirements)
* [Installation and Usage](#installation-and-usage)
  * [API Credentials](#api-credentials)
  * [Running the Application](#running-the-application)
* [Contributing](#contributing)
* [License](#license)

## Requirements

This application requires that you have the following installed locally:

* [Python 3.8 or newer](https://www.python.org/downloads/)
* [Flask 2.3.0 or newer](https://pypi.org/project/Flask/)
* [ngrok 3.30 or newer](https://ngrok.com/download)

Additionally, to test the application, you must have a Vonage account and have a virtual number to place calls across different carriers. You can create a Vonage account for free or manage your Vonage account details at the [Vonage Dashboard](https://developer.vonage.com).

## Installation and Usage

You can run this application by first creating a virtual environment to manage dependencies for your project. 

Once you have created a virtual environment, activate it and install the dependenciees. Change the directory into the directory of the application and start running the Flask application.

If you are using ngrop, then you can start the ngrok ingress application as well.
 
### Setting the Phone Numbers

You'll need to set the `<YOUR_VIRTUAL_NUMBER>` and `<CALL_CAMPAIGNER_PHONE_NUMBER>` phone numbers that the application uses.

### Running the Application

Once you have your Flask application up and running, you can go ahead and start sending the calls either by using curl command or from Postman. 


## Contributing

We ❤️ contributions from everyone! If you see something that needs fixed, then please follow the [GitHub Flow](https://guides.github.com/introduction/flow/index.html) and we'll try to incorporate it.

## License

This project is under the [Apache 2.0 License](LICENSE)

