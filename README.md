# Data Entry Clerk

[![Codeship](https://img.shields.io/codeship/00e3e560-5bf2-0135-71f7-12b712633443.svg)](https://app.codeship.com/projects/237709/)
[![Code Climate](https://img.shields.io/codeclimate/github/Automatiqa/data-entry-clerk.svg)](https://codeclimate.com/github/Automatiqa/data-entry-clerk)

> Hello, I'm your friendly _data entry clerk_. I take whatever data you give me
and store them in your database for later processing.

**Data Entry Clerk** might be a little demeaning, but it describes the purpose
of this project perfectly: To be able to analyse data, you need to have data.
The DEC stores whatever data you give it in a database for later processing.

Most external services allow data to be shared via [webhooks][webhook]. The DEC
provides an endpoint that accepts such webhooks and stores their payload in a
database.

While the application is set up in a way that allows different deployments
(e.g. via Docker), the initial implementation is made with [AWS Lambda][lambda]
and [DynamoDB] in mind.

## Development

To extend the service or customize it, either fork or clone this repository.

### Installation

We recommend that you create a [virtual environment](virtualenv) to isolate the
Python interpreter and all dependencies from your system Python or any other
projects you're working on.

```bash
virtualenv --python=$(which python3) .venv
source .venv/bin/activate
```

Then, install DEC's dependencies:

```bash
pip install -r requirements.txt
```

After that, you can hack away and make any changes you require to make the code
work for you. 😊

### DynamoDB

The default backend for DEC is Amazon's [DynamoDB]. For development and
testing, you can run an instance locally. First, go to the following page and
download the package from your nearest region:

[Setting Up DynamoDB Local](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html#DynamoDBLocal.DownloadingAndRunning)

Then, extract its contents into the `dynamodb` directory. Once you've done
this, you can use the script `start_dynamodb.sh` in `scripts` to run the
server.

**Note:** When starting the database for the first time, make sure to run
`create_table.sh` in a different terminal as well.

### Running the server

During development, you can run the server by simply starting the app:

    FLASK_APP=app.py flask run

## License

Copyright (c) 2017 Automatiqa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[dynamodb]: https://aws.amazon.com/dynamodb/
[lambda]: https://aws.amazon.com/lambda/
[virtualenv]: http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
[webhook]: https://en.wikipedia.org/wiki/Webhook
